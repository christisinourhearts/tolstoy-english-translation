# *The Death of Ivan Ilyich* — Flagship Edition

Work code: **IVI** · Governed by `project/docs/EDITIONS.md` and `project/docs/TRANSLATION.md`.

## Source record (verified 2026-10-06)

| Field | Value |
|---|---|
| Edition | Толстой Л. Н. Полное собрание сочинений в 90 тт. Т. 26. М.: ГИХЛ, 1936. С. 61–113 |
| Russian file | `corpus/works/v26_061_113_Smert_Ivana_Ilicha.md` |
| SHA-256 | `04ac37a0603e83997432c14a174f4d1282f58dbe610b17971fc5eb22845aef21` (matches the Russian repository's `SHA256SUMS.txt`) |
| Upstream | tolstoydigital/TEI, `texts/works/v26_061_113_Smert_Ivana_Ilicha.xml` (CC BY-SA) |
| Orthography | normalized reading (`reg`); е often printed for ё (see D0003) |
| Structure | 12 chapters (I–XII) |
| Variants | `corpus/works/v26_505_528_Smert_Ivana_Ilicha_Varianty.md` |
| Commentary | `editorial/comments/v26_679_691_Smert_Ivana_Ilicha.md` |

## English body

Target file: `translations/works/v26_061_113_The_Death_of_Ivan_Ilyich.md` (not yet created). The current website translation may be used as the first draft but must pass the full gauntlet (TRANSLATION.md §15) against the Russian file above.

## Status

| Chapter | Units | Status |
|---|---|---|
| I | — | not started |
| II | 1 recorded (chapter has 30 paragraphs) | pilot: IVI-02-001 complete |
| III–XII | — | not started |

## Plan

1. Pilot chapter II: segment into units, literal lines, translate/revise, audit, record. Review the process and adjust EDITIONS.md.
2. Chapters I, III–XII in order.
3. Assemble the English body file, run `validate_translation.py`, write the coverage record.
4. Cold audit at `other-model` or `human` level on all `difficult` units and a 10% sample.
