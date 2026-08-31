# Tolstoy English Markdown — Starter Scaffold

This scaffold was generated from the audited Russian corpus snapshot supplied on 2026-08-30. It contains **no bulk English translations yet**. Its purpose is to make translation resumable, source-linked, and auditable from the beginning.

Start with:

1. `CORPUS_ANALYSIS.md` — what is actually in the Russian repository.
2. `TRANSLATION.md` — translation and audit rules.
3. `WORKBENCH.md` — persistent handoff state.
4. `translation_manifest.jsonl` — one row for each of the 15,766 Tolstoy corpus documents.
5. `catalog.csv` — spreadsheet-friendly view of the manifest.

The 807 scholarly commentary files are deliberately outside the initial translation manifest. Their source identity remains in the original Russian repository and they can be added as a separate editorial phase.

## Tools

- `python tools/status.py` — corpus status summary.
- `python tools/next_batch.py --category letters --max-words 300 --count 10` — select resumable untranslated work.
- `python tools/check_source.py /path/to/tolstoy-russian-md-audited` — detect changed/missing Russian source files using SHA-256.
- `python tools/validate_translation.py /path/to/tolstoy-russian-md-audited` — validate source linkage and stable page markers for translated files that exist.

The relative English path is intentionally the same as the Russian path. English display titles belong in metadata, not in renamed filenames.
