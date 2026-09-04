# Russian Corpus Analysis

Source inspected: `tolstoy-russian-md-audited`, release 2026-08-18.

## What is already solved

The Russian repository already contains a machine-readable manifest, per-file SHA-256 checksums, exact TEI source paths, 90-volume edition metadata, retained page markers, conversion tools, and a deep audit. The English project should reuse this identity system rather than inventing a second one.

The TEI/XML source remains the archival authority. The Russian Markdown repository is the audited translation/search access layer and the immediate source against which English translations should be checked.

## Tolstoy corpus in scope

| Category | Files |
|---|---:|
| Works | 767 |
| Letters | 9,087 |
| Diaries | 4,584 |
| Notes / notebooks | 100 |
| Azbuka | 784 |
| Krug chteniya | 444 |
| **Tolstoy corpus total** | **15,766** |

The Russian repository also contains **807 modern scholarly commentary files** under `editorial/comments/`. They are intentionally excluded from the first-pass Tolstoy translation manifest. They can later become a separate English editorial corpus.

A rough token-independent word scan finds about **10,604,496 words** across the six Tolstoy categories. This is only a planning figure; it is not a linguistic word-count standard.

## File size distribution

| Rough body words | Files |
|---|---:|
| 0000-0100 | 4,180 |
| 0101-0300 | 5,884 |
| 0301-1000 | 4,557 |
| 1001-3000 | 795 |
| 3001-10000 | 225 |
| 10001-30000 | 91 |
| 30001-100000 | 21 |
| 100001+ | 13 |

**14,621 files (92.7%) are 1,000 words or shorter.** This makes transaction-sized, resumable translation particularly practical.

## Important structural findings

- `works/` is not just a shelf of canonical finished books. It includes textual variants, plans, drafts, alternate redactions, fragments, prefaces, afterwords, and other authorial material from the 90-volume edition. These should not be deduplicated away.
- At least 193 work records explicitly mention a variant in their title/subtitle, and many others are drafts or plans. The manifest flags likely cases for scheduling, but those flags are heuristic rather than scholarly classification.
- Letters are extremely suitable for checkpointed work: 9,087 files with a rough median around 261 words in this scan.
- Diaries are even more granular: 4,584 files with a rough median around 71 words.
- Many letter files contain an `### Editorial notes` section. Many other categories contain footnotes. Therefore body translation and editorial-apparatus translation have separate status fields.
- The source set is not literally all Russian: there are several French or mixed-language works and one English-language source (`The hostelry`). These require explicit handling rather than automatic Russian-to-English translation.
- Page boundaries such as `<!-- vol. 23, p. 17 -->` are stable scholarly anchors and should be preserved exactly in English.

## English navigation and source identity

The reader-facing English tree uses translated category and filenames beneath
`translations/`. The volume/page prefix is retained for stable ordering and to
reduce collisions; for example:

```text
RU: corpus/azbuka/v21_026_026_Byla_u_Nasti_kukla.md
EN: translations/primer/v21_026_026_Nastya_Had_a_Doll.md
```

Source identity does not depend on the English filename. Each English file and
manifest row retains the Russian relative path, stable manifest ID, and Russian
SHA-256. If the Russian source later changes, `project/tools/check_source.py`
can still identify exactly which English translations need re-audit. Historical
English path changes are recorded in
`project/metadata/english_path_migration.csv`.

## Recommended translation order

1. Pilot on representative material before scaling.
2. Finished/canonical works and high-value short works.
3. Azbuka and Krug chteniya.
4. Letters in chronological or correspondent batches.
5. Diaries and notebooks.
6. Variants, drafts, plans and alternate redactions.
7. Scholarly `editorial/comments/`, if a truly complete English equivalent is desired.

This ordering is editorial convenience only. Source identity remains one-to-one throughout.
