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

The authoritative audited Russian snapshot later mounted successfully in this recovery runtime. `tools/check_source.py` checked all **15,766** manifest sources with **0 missing and 0 changed**. After restoration reached P005.50, `tools/validate_translation.py` checked **182 English files with 0 errors** and only the two longstanding intentional-Cyrillic warnings elsewhere in the corpus. `tools/validate_coverage.py` checked **175 structured coverage records with 0 errors**.

The remaining distinction is methodological rather than structural: the former lost-runtime P005 cold audit cannot be inherited by newly reconstructed English files. A fresh periodic cold-fidelity sample should therefore be performed and recorded separately.

## Second ephemeral-workspace replay — P006.06–33

After P006.33 had been accepted in a later runtime, that runtime's working directory disappeared before a new full ZIP was produced. The last durable full repository ZIP was the P006.05 checkpoint. The accepted session record, however, retained the complete P006.06–33 translation text, coverage records, source-QA decisions, validator results, and unit-by-unit commit operations.

P006.06–33 were therefore replayed onto the durable P006.05 repository, one accepted unit at a time. The replayed Git hashes are intentionally new and must not be represented as recovery of the vanished temporary commit objects. The semantic/project state is reconstructed from the accepted records and then revalidated against the mounted audited Russian repository.

At the P006.33 replay boundary the manifest contains **215 reviewed translations** covering approximately **56,566 rough source-body words**, and `qa/coverage/` contains **208 structured coverage records**. The next translation target is P006.34 (`corpus/notes/v49_135_137_Zapisi_na_listah_1881.md`).
