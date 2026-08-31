#!/usr/bin/env python3
"""Flag suspicious beginning/end boundaries in small Russian source Markdown files.

This is a *preflight*, not an automatic corruption detector. It deliberately
prefers false positives over silently translating a truncated source unit.

Examples:
  python tools/preflight_boundaries.py --source-root ../tolstoy-russian-md-audited
  python tools/preflight_boundaries.py --source-zip ../tolstoy-russian-md-audited.zip
  python tools/preflight_boundaries.py --source-root ../tolstoy-russian-md-audited \
      --max-words 1200 --output qa/reports/BOUNDARY_PREFLIGHT.jsonl
  python tools/preflight_boundaries.py --self-test
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, Optional

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "translation_manifest.jsonl"

PAGE_RE = re.compile(r"<!--\s*vol\.\s*\d+,\s*p\.\s*\d+\s*-->")
CYR_RE = re.compile(r"[А-Яа-яЁё]")
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁёÀ-ÿ0-9'-]+")
FOOTNOTE_DEF_RE = re.compile(r"^\[\^[^\]]+\]:")
HEADING_RE = re.compile(r"^#{1,6}\s+")
LIST_RE = re.compile(r"^(?:[-*+]\s+|\d+[.)]\s+)")
QUOTE_RE = re.compile(r"^>\s?")
TERMINAL_RE = re.compile(r"[.!?…»”\"')\]}〉》—–:]\s*$")
LOWER_CYR_START_RE = re.compile(r"^[«\"'“„(\[]*[а-яё]")

# High-information Russian words that very often signal a sentence/clause has
# been cut before its complement. This is only a score booster, never proof.
TAIL_CONNECTORS = {
    "что", "чтобы", "если", "когда", "пока", "потому", "поскольку",
    "который", "которая", "которое", "которые", "которого", "которой",
    "которым", "которую", "как", "словно", "будто", "хотя", "чем",
    "и", "а", "но", "или", "либо", "же", "ведь", "ибо", "дабы",
    "от", "до", "для", "без", "через", "между", "над", "под", "при",
    "в", "во", "на", "к", "ко", "с", "со", "из", "у", "о", "об",
}

# Categories where intentional fragments are common. We still flag them, but
# lower confidence unless another strong signal is present.
FRAGMENT_FRIENDLY = {"notes", "diaries"}

@dataclass
class Finding:
    source_path: str
    category: str
    words: int
    score: int
    severity: str
    reasons: list[str]
    first_text: str
    last_text: str


def load_manifest() -> list[dict]:
    out = []
    with MANIFEST.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def main_body(text: str) -> str:
    text = strip_frontmatter(text)
    # Embedded scholarly apparatus is not the Tolstoy body whose boundary we
    # are testing. Stop before the common apparatus headings.
    lines = text.splitlines()
    body = []
    for line in lines:
        h = line.strip().lower()
        if h in {
            "### editorial notes", "## editorial notes",
            "### редакционные примечания", "## редакционные примечания",
            "### notes", "## notes", "### примечания", "## примечания",
        }:
            break
        body.append(line)
    # Remove trailing footnote definitions if they are not under a heading.
    while body and (not body[-1].strip() or FOOTNOTE_DEF_RE.match(body[-1].strip())):
        body.pop()
    return "\n".join(body)


def clean_line(line: str) -> str:
    line = PAGE_RE.sub("", line).strip()
    line = HEADING_RE.sub("", line)
    line = QUOTE_RE.sub("", line)
    line = LIST_RE.sub("", line)
    # Remove simple Markdown emphasis wrappers without touching punctuation.
    line = line.strip().strip("*_`")
    return line.strip()


def substantive_lines(body: str) -> list[str]:
    out = []
    in_fence = False
    for raw in body.splitlines():
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = clean_line(raw)
        if not s:
            continue
        if s in {"---", "———", "————", "* * *"}:
            continue
        if FOOTNOTE_DEF_RE.match(s):
            continue
        # Pure page numbers / section numerals are not prose boundaries.
        if re.fullmatch(r"[IVXLCDMivxlcdm\d .–—-]+", s):
            continue
        out.append(s)
    return out


def tail_word(s: str) -> str:
    words = WORD_RE.findall(s.lower())
    return words[-1] if words else ""


def analyze_text(path: str, category: str, text: str, words_hint: int = 0) -> Finding:
    body = main_body(text)
    lines = substantive_lines(body)
    first = lines[0] if lines else ""
    last = lines[-1] if lines else ""
    words = words_hint or len(WORD_RE.findall(body))
    score = 0
    reasons: list[str] = []

    if not lines:
        score += 5
        reasons.append("no substantive body text found")
    else:
        if CYR_RE.search(first) and LOWER_CYR_START_RE.search(first):
            score += 2
            reasons.append("body begins with lowercase Cyrillic, possible mid-sentence start")
        if last and not TERMINAL_RE.search(last):
            score += 4
            reasons.append("body ends without terminal punctuation")
        tw = tail_word(last)
        if tw in TAIL_CONNECTORS:
            score += 4
            reasons.append(f"body ends on connector/function word: {tw!r}")
        if last.endswith((",", ";", "(", "[", "—", "–")):
            score += 3
            reasons.append("body ends on punctuation that normally expects continuation")
        if last.count("(") > last.count(")"):
            score += 2
            reasons.append("final substantive line has unmatched opening parenthesis")
        if last.count("[") > last.count("]"):
            score += 2
            reasons.append("final substantive line has unmatched opening bracket")

    # Intentional fragments are common in these families, so make isolated
    # weak signals less alarming. Strong no-punctuation + connector signals
    # remain high.
    if category in FRAGMENT_FRIENDLY and score <= 4:
        score = max(0, score - 2)
        if reasons:
            reasons.append("confidence reduced: category often contains intentional fragments")

    if score >= 7:
        severity = "HIGH"
    elif score >= 4:
        severity = "MEDIUM"
    elif score >= 2:
        severity = "LOW"
    else:
        severity = "CLEAR"

    return Finding(path, category, words, score, severity, reasons, first[:220], last[-220:])


class SourceReader:
    def __init__(self, root: Optional[Path], zip_path: Optional[Path]):
        self.root = root
        self.zip_path = zip_path
        self.zf: Optional[zipfile.ZipFile] = None
        self.prefix = ""
        if zip_path:
            self.zf = zipfile.ZipFile(zip_path)
            names = self.zf.namelist()
            # GitHub/user ZIPs often contain one top-level directory.
            corpus_names = [n for n in names if "/corpus/" in n or n.startswith("corpus/")]
            if corpus_names:
                n = corpus_names[0]
                idx = n.find("corpus/")
                self.prefix = n[:idx]

    def read(self, rel: str) -> str:
        if self.root:
            return (self.root / rel).read_text(encoding="utf-8")
        assert self.zf is not None
        name = self.prefix + rel
        return self.zf.read(name).decode("utf-8")

    def close(self):
        if self.zf:
            self.zf.close()


def self_test() -> int:
    cases = [
        ("normal", "azbuka", "---\ntitle: x\n---\n\n<!-- vol. 21, p. 1 -->\nЖил старик. Он посадил яблоню.\n", "CLEAR"),
        ("known_56", "azbuka", "---\ntitle: x\n---\n\n<!-- vol. 21, p. 56 -->\nМышка вышла гулять и стал кричать так громко, что\n", "HIGH"),
        ("known_59", "azbuka", "---\ntitle: x\n---\n\n<!-- vol. 21, p. 59 -->\nМинистр пошёл к мужику и сказал: ты счастлив. Царь\n", "MEDIUM"),
    ]
    failed = 0
    for name, cat, text, minimum in cases:
        f = analyze_text(name, cat, text)
        ranks = {"CLEAR":0,"LOW":1,"MEDIUM":2,"HIGH":3}
        ok = ranks[f.severity] >= ranks[minimum]
        print(f"{name}: {f.severity} score={f.score} {'PASS' if ok else 'FAIL'} :: {', '.join(f.reasons)}")
        failed += not ok
    return int(bool(failed))


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--source-root", type=Path)
    src.add_argument("--source-zip", type=Path)
    ap.add_argument("--max-words", type=int, default=1200)
    ap.add_argument("--categories", nargs="*", default=None)
    ap.add_argument("--only-untranslated", action="store_true")
    ap.add_argument("--min-severity", choices=["LOW","MEDIUM","HIGH"], default="MEDIUM")
    ap.add_argument("--output", type=Path)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if not args.source_root and not args.source_zip:
        ap.error("one of --source-root or --source-zip is required unless --self-test is used")

    rows = load_manifest()
    ranks = {"CLEAR":0,"LOW":1,"MEDIUM":2,"HIGH":3}
    min_rank = ranks[args.min_severity]
    reader = SourceReader(args.source_root, args.source_zip)
    findings: list[Finding] = []
    scanned = 0
    missing = 0
    try:
        for r in rows:
            if int(r.get("body_word_count_rough") or 0) > args.max_words:
                continue
            if args.categories and r.get("category") not in set(args.categories):
                continue
            if args.only_untranslated and r.get("translation_status") != "untranslated":
                continue
            rel = r["source_ru_path"]
            try:
                text = reader.read(rel)
            except (FileNotFoundError, KeyError):
                missing += 1
                continue
            scanned += 1
            f = analyze_text(rel, r.get("category", ""), text, int(r.get("body_word_count_rough") or 0))
            if ranks[f.severity] >= min_rank:
                findings.append(f)
    finally:
        reader.close()

    findings.sort(key=lambda f: (-f.score, f.source_path))
    payload = [asdict(f) for f in findings]
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as out:
            for item in payload:
                out.write(json.dumps(item, ensure_ascii=False) + "\n")
    else:
        for item in payload:
            print(json.dumps(item, ensure_ascii=False))

    print(f"scanned={scanned} flagged={len(findings)} missing={missing}", file=sys.stderr)
    # Preflight findings do not themselves cause a nonzero exit. Missing source
    # files do, because that means the scan was incomplete.
    return 2 if missing else 0

if __name__ == "__main__":
    raise SystemExit(main())
