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

Store English files under `translations/` in reader-facing category folders:
`works`, `letters`, `diaries`, `notes`, `primer`, and `circle_of_reading`.
Use the printed-edition volume/page prefix followed by an English title slug.

Example:

```text
Russian source: corpus/azbuka/v21_026_026_Byla_u_Nasti_kukla.md
English file:   translations/primer/v21_026_026_Nastya_Had_a_Doll.md
```

The English path is for navigation, not source identity. Preserve the immutable
Russian path in `source_ru_path`, the source checksum in `source_ru_sha256`, and
the stable manifest `id`. Record every path change in
`project/metadata/english_path_migration.csv`.

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

The default posture is conservative fidelity. When a close rendering is clear and intelligible in English, preserve the source's concrete wording, imagery, repetitions, and unusual turns rather than replacing them with a smoother abstraction. “Contemporary English” means avoiding needless archaism and accidental Russian stiffness; it does not mean rewriting Tolstoy into more idiomatic or elegant English than the source warrants. See `project/metadata/DECISIONS.md` for consequential examples and standing editorial decisions.

- Use normal contemporary English syntax when Russian syntax carries no special force.
- Prefer ordinary English words when Tolstoy uses ordinary Russian words.
- Avoid decorative synonyms introduced only to prevent repetition.
- Avoid needless archaism: `whilst`, `thereupon`, `wherefore`, etc. require a textual reason.
- Do not simplify the thought merely because a sentence is intellectually difficult.
- Long sentences may remain long when their logical structure remains intelligible in English.
- Dialogue should sound like speech appropriate to the character and period without becoming theatrical pseudo-nineteenth-century English.
- Contractions may be used when natural to the register; they are not automatically modernizing or colloquializing.

## 6. Tolstoy's recurrent vocabulary

Do not translate recurrent philosophical or religious terms mechanically, but notice them deliberately. Maintain a terminology record in `project/metadata/TERMINOLOGY.md` when a choice has corpus-wide consequences.

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

Record recurring person-name decisions in `project/metadata/NAMES.md` rather than solving them independently in every file.

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

## 11. Source-suspicion protocol

The audited Russian corpus is the normal translation authority, but no digital corpus should be treated as infallible. A translator must distinguish **difficulty in Tolstoy** from a **possibly damaged source reading**.

Mark a passage `SOURCE_SUSPECTED` when the source contains a reading that is unexpectedly ungrammatical, semantically incoherent, internally contradictory, anomalous in a name/number/date, or otherwise looks more like transcription/OCR/encoding damage than deliberate roughness. Do not use this flag merely because Tolstoy is difficult, archaic, fragmentary, or stylistically unusual.

When `SOURCE_SUSPECTED` is triggered:

1. Stop finalizing the affected passage.
2. Identify the volume and printed page from the preserved page marker/front matter.
3. Check the 90-volume printed/electronic page and, where useful, an independent witness.
4. Record the issue under `project/qa/source_suspected/` and in the manifest `source_qa_flags`.
5. Never silently repair the Russian repository.
6. If the digital reading is confirmed, translate it and close the flag as `source_verified`.
7. If a source error is confirmed, record both readings in `project/metadata/source_errata.yml`, state which reading governs the English translation, and retain the original source hash.
8. If the reading cannot be resolved, keep the translation unit out of `reviewed` status and mark it `needs_source_review`.
9. If a confirmed source erratum requires the English structure to differ from the audited Markdown (for example, restoring a verified missing footnote), declare the exact structural exception in the translation manifest so mechanical validation remains narrow and auditable.

The system must prefer an explicit unresolved source problem over an ingenious invented interpretation.

For corpus families made of many small independently segmented files (especially *New Azbuka* material), perform a boundary sanity check before translation. A file that begins or ends in the middle of an ordinary sentence, has an obviously unfinished final clause, or conflicts with its stated page range should trigger `SOURCE_SUSPECTED`. Check the neighboring page/file and the full volume before assuming that the fragment is intentional. A valid source hash proves identity, not completeness of segmentation.

## 12. Compilations, adapted quotations, and wordplay

In compilations such as *Krug chteniya*, the Russian text selected, translated, shortened, or adapted by Tolstoy is itself the source object for this English corpus. Do not silently replace it with a familiar published English translation of the attributed author, Bible passage, or proverb. External originals may be consulted to resolve meaning or attribution, but the English should represent Tolstoy's compiled wording unless a separate editorial policy explicitly says otherwise.

When a passage depends on sound-play, punning, or deliberate mishearing that cannot survive literally in English, preserve the semantic action and record the untranslatable correspondence in the coverage record. Do not invent a substantially different English joke merely to recreate an effect.

## 13. Bilingual coverage proof

A translation cannot be accepted merely because it reads well or passes structural validation. Its final audit must make an exhaustive source-to-English pass whose primary question is: **is every substantive source element represented, and is every substantive English element supported by the source?**

