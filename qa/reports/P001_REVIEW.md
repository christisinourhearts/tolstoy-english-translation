# P001 Post-Pilot Review

Pilot batch: P001  
Units completed: 7 / 7  
Fidelity audits passed: 7 / 7  
Mechanical validation: 7 files checked, 0 errors  
Source-integrity check: 15,766 records checked, 0 missing, 0 changed

## Verdict

The basic architecture works. The Russian repository can serve as the immutable source layer; the English repository can mirror its paths; the source hashes make drift detectable; and one-file checkpoints give reliable persistence. P001 is **not** evidence that the remaining corpus should now be translated unattended in one long run. It is evidence that a controlled P002 can begin after the findings below are reviewed and the schema/policies are tightened.

## 1. What failed or nearly failed?

### Source-layer anomaly

`Two Brothers and Gold` exposed a probable source-layer reading problem in the audited Markdown (`в горè` in a context for which another Russian witness reads `на горе`). The translation workflow needs a formal way to flag a suspected source defect without changing the authoritative Russian repository and without hiding the issue inside an English choice.

### Editorial apparatus masquerading as a work

The `Childhood` *Sovremennik* variants file lives under `corpus/works`, but its content is primarily scholarly editorial apparatus quoting tiny pieces of Tolstoy. A binary “body versus apparatus” model is too simple for this class.

### Declared language versus actual body language

The 1848 letter is declared `language: ru`, while Tolstoy's letter body is French and the Russian appears in the editors' notes. A single source-language field is insufficient.

### Fragmentary material is vulnerable to hallucinated coherence

The 1870 notebook contained `Сапела`, initially misread as a proper name and corrected during the fidelity audit to “She panted.” This is precisely the sort of error that a smooth initial translation can conceal. Rough notebooks need especially conservative handling and explicit unresolved states.

### Compiled quotations can be falsely “restored”

The 1 January `Krug chteniya` entry contains quotations attributed to Emerson, Locke, Seneca, Thoreau, and Schopenhauer. The volume commentary confirms that Tolstoy sometimes translated, adapted, or shortened material for the compilation. Substituting a familiar English or German original would therefore risk erasing Tolstoy's editorial/translation intervention.

### Mechanical validation does not prove semantic correctness

The validator successfully detects structural/source-link problems, but it cannot detect a mistranslation such as the initial `Сапела` error. The fidelity audit remains indispensable.

## 2. Which provisions of `TRANSLATION.md` proved ambiguous or insufficient?

The constitution is sound at the general level, but the pilot suggests adding explicit category policies rather than making the main file much longer.

Recommended policy files:

- `policies/LETTERS.md` — actual body language, multilingual letters, salutations, postscripts, editorial translations, correspondents.
- `policies/VARIANTS_AND_APPARATUS.md` — editorial-only files, micro-variants, manuscript states, empty editorial notes, witness-specific spelling.
- `policies/DIARIES_AND_NOTES.md` — fragments, abbreviations, uncertain syntax, deleted material, code-switching, unresolved tokens.
- `policies/KRUG_CHTENIYA.md` — compiler/author roles, attributed quotations, adaptation, provenance, and the rule against silently restoring external originals.
- `policies/NAMES_AND_TRANSLITERATION.md` — recurring Russian names, places, historical offices, and when commentary may justify a conventional form.

The constitution should also state explicitly that scholarly commentary may be consulted to identify a name, place, quotation, or textual state, but such information must not be smuggled into Tolstoy's body text as though he wrote it.

## 3. Did the metadata model adequately represent the real source files?

Partly. The source path/hash/volume/page model worked very well. The translation-state fields also worked. The following additions are recommended:

- `content_role`: e.g. `tolstoy_body`, `editorial_apparatus`, `mixed_body_apparatus`, `compilation`.
- `declared_source_language`.
- `body_source_languages`: list, because a body may genuinely switch languages.
- `apparatus_source_languages`: list.
- `translation_scope`: what was translated in the current milestone.
- `source_qa_flags`: suspected transcription/conversion/source anomalies that do not alter the Russian source.
- `needs_specialist_review`: optional unresolved issue that does not necessarily block acceptance.
- `compiler_or_editor`: useful for `Krug chteniya` and similar compilations.
- optional `quotation_provenance`: bibliographic/provenance information kept separate from the translated reading text.

