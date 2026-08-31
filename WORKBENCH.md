# Workbench

This is the persistent handoff ledger. A fresh session should read, in this order:

1. `HANDOFF_NEW_CHAT.md`
2. `TRANSLATION.md`
3. `metadata/DECISIONS.md`
4. `WORKBENCH.md`
5. `qa/batches/P003.md`
6. `translation_manifest.jsonl`

## Source snapshot

Russian source release: 2026-08-18  
Source repository: `tolstoy-russian-md-audited`

The authoritative Russian repository must remain read-only. The exact Russian ZIP was not available to the final runtime of the previous chat because of a file-mount failure. Therefore the first task in a new runtime is to verify that the newly uploaded Russian ZIP is actually accessible and run the source/hash and P003 boundary preflight against that exact snapshot.

## Completed work

### P001

- 7 / 7 units accepted.
- Full translate → fidelity audit → English edit → final source audit workflow completed.
- Post-pilot review in `qa/reports/P001_REVIEW.md`.

### Russian source stress test

- Stratified source-integrity sampling completed across 31 volumes.
- No evidence of systemic corruption found.
- Report: `qa/reports/SOURCE_STRESS_TEST.md`.
- Two later *New Azbuka* segmentation truncations were independently confirmed and recorded in `metadata/source_errata.yml`.

### P002

- 25 / 25 units accepted.
- 25 / 25 structured bilingual coverage records passed.
- 10-unit cold fidelity audit completed (40% of P002; ~1,766 source words).
- Cold audit found 0 substantive omissions, 0 unsupported substantive additions, 0 reversed meanings, and 0 speaker/reference errors.
- Four style-only smoothings from the cold audit were subsequently reverted under Decision D0001 in favor of more conservative fidelity.
- Reports: `qa/reports/P002_REVIEW.md` and `qa/reports/P002_COLD_AUDIT.md`.

### Translation policy hardening

- Decision D0001 adopted: conservative fidelity before stylistic smoothing.
- Preserve unusual but intelligible concrete Tolstoy phrasing rather than replacing it with smoother abstractions.
- Example settled decision: keep “the whole world of people” rather than “all humanity.”
- Permanent decisions ledger: `metadata/DECISIONS.md`.
- `SOURCE_SUSPECTED` protocol added.
- Automatic source-boundary suspicion detector added as `tools/preflight_boundaries.py`.

## Current corpus state

- Reviewed English translations: **40**.
- P001: 7 complete.
- P002: 25 complete.
- P003: **8 / 50 complete and individually Git-committed**.
- Approximate reviewed source-body words: **8,479**.
- Confirmed source errata: **2**.
- Existing structured coverage records: **33**, currently validating with 0 errors (P001 used the older unstructured audit format).

`python tools/status.py` should reproduce the manifest counts.

## P003 status

Batch file: `qa/batches/P003.md`.

Completed and accepted:

1. `corpus/works/v90_122_122_Obschestvo_nezavisimyh.md`
2. `corpus/works/v34_143_143_Predislovie_k_The_Anatomy_of_Misery_Dzhona_Kenvorti.md`
3. `corpus/works/v26_457_458_Pechatnye_varianty_pervogo_izdanija_stati_Pora_opomnitsja_k_osnovnomu_tekstu.md`
4. `corpus/works/v34_343_344_Konspekt_Vospominanij.md`
5. `corpus/works/v90_093_094_Detskie_zabavy.md`
6. `corpus/works/v29_363_363_Kto_prav_Varianty.md`
7. `corpus/works/v37_005_005_Volk.md`
8. `corpus/works/v40_435_435_Zhizn_i_izrechenija_Krishny_Predislovie.md`

Last completed unit: **P003.08 — Preface to the Book “Life and Sayings of Krishna.”**

Next planned unit: **P003.09 — `corpus/letters/v60_095_N_A_Nekrasovu.md`**.

## Important source-verification caveat for P003.01–08

During the previous chat, the exact Russian ZIP failed to mount in the runtime immediately before P003 production. The eight P003 translations were checked against authoritative 90-volume source text, but the new runtime should still run the exact repository hash/source check against the uploaded Russian ZIP before continuing. If the P003.01–08 source hashes match `metadata/source_manifest.jsonl` / `translation_manifest.jsonl`, no reopening is necessary. If any differ, reopen only the affected units.

## NEXT ACTION

1. Confirm both the English handoff ZIP and Russian source ZIP are physically accessible in the new runtime.
2. Run `tools/check_source.py` against the exact Russian repository snapshot.
3. Run `tools/preflight_boundaries.py` for the selected P003 paths.
4. Inspect any MEDIUM/HIGH boundary flags rather than automatically rejecting them.
5. Confirm source hashes for P003.01–08.
6. If clean, resume at **P003.09** and continue the existing finite workflow:
   translate → fidelity audit → conservative English edit → exhaustive bilingual coverage → mechanical validation → update manifest/workbench → Git commit.
7. After P003.50, stop and perform a deliberately difficult cold-audit sample before selecting P004.

Do not begin a new batch or retranslate completed units merely for stylistic variety. `metadata/DECISIONS.md` governs settled editorial choices.
