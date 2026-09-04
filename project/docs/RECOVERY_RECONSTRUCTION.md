# Workspace-loss recovery reconstruction

Date: 2026-09-01

## What survived exactly

- `baseline.zip`: a clean Git repository whose last translation checkpoint is P004.30.
- `recovery.zip`: four P005.21–22 artifacts (two English Markdown files and two coverage records), plus its README and QA report. The four integrated files in this repository are copied verbatim from that recovery package.
- The baseline translation manifest, including pinned source paths/hashes for the full corpus and the exact P004 source identities.

## What did not survive

No later P004/P005 commits, reflog entries, or dangling Git objects were present in `baseline.zip`. No complete later P005 English repository was found among the available saved ZIPs. Prior project history records that a lost runtime eventually reached P005 50/50 and performed a 16-unit cold audit, but the accepted English files for P005.01–20 and P005.23–50 were not recoverable as artifacts.

## What this repair reconstructs

1. P004.31–50 are freshly reconstructed from the already-pinned P004 source identities and checked against the official 90-volume text. They are clearly labelled reconstruction work and are not represented as recovered original bytes.
2. The exact P005 50-unit selection is reproducible from the P004-complete manifest using the established category composition (8 works / 15 letters / 10 diaries / 3 notes / 9 Azbuka / 5 Circle of Reading). The resulting rough word total is 20,913, matching the recorded former P005 batch; units 21–22 are exactly the two source paths in `recovery.zip`.
3. P005.21 and P005.22 are integrated verbatim from the recovery package and marked reviewed. The package itself says P005.21 was reconstructed and P005.22 freshly prepared after the loss, so their provenance is “surviving recovery artifact,” not “byte-for-byte copy of the vanished pre-loss working tree.”
4. Restoration subsequently reached P005 50/50. P005.01–20 and P005.23–50 were freshly rebuilt from their pinned source identities; P005.21–22 remain the surviving recovery-package artifacts. Once the authoritative Russian ZIP mounted successfully, the exact source Markdown resolved special cases such as P005.03’s preserved graphic-notation figure references, and the reconstructed units were validated directly against that snapshot. These are documented recovery reconstructions, not claimed byte-for-byte recoveries of the vanished pre-loss English files.

## Validation boundary — closed for source identity

The authoritative audited Russian snapshot later mounted successfully in this recovery runtime. `project/tools/check_source.py` checked all **15,766** manifest sources with **0 missing and 0 changed**. After restoration reached P005.50, `project/tools/validate_translation.py` checked **182 English files with 0 errors** and only the two longstanding intentional-Cyrillic warnings elsewhere in the corpus. `project/tools/validate_coverage.py` checked **175 structured coverage records with 0 errors**.

The remaining distinction is methodological rather than structural: the former lost-runtime P005 cold audit cannot be inherited by newly reconstructed English files. A fresh periodic cold-fidelity sample should therefore be performed and recorded separately.

## Second ephemeral-workspace replay — P006.06–33

After P006.33 had been accepted in a later runtime, that runtime's working directory disappeared before a new full ZIP was produced. The last durable full repository ZIP was the P006.05 checkpoint. The accepted session record, however, retained the complete P006.06–33 translation text, coverage records, source-QA decisions, validator results, and unit-by-unit commit operations.

P006.06–33 were therefore replayed onto the durable P006.05 repository, one accepted unit at a time. The replayed Git hashes are intentionally new and must not be represented as recovery of the vanished temporary commit objects. The semantic/project state is reconstructed from the accepted records and then revalidated against the mounted audited Russian repository.

At the P006.33 replay boundary the manifest contains **215 reviewed translations** covering approximately **56,566 rough source-body words**, and `project/qa/coverage/` contains **208 structured coverage records**. The next translation target is P006.34 (`corpus/notes/v49_135_137_Zapisi_na_listah_1881.md`).

## Bounded recovery replay — P006.34–36

Date: 2026-09-03

At the user's request, recovery was deliberately stopped at **P006.36** before any work on P006.37. P006.34–36 were freshly reconstructed against the exact mounted audited Russian witness and committed individually. The source hash gate at this boundary is **15,766 checked, 0 missing, 0 changed**; the translation validator checks **218 English files with 0 errors** (plus the two longstanding intentional-Cyrillic warnings), and the coverage validator checks **211 structured records with 0 errors**.

P006.36 (`corpus/notes/v49_149_156_Zapisnaja_knizhka_1882.md`) exposes a confirmed source-conversion defect: the audited Markdown preserves footnote marker/definition `[^15]` but leaves its definition empty. Official volume 49, p. 155, textual note 136 supplies five deleted lines. The Russian repository remains immutable; only the verified deleted passage is restored in the English apparatus, explicitly labeled as deleted text. No other omitted printed apparatus was silently imported. The final source-to-target structural pass confirms all **19** body footnote references and definitions, all **8** page markers, and all source deletion delimiters.

The next translation target is P006.37 (`corpus/azbuka/v21_023_023_Dva_volka_vyshli.md`).


## Bounded continuation — P006.37–40

Date: 2026-09-03

At the user's request, exactly four additional units were completed after the P006.36 checkpoint: P006.37–40, all miniature exercises from *The New Primer*. Each was translated directly from the exact mounted audited Russian witness, received an exhaustive source-to-target coverage record, passed reverse target-to-source checking, and was committed separately. No work was begun on P006.41.

At this boundary the source hash gate remains **15,766 checked, 0 missing, 0 changed**; the translation validator checks **222 English files with 0 errors** (plus the two longstanding intentional-Cyrillic warnings), and the coverage validator checks **215 structured records with 0 errors**. The repaired manifest contains **222 reviewed translations**, approximately **58,204 rough source-body words**.

The next translation target is P006.41 (`corpus/azbuka/v21_023_023_Nastja_ela_grushu.md`).

## Bounded continuation — P006.41–45

At the user's request, exactly five additional reviewed units were completed after the P006.40 checkpoint. P006.41–43 were translated directly from the exact mounted audited Russian witness. During preflight, the accepted recovery record was reconciled with the stale batch list: `U_babki_byla_vnuchka` ends mid-sentence at the p. 23/24 boundary and `Na_lugu_byli_churki` ends at the p. 24/25 boundary. Official volume 21 confirms both continuations, so those individual Markdown witnesses are quarantined rather than counted as complete units.

The corrected P006 Primer sequence is therefore P006.41 `Nastja_ela_grushu`, P006.42 `Palo_mnogo_snegu`, P006.43 `Vbili_na_dvore_dva_shesta`, P006.44 `Petja_i_Masha_byli_gosti`, and P006.45 `Pomnju_ja_byla_mala`. P006.44–45 were restored byte-for-byte from the exact accepted recovery artifacts and their source hashes were revalidated. The batch selector now skips `source_qa_status == confirmed_erratum` rows by default.

At this boundary the source hash gate remains **15,766 checked, 0 missing, 0 changed**; the translation validator checks **227 English files with 0 errors** (plus the two longstanding intentional-Cyrillic warnings), and the coverage validator checks **220 structured records with 0 errors**. The repaired manifest contains **227 reviewed translations**, approximately **58,312 rough source-body words**.

The next translation target is P006.46 (`corpus/krug_chtenija/v41_033_035_Krug_chtenija_daily_jan_2_6.md`). No work on P006.46 has begun in this checkpoint.