These should be added before large-scale automation, but not retrofitted casually in the middle of P001.

## 4. Did separation of Tolstoy text and editorial apparatus work?

Yes for ordinary mixed files, especially the French letter: Tolstoy's body and the Soviet editors' Russian notes remained visibly distinct and can have separate statuses.

It was inadequate for the `Childhood` variants file because the file itself is fundamentally an editorial apparatus document containing Tolstoy quotations. A richer `content_role` or document-type field is needed.

## 5. Did translation choices reveal a need for corpus-wide terminology or name policies?

Yes, although P001 was too small to establish a philosophical glossary with confidence.

Immediate needs are:

- consistent transliteration and conventional English forms for people and places;
- a policy for historical Russian ranks/titles (`stolnik`, `tsaritsa`, `tsarevna`, etc.);
- a distinction between translating a source phrase and identifying its historical referent;
- a record of recurrent philosophical/religious terms only when enough examples have accumulated to justify a corpus-wide preference.

The existing `TERMINOLOGY.md` and `NAMES.md` are the right places to accumulate decisions. They should remain evidence-driven rather than becoming a rigid word-substitution dictionary.

## 6. Were the existing validators sufficient?

They were sufficient for the pilot's basic structural checks, but not for production scale.

Recommended additions:

1. Verify that every manifest row marked `reviewed` has an English file.
2. Verify that English YAML source path/hash/title metadata agrees with the manifest.
3. Compare source and English page-marker sequences exactly.
4. Compare source and English footnote identifiers/references.
5. Flag unexplained Cyrillic remaining in English body text while allowing intentional Russian quotations/names.
6. Heuristically compare headings, block quotes, tables, deletion markers, and major structural blocks.
7. Detect duplicate output paths and duplicate stable IDs.
8. Validate state transitions in the manifest (for example, `reviewed` should not coexist with an unstarted final audit).
9. Produce a source-QA report for suspected upstream anomalies without editing the Russian repository.

No mechanical validator should be treated as a replacement for source-to-English fidelity review.

## 7. What should change before scaling?

Before P002:

- review these seven translations manually;
- add the metadata fields above;
- add the category policy files, especially for letters, variants/apparatus, diaries/notes, and `Krug chteniya`;
- strengthen validation;
- give unresolved textual problems a formal non-destructive status;
- preserve the rule that every accepted unit is saved, manifested, and committed before the next unit begins.

Do **not** change the Russian repository merely to make English automation easier.

## 8. What batch size appears safe for routine work?

For heterogeneous material like P001, 5–10 units is a sensible review batch.

After schema/tooling improvements, P002 could reasonably contain about 20–25 short, deliberately selected files while retaining one commit/checkpoint per accepted unit. Once that succeeds, batches of roughly 50 very short letters or diary entries are plausible. Long works should be internally processed in chapter/section checkpoints even if the repository ultimately keeps one English file corresponding to one Russian file.

The important safety unit is the accepted file/checkpoint, not the number printed on the batch.

## 9. Which categories require specialized instructions?

Highest priority:

- letters;
- textual variants/editorial apparatus;
- diaries and notebooks;
- `Krug chteniya`;
- long works with internal chapter/section structure.

`Azbuka` also benefits from a short register rule: simple source prose must remain simple and should not be “improved” into more literary English.

## 10. Is the system ready to scale?

**Ready for a controlled P002 after human review and the schema/tooling revisions above.**

**Not yet ready for unattended corpus-scale translation.**

The most important result of P001 is positive: persistence works. Each accepted unit exists as an ordinary English Markdown file tied to an exact Russian hash and preserved in Git. A lost chat or exhausted model context no longer destroys completed work.

## P001 checkpoint history

- `e3602d2` — Two Brothers and Gold
- `06aba17` — Childhood *Sovremennik* variants
- `f4204ff` — 1848 letter to Yergolskaya and Tolstaya
- `4daef23` — April 1861 diary entry
- `4d90d38` — 1870 notebook notes
- `33240ca` — Fire Dogs
- `e381241` — Circle of Reading, 1 January

The final handoff commit follows these seven unit commits.
