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
4. The remaining P005 units stay untranslated in the manifest until they are rebuilt from source.

## Validation boundary

Coverage and English-structure validators pass in this repaired repository. A fresh validator requiring raw Russian source bytes cannot run in this container because the saved audited Russian ZIP could not be materialized. On the next runtime with a mounted Russian snapshot, run the repository-wide source/hash and translation validators before proceeding.
