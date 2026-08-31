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
- Cold-audit lasting local revision: 1 precision correction. Four style-only smoothings were later reverted under Decision D0001 in favor of conservative fidelity.
- Mechanical validation after cold-audit revisions: 32 English files checked, 0 errors, 2 intentional Cyrillic warnings.
- Source-integrity postflight after cold audit: 15,766 records checked, 0 missing, 0 changed by hash; source files remain unmodified.
- Confirmed source errata: 2, both *New Azbuka* files truncated at page boundaries and quarantined before translation.
- Approximate reviewed source-body words: 6,752.

See `qa/reports/P002_COLD_AUDIT.md` in addition to the earlier P001/P002 reports.

## Last completed unit

P002.25 — `corpus/krug_chtenija/v41_016_017_Krug_chtenija_daily_jan_1_4.md` accepted.

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; structured coverage PASS; mechanical validation PASS.

## Batch status

P002 is closed. P003 has been selected (50 units, ~8,136 rough source-body words) but no P003 translation has been started. The full source-boundary preflight remains the gate before the first P003 unit.

## NEXT ACTION

Run `tools/preflight_boundaries.py` against the authoritative Russian source tree/ZIP for the selected P003 paths. Resolve/replace any MEDIUM/HIGH boundary flags. Then begin P003 unit 1 from `qa/batches/P003.md`. Keep a post-P003 cold-audit sample as a quality gate.

## P003 production status

P003 is in production. Completed and accepted: **2/50**.

Last completed unit: `P003.02` — `corpus/works/v34_143_143_Predislovie_k_The_Anatomy_of_Misery_Dzhona_Kenvorti.md`.

NEXT ACTION: translate and audit `P003.03`.