For every P002-and-later accepted unit, create a structured record under `project/qa/coverage/`. The record must identify the source path and SHA-256 and state at minimum:

- coverage method (`exhaustive_source_to_target_pass`);
- whether every substantive source passage was checked;
- known omissions (normally zero);
- known unsupported additions (normally zero);
- names/numbers/dates checked;
- headings/page markers/footnote structure checked where applicable;
- ambiguities or source-suspected readings encountered;
- final result (`PASS`, `NEEDS_REVIEW`, or `SOURCE_SUSPECTED`).

The bilingual audit should proceed from the source forward, not merely by rereading the English. Every source sentence or fragment must be deliberately accounted for. Then perform a reverse English-to-source scan looking for explanatory material, intensification, or meaning with no source support.

A mechanical paragraph or sentence count is useful only as a warning signal. Russian and English may legitimately divide sentences or paragraphs differently. Counts do not constitute semantic proof.

Any omission, unsupported addition, reversed relation, wrong subject/speaker, lost negation, altered modality, wrong name/number/date, or other hard fidelity error blocks acceptance until corrected. Legitimate interpretive alternatives may be recorded without blocking acceptance when the chosen English is defensible and does not conceal uncertainty in the source.

## 14. Periodic cold audits

Batch acceptance does not eliminate the need for fresh-pass checking. At regular intervals, select a deliberately difficult sample of accepted translations and compare the final English directly against the source without first reading the unit's earlier translation reasoning or coverage notes.

The cold audit must distinguish **hard fidelity defects** from **non-blocking wording alternatives**. Hard defects include omissions, unsupported additions, reversed relations, lost negation or modality, wrong subjects/speakers/referents, incorrect names/numbers/dates, or structural loss. A merely conceivable alternative translation is not a defect.

Record cold audits under `project/qa/reports/` and, where useful, per-unit structured records under `project/qa/cold_audit/`. If a hard defect is found, correct the translation, update its QA/manifest state, and consider widening the sample to determine whether the problem is local or systemic.

A cold pass performed by the same model in a later/fresh reading context is useful but should not be mislabeled as independent-model or human verification. At publication scale, periodically use a genuinely separate model/context or human reader when available.

## 15. Gauntlet workflow

Each translation unit passes through finite stages. The creator of a translation should not be its only critic.

1. **Translate** — produce a complete English rendering from the audited source.
2. **Fidelity audit** — compare Russian/source text against English and identify concrete omissions, additions, misread syntax, incorrect referents, tone shifts, factual errors, or structural loss.
3. **Revision** — correct substantiated fidelity issues.
4. **English edit** — read the English as English; remove calques, stiffness, and accidental obscurity without taking new liberties.
5. **Final source audit / coverage proof** — compare the finished English against the source again after stylistic editing, source-to-target and then target-to-source; write the structured coverage record.
6. **Mechanical validation** — verify file identity, page markers, footnote IDs, Markdown structure, and source hash.
7. **Checkpoint/commit** — update the manifest and workbench before beginning the next unit.

Critics must cite a specific source passage and a specific problem. “Could be better” is not a defect report.

Do not loop indefinitely. A unit passes when no substantive fidelity defects remain, the English is intelligible and natural at the source's register, and mechanical validation passes.

## 16. Batch sizing and persistence

Assume the active AI context can disappear at any time.

- Never hold unique progress only in chat context.
- Save completed translation text before beginning criticism.
- Update `project/docs/WORKBENCH.md` and `project/translation_manifest.jsonl` after every accepted unit or small batch.
- Commit frequently.
- For long works, process chapter/section chunks internally, but keep the final repository's one-to-one file identity unless there is a compelling technical reason otherwise.
- A resumed session should be able to determine the next action from the repository alone.

## 17. Acceptance checklist

A completed unit should satisfy all applicable items:

- [ ] Correct Russian/source file and SHA-256 recorded.
- [ ] Every substantive source passage represented.
- [ ] Structured bilingual coverage record exists and passes (P002+).
- [ ] No substantive additions.
- [ ] Names, dates, numbers, quotations and references verified.
- [ ] Meaningful repetitions preserved.
- [ ] Ambiguities not silently resolved.
- [ ] Any suspicious source reading handled through the `SOURCE_SUSPECTED` protocol.
- [ ] Tone/register not inflated or flattened.
- [ ] English edited for genuine readability.
- [ ] Finished English rechecked against source after editing.
- [ ] Page markers preserved.
- [ ] Footnote IDs/references structurally valid.
- [ ] Translation manifest updated.
- [ ] Workbench updated.
- [ ] Changes committed/checkpointed.

## 18. Changing these rules

Improve this constitution when repeated real examples show that a rule is inadequate. Record consequential changes in Git. Do not casually rewrite the rules in the middle of a batch merely to justify a local translation choice.
