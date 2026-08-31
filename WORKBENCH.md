# Workbench

This is the persistent handoff ledger. A new session should read `TRANSLATION.md`, this file, and `translation_manifest.jsonl` before doing corpus work.

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

## Current state

Pilot batch P001 is active. Source-integrity preflight passed: 15,766 records checked, 0 missing, 0 changed.

## Last completed unit

P001.1 — `corpus/works/v25_028_030_Dva_brata_i_zoloto.md`

Stages: translation complete; fidelity audit PASS; English edit complete; final source audit PASS; mechanical validation PASS.

Upstream QA note: possible Russian source-layer discrepancy `в горè` / `на горе` recorded in `qa/batches/P001.md`.

## Active batch

P001 — see `qa/batches/P001.md`.

## Current unit

`corpus/works/v01_097_099_Detstvo_Varianty_teksta_Sovremennika_1852_g_No_9.md`

Stage: not started.

## Next action

Translate the *Childhood* Sovremennik variant apparatus exactly as represented, preserving its editorial nature, foreign-language epigraphs, footnotes, page markers, and distinctions among the 1852, 1856, and manuscript readings. Then audit, validate, update the manifest/report/workbench, and commit before advancing.
