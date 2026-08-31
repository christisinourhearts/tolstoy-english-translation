# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, `qa/batches/P001.md`, `qa/reports/P001_REVIEW.md`, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

Pilot batch P001 is complete. A post-P001 Russian source-integrity stress test is also complete.

- Units: 7 / 7 accepted.
- Fidelity audits: 7 / 7 PASS.
- Mechanical validation: 7 English files checked, 0 errors.
- Source-integrity postflight: 15,766 records checked, 0 missing, 0 changed.
- English corpus status after P001: 7 reviewed translations; 1 source-already-English record; 15,758 untranslated records.
- Source stress test: 31 volumes sampled across the 90-volume edition; 0 substantive mismatches; 0 confirmed source errata.
- Source-integrity disposition: PASS, with a `SOURCE_SUSPECTED` verification protocol recommended before scaling.

See `qa/reports/P001_REVIEW.md` for pilot findings and `qa/reports/SOURCE_STRESS_TEST.md` for the Russian-source stress test.

## Last completed unit

P001.7 — `corpus/krug_chtenija/v41_011_013_Krug_chtenija_daily_jan_1_1.md`

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; mechanical validation PASS.

## Active batch

P002 — in progress. Target: 25 accepted short units.

P002 introduced structured bilingual coverage records and the formal `SOURCE_SUSPECTED` gate. During candidate selection, two truncated *New Azbuka* source files were confirmed against volume 21 and excluded from translation; see `metadata/source_errata.yml` and `qa/source_suspected/`.

## Current unit

P002.01 — `corpus/works/v01_246_246_Dlja_chego_pishut_ljudi.md` accepted.

## NEXT ACTION

Translate and audit P002.02 — `corpus/works/v07_120_120_O_haraktere_myshlenija_v_molodosti_i_v_starosti.md`.
