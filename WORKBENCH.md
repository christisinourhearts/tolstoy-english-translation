# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, `qa/batches/P001.md`, `qa/reports/P001_REVIEW.md`, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

P001 and P002 are complete. The post-P001 Russian source stress test remains in force, now supplemented by two confirmed small-file segmentation errata found during P002.

- Reviewed English translations: 32.
- P002 accepted units: 25 / 25.
- P002 structured bilingual coverage records: 25 / 25 PASS.
- Mechanical validation after P002: 32 English files checked, 0 errors.
- Source-integrity postflight: 15,766 records checked, 0 missing, 0 changed by hash.
- Confirmed source errata: 2, both *New Azbuka* files truncated at page boundaries and quarantined before translation.
- Approximate reviewed source-body words: 6,752.

See `qa/reports/P001_REVIEW.md`, `qa/reports/SOURCE_STRESS_TEST.md`, and `qa/reports/P002_REVIEW.md`.

## Last completed unit

P002.25 — `corpus/krug_chtenija/v41_016_017_Krug_chtenija_daily_jan_1_4.md` accepted.

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; structured coverage PASS; mechanical validation PASS.

## Batch status

P002 is closed. No P003 files have been started.

## NEXT ACTION

Review `qa/reports/P002_REVIEW.md`. Before P003, optionally run a cold/fresh-context fidelity sample and add a preflight detector for suspicious source-file boundaries. Then select a P003 batch of approximately 50 short units / 7,000–10,000 source words.
