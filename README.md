# Tolstoy English Markdown

This repository is the source-linked English counterpart to the audited Russian Tolstoy Markdown corpus snapshot supplied on 2026-08-30.

It is designed so that translation progress survives individual AI sessions and every accepted English file remains traceable to one exact Russian source file and SHA-256.

## Current state

- Russian corpus records: **15,766**
- Reviewed English translations: **32**
- P001: **7 / 7 complete**
- P002: **25 / 25 complete**
- P002 structured bilingual coverage records: **25 PASS**
- Confirmed source-QA errata: **2** quarantined *New Azbuka* segmentation truncations
- Latest mechanical validation: **0 errors**
- Latest Russian-source hash check: **15,766 checked; 0 missing; 0 changed**

No P003 material has been started.

## Read these first

1. `TRANSLATION.md` — governing translation, fidelity, source-QA, and persistence rules.
2. `WORKBENCH.md` — exact resumable project state and next action.
3. `qa/reports/P002_REVIEW.md` — findings from the first scaled batch.
4. `qa/reports/SOURCE_STRESS_TEST.md` — Russian-source integrity stress test.
5. `translation_manifest.jsonl` — one machine-readable record for each Tolstoy source document.
6. `CORPUS_ANALYSIS.md` — structure and scale of the Russian corpus.

The 807 scholarly commentary files remain outside the initial Tolstoy translation manifest and can be handled as a separate editorial project.

## Corpus layout

The English corpus mirrors the Russian corpus paths and filenames:

```text
corpus/works/
corpus/letters/
corpus/diaries/
corpus/notes/
corpus/azbuka/
corpus/krug_chtenija/
```

English titles are metadata. Stable filenames remain source identifiers.

## QA records

- `qa/coverage/` — P002-and-later structured bilingual coverage proofs.
- `qa/source_suspected/` — suspicious or confirmed source-reading/segmentation cases.
- `metadata/source_errata.yml` — confirmed upstream/source-segmentation problems; the Russian repository itself is never silently changed.
- `qa/batches/` — batch ledgers.
- `qa/reports/` — post-batch and source-integrity reports.

## Tools

- `python tools/status.py` — summarize corpus progress.
- `python tools/next_batch.py --category letters --max-words 300 --count 10` — propose untranslated candidates.
- `python tools/check_source.py /path/to/tolstoy-russian-md-audited` — detect missing or hash-changed Russian source files.
- `python tools/validate_translation.py /path/to/tolstoy-russian-md-audited` — validate source linkage, hashes, page markers, footnote identities, and accepted-state consistency.
- `python tools/validate_coverage.py` — validate P002-and-later coverage records.

## Git checkpoints

The repository includes its local `.git` history. Git is being used as a stack of durable save points; GitHub is optional.

Useful inspection commands, if ever needed:

```bash
git status
git log --oneline --decorate -30
```

Every accepted P001/P002 unit has its own commit, followed by batch-review commits. A later session can therefore resume from the files and history without relying on the previous chat context.

## Editorial memory and source preflight

- `metadata/DECISIONS.md` records consequential translation/editorial choices so later audits do not silently undo settled policy.
- `tools/preflight_boundaries.py` flags suspicious beginnings/endings in small Russian source files before translation. It supports either an unpacked source repository (`--source-root`) or the source ZIP directly (`--source-zip`). Findings are warnings for review, not automatic declarations of corruption.
