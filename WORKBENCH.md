# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, `qa/batches/P001.md`, `qa/reports/P001_REVIEW.md`, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

P001 and P002 are complete. P002 has now also received a 10-unit cold fidelity sample covering 40% of the batch and about 1,766 rough source-body words.

- Reviewed English translations: 32.
- P002 accepted units: 25 / 25.
- P002 structured bilingual coverage records: 25 / 25 PASS.
- P002 cold-audit sample: 10 / 10 PASS.
- Cold-audit hard fidelity defects: 0.
- Cold-audit minor local revisions: 5 edits across 4 files (1 precision correction, 4 contemporary-English clarity edits).
- Mechanical validation after cold-audit revisions: 32 English files checked, 0 errors, 2 intentional Cyrillic warnings.
- Source-integrity postflight after cold audit: 15,766 records checked, 0 missing, 0 changed by hash; source files remain unmodified.
- Confirmed source errata: 2, both *New Azbuka* files truncated at page boundaries and quarantined before translation.
- Approximate reviewed source-body words: 6,752.

See `qa/reports/P002_COLD_AUDIT.md` in addition to the earlier P001/P002 reports.

## Last completed unit

P002.25 — `corpus/krug_chtenija/v41_016_017_Krug_chtenija_daily_jan_1_4.md` accepted.

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; structured coverage PASS; mechanical validation PASS.

## Batch status

P002 is closed. No P003 files have been started.

## NEXT ACTION

Add the planned automatic boundary-suspicion preflight for small source files, then select P003 at approximately 50 short units / 7,000–10,000 source words. Keep a post-P003 cold-audit sample as a quality gate.
