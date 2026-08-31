# Translation Constitution

This file governs all English translation work in this repository. Agents and human editors should read it before editing corpus files.

## 1. Purpose

Create a complete, auditable English counterpart to the Tolstoy Russian Markdown corpus while preserving a permanent one-to-one relationship with the audited source files.

The aim is clear contemporary English faithful to Tolstoy's wording, thought, tone, structure, and degree of plainness. The aim is not to imitate Victorian English, improve Tolstoy's prose, or make him sound more literary than the source.

## 2. Source hierarchy

1. Tolstoy Digital TEI/XML is the archival source.
2. `tolstoy-russian-md-audited` is the audited Markdown access layer used for translation and comparison.
3. The English Markdown is a derivative tied to one exact Russian Markdown source by relative path and SHA-256.

Never silently translate from an unrelated web edition when the audited source is available.

## 3. Identity and file structure

Keep the same relative path and filename as the Russian source whenever possible.

Example:

```text
corpus/works/v01_003_095_Detstvo.md
```

English titles belong in YAML/front matter and catalogs. Stable filenames are identifiers, not display titles.

Preserve source page markers exactly:

```md
<!-- vol. 1, p. 3 -->
```

Preserve heading hierarchy, block quotes, verse lineation, tables, deletion/addition markup where meaningful, and footnote identifiers. Do not renumber footnotes merely for convenience.

## 4. Core fidelity rules

- Translate every substantive part of the selected source scope. Do not omit material because it is repetitive, awkward, embarrassing, obscure, or apparently unimportant.
- Do not add explanations to the body that Tolstoy did not write.
- Do not intensify emotion, moral judgment, imagery, or rhetoric.
- Do not smooth away meaningful repetition.
- Do not silently resolve genuine ambiguity in the Russian.
- Preserve distinctions between certainty, probability, hearsay, irony, quotation, and conjecture.
- Verify all names, numbers, dates, measurements, biblical references, and quoted material.
- Preserve changes of tense, person, and point of view when they are meaningful rather than automatically regularizing them.
- When the Russian is deliberately rough, fragmentary, telegraphic, or unfinished, English may also be rough, fragmentary, telegraphic, or unfinished.

## 5. English style

- Use normal contemporary English syntax when Russian syntax carries no special force.
- Prefer ordinary English words when Tolstoy uses ordinary Russian words.
- Avoid decorative synonyms introduced only to prevent repetition.
- Avoid needless archaism: `whilst`, `thereupon`, `wherefore`, etc. require a textual reason.
- Do not simplify the thought merely because a sentence is intellectually difficult.
- Long sentences may remain long when their logical structure remains intelligible in English.
- Dialogue should sound like speech appropriate to the character and period without becoming theatrical pseudo-nineteenth-century English.
- Contractions may be used when natural to the register; they are not automatically modernizing or colloquializing.

## 6. Tolstoy's recurrent vocabulary

Do not translate recurrent philosophical or religious terms mechanically, but notice them deliberately. Maintain a terminology record in `metadata/TERMINOLOGY.md` when a choice has corpus-wide consequences.

Particular attention should be paid to terms such as:

- насилие
- зло
- добро
- совесть
- разум
- вера
- дух
- душа
- жизнь
- любовь
- закон
- власть
- истина / правда

A change in English rendering is allowed when context requires it. The reason should be recoverable when the distinction is significant.

## 7. Names and forms of address

Use established English forms for widely conventional historical names where appropriate. Otherwise use a consistent transliteration policy. Do not flatten meaningful distinctions among first name, patronymic, surname, title, nickname, diminutive, and respectful address.

Record recurring person-name decisions in `metadata/NAMES.md` rather than solving them independently in every file.

## 8. Foreign-language source passages

The source corpus contains some French, mixed-language, and English material.

- Detect the actual source language before translating.
- Do not pretend a French passage was translated from Russian.
- For source text already in English, preserve it unless there is a documented reason to normalize obvious archival transcription conventions.
- When Tolstoy deliberately switches languages inside a work, preserve the fact of the switch in metadata or a note even if the reading edition renders the passage in English.

## 9. Footnotes and editorial apparatus

The corpus contains both Tolstoy text and editorial apparatus. Many letters include an `### Editorial notes` section, and many files contain footnotes.

Track these separately:

- `translation_status`: Tolstoy/main body
- `apparatus_translation_status`: footnotes/editorial apparatus

For a body-only milestone, editorial apparatus may remain untranslated, but footnote markers and structure must not be destroyed. A file is not `final_complete` until all material designated for the complete English corpus has been handled.

Never silently convert an editor's statement into Tolstoy's voice.

## 10. Variants, drafts and unfinished material

Variants and drafts are not duplicates to discard. The 90-volume corpus intentionally preserves them.

Translate their actual textual state. Do not reconstruct a hypothetical finished version. Preserve deletions, fragmentary passages, alternative formulations, and uncertainty where represented by the source.

## 11. Gauntlet workflow

Each translation unit passes through finite stages. The creator of a translation should not be its only critic.

1. **Translate** — produce a complete English rendering from the audited source.
2. **Fidelity audit** — compare Russian/source text against English and identify concrete omissions, additions, misread syntax, incorrect referents, tone shifts, factual errors, or structural loss.
3. **Revision** — correct substantiated fidelity issues.
4. **English edit** — read the English as English; remove calques, stiffness, and accidental obscurity without taking new liberties.
5. **Final source audit** — compare the finished English against the source again after stylistic editing.
6. **Mechanical validation** — verify file identity, page markers, footnote IDs, Markdown structure, and source hash.
7. **Checkpoint/commit** — update the manifest and workbench before beginning the next unit.

Critics must cite a specific source passage and a specific problem. “Could be better” is not a defect report.

Do not loop indefinitely. A unit passes when no substantive fidelity defects remain, the English is intelligible and natural at the source's register, and mechanical validation passes.

## 12. Batch sizing and persistence

Assume the active AI context can disappear at any time.

- Never hold unique progress only in chat context.
- Save completed translation text before beginning criticism.
- Update `WORKBENCH.md` and `translation_manifest.jsonl` after every accepted unit or small batch.
- Commit frequently.
- For long works, process chapter/section chunks internally, but keep the final repository's one-to-one file identity unless there is a compelling technical reason otherwise.
- A resumed session should be able to determine the next action from the repository alone.

## 13. Acceptance checklist

A completed unit should satisfy all applicable items:

- [ ] Correct Russian/source file and SHA-256 recorded.
- [ ] Every substantive source passage represented.
- [ ] No substantive additions.
- [ ] Names, dates, numbers, quotations and references verified.
- [ ] Meaningful repetitions preserved.
- [ ] Ambiguities not silently resolved.
- [ ] Tone/register not inflated or flattened.
- [ ] English edited for genuine readability.
- [ ] Finished English rechecked against source after editing.
- [ ] Page markers preserved.
- [ ] Footnote IDs/references structurally valid.
- [ ] Translation manifest updated.
- [ ] Workbench updated.
- [ ] Changes committed/checkpointed.

## 14. Changing these rules

Improve this constitution when repeated real examples show that a rule is inadequate. Record consequential changes in Git. Do not casually rewrite the rules in the middle of a batch merely to justify a local translation choice.
