# P004 recovery reconstruction audit

Date: 2026-09-01

## Scope

The original packaged Git repository ended at P004.30. This audit covers the freshly reconstructed P004.31–50 bridge. It does not pretend those English files are byte-identical to the vanished earlier runtime.

The reconstruction retained the already-pinned manifest source paths and SHA-256 controls. The textual reconstruction was checked against the official Tolstoy 90-volume electronic witness, with particular attention to the clipped 1850 diary schedules, textual-note apparatus, fragmentary notebooks, tiny Primer units, and the January *Circle of Reading* selections.

## Difficult sample reviewed

- P004.31 — 18 June 1850 diary: historical `наряд` kept in the work-assignment sense; textual note retained.
- P004.32 — 19 June 1850 diary: schedule structure and all six textual notes retained; `юмор` read in the older *humeur* / mood sense.
- P004.33 — 11 December 1850 diary: the source's odd backward-looking “Tasks for 8 December” sequence is preserved in source order rather than silently reorganized.
- P004.35 — notebook fragment: biblical/Talmudic shorthand remains fragmentary rather than being completed from external scripture.
- P004.36 — notebook fragment: plant-name reading rendered “Turkish rocket”; terse agricultural notes kept terse.
- P004.42 — Primer fragment crossing pp. 16–17: page boundary and the very small source unit are preserved without importing neighboring primer sentences.
- P004.47–50 — *Circle of Reading*: page boundaries, numbered extracts, attributions, repetitions, and Tolstoy's compiled Russian wording are represented without replacing passages by modern external translations.

## Mechanical results

- Structured coverage validator after P004 reconstruction: 125 records checked, 0 errors.
- Reviewed-file structural pass: 132 reviewed files checked, 0 metadata/path/hash/page-marker/footnote-balance errors.

## Runtime limitation

The audited Russian ZIP was visible in the user's Library but its raw bytes could not be materialized into this execution container (the file service returned HTTP 403). Therefore `tools/validate_translation.py <mounted-russian-repo>` and a fresh all-source SHA-256 check cannot honestly be reported for this recovery runtime. The source identities used here are the exact paths/hashes already pinned in the baseline manifest, whose P004 preflight records that all 50 P004 sources had matched the audited snapshot before the loss.

Result: **PASS AS A DOCUMENTED RECONSTRUCTION**, with full source-byte revalidation deferred until the audited Russian snapshot is mountable again.


## Deferred source-byte validation — subsequently completed

On 2026-09-01 the authoritative audited Russian ZIP mounted successfully. The deferred gate is therefore closed: `tools/check_source.py` checked all **15,766** manifest sources with **0 missing and 0 changed**, and the full English/source validator passed after the later P005 restoration. This does not turn P004.31–50 into recovered historical bytes; it confirms that their pinned source identities and current English/source structures are validated against the exact audited snapshot.
