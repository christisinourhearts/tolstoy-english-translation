# Public-domain core provenance pilot

## Purpose

This directory tests whether the existing English translation work can be detached from the Tolstoy Digital CC BY-SA source chain without discarding the translations.

The pilot is deliberately isolated from `corpus/` and `translation_manifest.jsonl`. It does **not** change the 61 accepted translations or their recorded source hashes.

## Pilot unit

- Tolstoy: notes numbered 2 and 3, 1870
- 90-volume edition: volume 48 (1952), printed pp. 342–346
- scan PDF pages: 372–376
- existing Russian witness: `corpus/notes/v48_342_346_Zapisi_No_2_i_3_1870.md`
- existing Russian witness SHA-256: `8849c8a0052527371a65546811f55371febca50bc494bce2bf17e298ffb3331f`
- existing reviewed English SHA-256: `03926dcbc45bb7695597383c28dd3eb7c96502ea5dc9faf80ff5e3d171c70ae6`

Scan:

`https://upload.wikimedia.org/wikipedia/commons/8/86/L._N._Tolstoy._All_in_90_volumes._Volume_48.pdf`

Wikimedia Commons describes this scan as public domain, citing the edition's reproduction declaration and, where that is not legally possible, an unrestricted permission to use the work for any purpose.

## Method

1. Inspect the actual page images for printed pp. 342–346.
2. Build a new Russian pilot transcription from the visible printed copy rather than inheriting the TEI license field or TEI metadata scheme.
3. Preserve visible bracket completions instead of silently normalizing them.
4. Preserve Tolstoy-authored deleted/marginal manuscript readings when the printed apparatus exposes them, but restate the apparatus labels in project-neutral factual language rather than copying Soviet editorial prose.
5. Use the old Russian Markdown only as a comparison witness to detect discrepancies.
6. Rebase a copy of the already-reviewed English translation onto the pilot Russian source and compare its substantive wording to the accepted English file.

This is a provenance experiment, not a claim that every manuscript transcription in the 90-volume edition is free of all editorial authorship. Hard manuscript readings may eventually require manuscript-image verification or a separate policy.

## Result

The current Russian Markdown is very close to the printed pages, but its `orthography_mode: reg` layer silently removes several distinctions visible in the edition. In this five-page sample it normalizes at least these printed bracket completions:

- `Андр[ей]` → `Андрей`
- `на[до]` → `надо`
- `кот[орого]` → `которого`
- `пролетар[иата]` → `пролетариата`

It also normalizes the deleted reading `ули[цу]` to `улицу` in the apparatus.

Those changes are linguistically obvious, but they demonstrate that the present Russian corpus is not a purely diplomatic transcription of the public-domain scan. It contains inherited editorial normalization.

The important positive result is that the **English translation itself did not need substantive rewriting**. After removing YAML, page comments, footnote markers, and apparatus labels, the accepted English body and the rebased pilot English body normalize to exactly the same wording.

## Files

- `russian/...md` — scan-led Russian PD-core candidate.
- `english/...md` — provenance-rebased copy of the accepted English translation.
- `AUDIT.md` — page-by-page findings and migration implications.
- `evidence.json` — machine-readable hashes, page mapping, and observed normalization cases.

## Interim conclusion

A corpus-wide migration looks technically feasible without throwing away the English work. The likely operation is:

1. build a scan-authoritative Russian core;
2. treat Tolstoy Digital as a comparison witness only;
3. strip or independently restate later editorial prose;
4. preserve editorially supplied/bracketed readings explicitly instead of silently normalizing them;
5. re-audit each accepted English file against the new Russian authority;
6. change the English source-link metadata only after that audit passes.

No corpus-wide license change should be made by simply deleting `CC BY-SA` from the existing files.
