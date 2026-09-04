# Tolstoy in English

An ongoing, source-linked English translation of Leo Tolstoy's works, letters,
diaries, notebooks, educational writings, and *Circle of Reading* selections.

## Read the translations

- [Works](translations/works/)
- [Letters](translations/letters/)
- [Diaries](translations/diaries/)
- [Notes and notebooks](translations/notes/)
- [Primer](translations/primer/) — material from *Azbuka* and *The New Primer*
- [Circle of Reading](translations/circle_of_reading/) — Tolstoy's *Krug chteniya*

The repository currently contains **329 translated Markdown files**.
Each filename uses an English title while retaining the edition volume and page
prefix—for example, `v21_026_026_Nastya_Had_a_Doll.md`.

## Source identity

Every translation keeps its original Russian path and SHA-256 checksum in YAML
front matter. Renaming the English file therefore does not break its connection
to the audited Russian witness. The old and new English paths are recorded in
[`project/metadata/english_path_migration.csv`](project/metadata/english_path_migration.csv).
The main manifest retains its source-facing category keys and stable original
paths; the validation tools resolve those paths through the migration ledger.

## Project records

Translation policy, resumable status, manifests, validation tools, QA records,
and provenance material live under [`project/`](project/). Start with:

- [`project/docs/TRANSLATION.md`](project/docs/TRANSLATION.md)
- [`project/docs/WORKBENCH.md`](project/docs/WORKBENCH.md)
- [`project/translation_manifest.jsonl`](project/translation_manifest.jsonl)

The audited Russian source repository remains read-only. English translations
are tracked separately so editorial changes never silently alter the source.
