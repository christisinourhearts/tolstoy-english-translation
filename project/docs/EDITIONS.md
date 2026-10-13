# Flagship Editions

This document governs the sentence-level apparatus for works published as **verifiable editions** on christisinourhearts.com (TRANSLATION.md §22). It adds to the normal workflow; it does not replace it.

- The English body lives in `translations/` like every other file, tied to its Russian source by path and SHA-256.
- The edition apparatus lives in `project/editions/<work>/` and is what the website's verifiable-translation page renders.
- The page design itself is specified separately with the website, not in this repository.

## 1. Folder layout

```text
project/editions/<work>/
  README.md          source record, status, plan
  GLOSSARY.md        work glossary and name table (fixed before translating)
  units/
    ch01.jsonl       one JSON record per translation unit
    ch02.jsonl
    ...
  ledger.csv         public discrepancy ledger
```

## 2. Translation units

- **One unit = one Russian sentence** as punctuated in the source file.
- The English may split a unit into several sentences (record the split), but it still maps to one unit.
- Very short connected lines of dialogue may be grouped; record the grouping.
- **ID format:** `WORK-CC-NNN`, e.g. `IVI-02-001` (*Ivan Ilyich*, chapter II, unit 1). The work code avoids confusion with Roman numerals.
- **IDs are permanent.** A later split uses suffixes (`-001a`, `-001b`). Never renumber. A retired ID stays reserved and resolves to a note.
- Each unit stores the SHA-256 of its exact Russian string so any source change is detectable.

## 3. Literal gloss conventions

The literal line exposes the Russian; it never competes with the translation.

- Follow Russian word order wherever it carries emphasis.
- `[brackets]` mark words supplied by English grammar.
- `/` marks genuine alternatives: *ordinary/commonplace*.
- Hyphens join a Russian case-form to its English preposition: *of-Ivan*.
- Keep every repetition and every и (*i*, "and").
- Mark case or aspect only when it changes meaning: *was-dying (impf.)*.
- Do not improve a literal line once written unless it is wrong.

## 4. Notes

- A note (WHY THIS WORDING) answers only material questions.
- First mention of any Russian word: Cyrillic, then transliteration and meaning.
- Name the rule that decided the case (P1–P7, T1–T11).
- Every claim about the Russian is checked against the source file (E13); every claim about the English is checked against the English (E14).

## 5. Status

| Status | Assign when |
|---|---|
| `clear` | no meaningful ambiguity; all checks pass |
| `choice` | several defensible renderings; an editorial choice was made and justified |
| `difficult` | the Russian permits materially different readings, or a P1–P5 loss was unavoidable |
| `textual` | source editions or the variants file differ in a way that affects the English |
| `open` | an unresolved finding exists; **blocks publication** |

`choice`, `difficult` and `textual` units carry reason codes (P, T, or E codes) so the website's filters mean something.

## 6. Unit record

```json
{
  "id": "IVI-02-001",
  "chapter": 2,
  "page": "vol. 26, p. 68",
  "russian": "…",
  "russian_sha256": "…",
  "literal": "…",
  "english": "…",
  "status": "choice",
  "reason_codes": ["P2", "T2", "T3"],
  "note": "…",
  "alternatives": [{"english": "…", "rejected_because": "…"}],
  "revisions": [{"text": "…", "finding": "…", "ledger": "L-0001"}],
  "audits": [
    {
      "audit": "omission",
      "date": "2026-10-06",
      "procedure": "TRANSLATION.md §13",
      "performed_by": "model",
      "independence": "fresh-session",
      "reviewer": "Andrei Evanghelușcă",
      "result": "fail",
      "findings": [{"code": "E2", "detail": "…", "action": "…", "ledger": "L-0001"}]
    }
  ]
}
```

Audits are stored as evidence records, never as `true`/`false` flags. Audit names follow the gauntlet (TRANSLATION.md §15): `source_alignment`, `fidelity`, `omission`, `addition`, `grammar`, `lexical`, `register`, `references`, `english_edit`, `cold`.

## 7. Discrepancy ledger

`ledger.csv` columns: `ledger_id, unit, audit, codes, issue, resolution, date`. Log every finding that led to a change or an editorial decision. The ledger is published: it shows that errors were found and corrected.

## 8. Human review sampling

- Every `difficult` and `textual` unit.
- Every glossary motif at its first and last occurrence.
- A random 10% of the remaining units, drawn with a recorded seed.

## 9. Release checklist (in addition to TRANSLATION.md §17)

- [ ] Glossary and name table frozen; later changes logged as global edits
- [ ] Every unit has a record with literal line and audits
- [ ] Every unit has a cold audit at `fresh-session` or stronger
- [ ] Human sample complete; seed recorded
- [ ] Zero `open` units
- [ ] Every note checked for E13/E14
- [ ] Refrains identical across all occurrences
- [ ] Paragraph count English = paragraph count Russian
