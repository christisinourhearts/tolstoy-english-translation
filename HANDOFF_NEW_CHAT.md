# Tolstoy English Corpus — New Chat Handoff

## Latest durable checkpoint — P006.36

The repository has been revalidated and reconstructed through **P006.36**. The last durable checkpoint before the second temporary-workspace loss was P006.05; P006.06–33 were replayed from the exact previously accepted translation/QA records, one unit per commit, and P006.34–36 were then freshly reconstructed from the exact audited Russian witness. The replay does not claim to reproduce the vanished temporary Git commit hashes. The accepted English text, coverage records, and source-QA dispositions are the recovered project state.

**Next target:** P006.37, `corpus/azbuka/v21_023_023_Dva_volka_vyshli.md`. Do not redo P006.01–36 for stylistic preference.

This repository is the current repaired resumable master. It contains the complete surviving packaged Git history through P004.30 plus the new, explicitly documented recovery commits; the vanished later working-tree history is not claimed to have been recovered.

## What to upload in the new chat

Upload this English repository ZIP and the authoritative Russian repository ZIP (`tolstoy-russian-md-audited`). Use a unique filename for each upload if the interface has previously seen the same filename.

## First instruction for the new chat

Use this instruction:

> Resume the Tolstoy English corpus from the saved repository. Before doing any translation, verify that both ZIPs are actually mounted/readable. Read `HANDOFF_NEW_CHAT.md`, `TRANSLATION.md`, `metadata/DECISIONS.md`, `WORKBENCH.md`, `RECOVERY_RECONSTRUCTION.md`, `qa/batches/P004.md`, `qa/batches/P005.md`, and the provenance notes under `provenance/pd_core_pilot/`. Treat the Russian repository as read-only and as a licensed comparison witness; do not mass-delete or relabel its CC BY-SA metadata. Run `tools/check_source.py` against the uploaded Russian snapshot. P005 restoration is complete through P005.50; preserve P005.21–22 as the surviving recovery-package artifacts and do not redo completed units for stylistic preference. P006 is selected and complete through P006.36. P006.06–33 were replayed from the previously accepted session record after an ephemeral workspace loss; P006.34–36 were freshly reconstructed from the exact audited Russian witness in this recovery pass. Resume at P006.37 (`corpus/azbuka/v21_023_023_Dva_volka_vyshli.md`). Preserve the conservative-fidelity policy, keep the English translation license separate as `PROJECT-TBD`, commit each accepted unit separately, and keep the reconstructed-file provenance explicit. A fresh P005 cold-fidelity sample remains pending and must not inherit the lost-runtime cold-audit status.

## Current state

- P001: complete (7 units)
- P002: complete (25 units)
- P002 cold audit: complete
- P003: complete (50 / 50), with cold audit PASS AFTER REVISION
- P004: **50 / 50 represented; P004.01–30 are original packaged accepted units, P004.31–50 are explicitly documented fresh recovery reconstructions**
- P004 recovery audit: PASS AS DOCUMENTED RECONSTRUCTION (`qa/reports/P004_RECOVERY_AUDIT.md`)
- P005: **50 / 50 restored and reviewed**. P005.01–20 and P005.23–50 are fresh recovery reconstructions; P005.21–22 remain the surviving recovery-package artifacts.
- P006: **36 / 50 reviewed**. P006.01–05 are in the durable pre-loss checkpoint; P006.06–33 were deterministically replayed from the previously accepted session record; P006.34–36 are fresh recovery reconstructions against the exact audited Russian witness.
- Next translation target: **P006.37 — `corpus/azbuka/v21_023_023_Dva_volka_vyshli.md`**. P005 periodic cold audit is separately pending.
- Total reviewed translations in repaired manifest: **218**
- Approximate reviewed source-body words: **58,153**
- Structured bilingual coverage records: **211** (plus 7 P001 legacy unstructured passes)
- Confirmed source errata: **24**; source-verified anomalies: **5**
- Git history through P004.30 is the original packaged history. Recovery commits after that point are new and intentionally do not manufacture the vanished historical per-unit commits.

- The audited Russian snapshot remains an immutable CC BY-SA comparison witness. English translations are separately marked `translation_license: PROJECT-TBD`; do not infer ShareAlike status for the translation text merely from the witness metadata.
- The authoritative Russian ZIP mounted successfully in this runtime. Full source identity check at P006.36: 15,766 checked, 0 missing, 0 changed. Full translation validator: 218 English files, 0 errors, 2 longstanding intentional-Cyrillic warnings; structured coverage validator: 211 records, 0 errors.
- Read `RECOVERY_RECONSTRUCTION.md` before continuing.

## Source provenance development

The existing Russian snapshot remains byte-for-byte valid against its recorded source manifest, but it derives from Tolstoy Digital material distributed as CC BY-SA and contains normalized/editorial layers that should not simply be relabelled. A scan-led public-domain-core experiment is stored at `provenance/pd_core_pilot/`.

For the Volume 48 pp. 342–346 pilot, comparison with the printed scan showed that normalized Russian silently expands several visible editorial bracket completions (`Андр[ей]`, `на[до]`, `кот[орого]`, `пролетар[иата]`). The pilot preserves these provenance distinctions and uses neutral apparatus labels.

Crucially, the accepted English body survives the rebase unchanged: after removal of YAML, page comments, footnote markers, apparatus and whitespace variation, the accepted English and pilot English bodies match exactly. This supports retaining reviewed translations while progressively replacing their Russian textual authority with independently verified scan-led source files.

Do not delete or rewrite the old Russian corpus in place. Keep it available as a comparison witness until the rebase method has been tested on at least one published literary work and then adopted deliberately.

## Exact Russian source verification

The previously provisional P003.01–08 source check is now closed. In the resumed 2026-08-31 runtime, the uploaded Russian repository was physically mounted and `tools/check_source.py` checked all 15,766 manifest sources: 0 missing, 0 changed. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly.

The P003 boundary preflight on that exact snapshot produced only two MEDIUM flags among the 50 selected units: P003.39 and P003.45. Both were inspected. Their apparent nonterminal endings are caused by deletion markup with terminal punctuation inside the deleted span, and neighboring page units are independently segmented. They are intentional draft boundaries, not `SOURCE_SUSPECTED` cases.

A future runtime should still run the source check against whatever Russian ZIP is actually uploaded, because the repository's source identity is intentionally verified per runtime. If it is the same audited snapshot and the check is clean, do not reopen P003.01–29.

## P003.11 translation note

The Fet letter of 24 December 1877 was accepted in commit `6a0b316`. Tolstoy's familiar contracted patronymic `Афанасьич` is preserved as “Afanasich”; the full scholarly metadata form remains “Afanasy Afanasyevich Fet (Shenshin).” The mixed Russian/German title `Критика der reinen Vernunft` is rendered by the standard English title *Critique of Pure Reason*, with the original German code-switch recorded in `body_source_languages` and the coverage record.

## P003.12 translation note

The Nagornov letter from mid-May 1879 was accepted in commit `0750a40`. The source has plural `векселей` (“promissory notes”) followed immediately by singular `его` (“it”) in the instruction to arrange and discount the paper; the English deliberately preserves that mismatch rather than silently changing it to “them.” Neighboring 1879 Nagornov correspondence confirms that `учесть [вексель]` here is the financial sense “discount [a promissory note].” The horse remains gender-neutral in English because grammatical feminine `лошадь` does not establish biological sex. An anomalous colon splitting `Николай Михайлович: Нагорнов` in footnote 1 was normalized as nonsemantic punctuation and documented in the coverage record.

## P003.13 translation note

The Ilya Lvovich Tolstoy letter fragment from October 1887 was accepted in commit `8ff458d`. Tolstoy distinguishes human/Christian `любовь` from `влюбленье`; the English deliberately keeps the slightly unusual phrase “love—being in love” rather than flattening both into one generic “love” or introducing a freer psychological label. The authoritative 90-volume text shares the source's irregular `Если будет любовь одна — влюбленья`, so that construction was not silently regularized. The French `prétexte`, editorially glossed as `вид`, is rendered “appearance,” with the code-switch recorded in metadata. The closing `во имя чего ты действуешь` remains close as “what you are acting in the name of.”

## P003.14 translation note

The Ivan Ivanovich Petrov letter from September–November 1887 was accepted in commit `bbcf8bd`. Tolstoy names only `Иван Дмитриевич` in the body; surrounding correspondence strongly points to Ivan Dmitrievich Sytin, but the selected source does not supply the surname, so the English deliberately leaves him as “Ivan Dmitrievich” rather than silently identifying him. The recurrent closing `Дружески жму вам руку` follows the established corpus rendering “I shake your hand in friendship.” In editorial note 2, library-context `фонд` is rendered “collection” rather than the misleading financial “fund.” P003.14 raised no MEDIUM/HIGH boundary flag.

## P003.15 translation note

The Viktor Alexandrovich Goltsev letter of 24–28 April 1891 was accepted in commit `1080d84`. Tolstoy first calls S. T. Semenov's piece `статья` and then `рассказ`; the English preserves the shift as “article” and “story.” The repeated `поместить` remains repeated as “publish” rather than being stylistically collapsed. The polite `не поместите ли его?` is rendered “wouldn't you publish it?” The publication names are retained as *Russkaya Mysl* and *Russkie Vedomosti*, while editorial note 3 makes explicit that the latter reference is to the newspaper's feuilleton section. The sign-off `Любящий вас Л. Толстой` is kept conservatively as “Loving you, L. Tolstoy.” The external 90-volume text at tolstoy.ru was also checked and agrees with the mounted audited source at this letter. P003.15 raised no MEDIUM/HIGH boundary flag.

## P003.16 translation note

The Grigory Alexeyevich Ermolaev letter of 6 February 1892 was accepted in commit `968dcd9`. Tolstoy sends Fyodor Alexeyevich Strakhov to Klekotki to clarify the quantity and distribution of firewood and other matters. The English preserves the repetition in `расскажите и разъясните ему всё` as “tell him everything and explain everything to him” rather than compressing it. `все его распоряжения исполняйте` is rendered “carry out all his instructions,” avoiding the stronger “orders.” The closing `Желаю вам всего хорошего` is the plain “I wish you all the best.” In the scholarly footnote, famine-relief `столовые` is rendered contextually as “soup kitchens.” The mounted source hash matched exactly, P003.16 raised no MEDIUM/HIGH boundary flag, and the electronic 90-volume text was checked and agrees with the audited source at the letter.

## P003.17 translation note

The Trofim Fyodorovich Gotoitsev letter of 19 October 1896 was accepted in commit `1fe75ff`. Tolstoy's repeated friendship formula `Владимир Григорьевич Чертков мой близкий друг, такой же друг мой и Иван Михайлович Трегубов` is kept closely as “Vladimir Grigoryevich Chertkov is a close friend of mine, and Ivan Mikhailovich Tregubov is just as much a friend of mine,” rather than stylistically collapsing the repetition. `то, что они спрашивают у вас` remains the unspecified “what they are asking you for”; the English does not import “materials” into Tolstoy's body merely because the editorial apparatus explains what Chertkov and Tregubov sought. The scholarly note retains the historical terms “Caucasian Doukhobors” and “sectarians.” P003.17 raised no MEDIUM/HIGH boundary flag, its source hash matched exactly, and the electronic 90-volume text was checked and agrees with the mounted source.

## P003.18 translation note

The open statement to foreign publishers and translators, dated 25 February 1898 in the editorial heading, was accepted in commit `0c6e17f`. Tolstoy's document body is already in English in the authoritative source, so it is preserved verbatim rather than retranslated from the editors' Russian rendering; this includes the historical spellings “Vladimir Tchertkoff” and “Moscou.” The document itself is signed “8 March 1898,” and editorial note 5 says that this is a New Style date. The printed/electronic 90-volume edition confirms the exact coexistence of the 25 February heading and 8 March signature, so neither date was normalized or treated as a source error. Russian editorial notes 1–5 were translated separately as apparatus. P003.18 raised no MEDIUM/HIGH boundary flag and its source hash matched exactly.

## P003.19 translation note

The Alexander Nikiforovich Dunaev letter of 7–8 November 1898 was accepted in commit `209069c`. Tolstoy's slightly awkward `Слышу всё, что ваше здоровье физическое нехорошо` is kept closely as “I keep hearing that your physical health is not good,” preserving the explicit bodily/physical qualifier rather than smoothing it to generic “health.” `Мне хочется, чтобы он сам снес Коншину письмо` remains “I want him to take the letter to Konshin himself,” retaining both physical delivery and the emphasis that Archer should do it personally. The repetition `часто, часто` remains “often, often,” and `всей милой, дорогой семье` retains both adjectives as “the whole dear, beloved family.” The footnote marker remains attached to “these two letters.” P003.19 raised no MEDIUM/HIGH boundary flag, its source hash matched exactly, and the electronic 90-volume edition was checked and agrees with the mounted source and apparatus.

## P003.20 translation/source-QA note

The Fyodor Alexeyevich Strakhov letter headed 28 January 1905 was accepted in commit `8341552`. Its source SHA-256 matches the mounted audited Russian snapshot exactly and it raised no MEDIUM/HIGH boundary flag. During the apparatus audit, however, the audited Markdown was found to contain a bare numeral `3` after `карандашом` while defining only footnotes `[^1]` and `[^2]`. The official 90-volume electronic edition, volume 75, pp. 209–210, confirms that the numeral is footnote marker 3 and supplies the omitted third note: Strakhov recorded that Tolstoy conveyed through M. V. Syaskova that the marked passages should be included in *Circle of Reading*. This is now a confirmed source erratum in `metadata/source_errata.yml` and `qa/source_suspected/v75_298_F_A_Straxovu.json`. The Russian repository was not modified; the English restores only the verified marker/note while retaining the original Russian Markdown hash. `tools/validate_translation.py` now supports an exact manifest-declared `source_qa_extra_footnote_ids` exception only when `source_qa_status` is `confirmed_erratum`, so this recovery does not weaken footnote equality for ordinary units. The body keeps `отчеркнул карандашом` as “marked off in pencil” and `баллы` as “scores.” The heading's `January 28?` and the editorial unknown-hand note `Feb. 1905` are both preserved without reconciliation.

## P003.21 translation/source-QA note

The Samuil Vulfovich Danilevich letter of 17 May 1907 was accepted in commit `fd665d8`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag. The body preserves the standalone dative address `Данилевичу.` as “To Danilevich.” rather than inventing a warmer salutation; `намерениях чистоты жизни` remains the broad “intentions toward purity of life” rather than being narrowed to “chastity”; the repeated `успешной ... успеха` remains “a successful struggle ... the possibility of success”; and `постоянства и вследствие постоянства преуспеяния` remains “constancy and, as a result of constancy, progress.” During apparatus audit, the audited Markdown was found to contain a bare list item `3.` immediately before the p. 106 page marker. The official 90-volume edition, volume 77, pp. 105–106, confirms that the apparatus ends after note 2 and page 106 begins directly with letter 117; there is no third note or numeral. This is recorded as a confirmed non-substantive source erratum in `metadata/source_errata.yml` and `qa/source_suspected/v77_116_S_V_Danilevichu.json`. The Russian repository remains unchanged; the English omits only that spurious numeral and preserves the page marker and original source hash.

## P003.22 translation note

The Gavriil Alexandrovich Novichkov letter of 26 September 1907 was accepted in commit `9eb3bda`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag. Tolstoy's salutation uses the variant/familiar first-name form `Гаврило Александрович`, preserved in the body as “Gavrilo Alexandrovich,” while the metadata retains the catalogued full form “Gavriil Alexandrovich Novichkov.” `моему хорошему знакомому` remains “my good acquaintance,” not “friend”; `похлопотать о вашем деле у губернатора` is rendered “intercede in your case with the governor”; and the compact `что нужно и можно` remains “what is necessary and possible.” `От всей души соболезную вам` is rendered “With all my heart I sympathize with you,” and the final `мужественно и безропотно по-христиански переносите вашу невзгоду` remains close as “bearing your misfortune courageously and without complaint, in a Christian way.” All three editorial notes were translated and checked; no source erratum was found.

## P003.23 translation note

The Tatyana Andreevna Kuzminskaya letter of 4 August 1908 was accepted in commit `ea67984`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag; the official 90-volume electronic edition was also checked and agrees with the letter and apparatus. Tolstoy's `Только, наверное, не лейб-гусар` is kept as “Only, probably, not a Life Guards Hussar,” preserving the uncertainty rather than strengthening it. His mildly reproachful wish that Vasya would ask him about `вещи более нужные для жизни` remains “things more necessary for life,” without editorial expansion. `Братски целую тебя, Сашу и Васю` is rendered “I kiss you, Sasha, and Vasya as a brother.” In footnote 1, the historical unit `гвардейский экипаж` is rendered by its established English proper name “Guards Equipage.” All two editorial notes and three footnotes are translated; no source erratum was found.

## P003.24 translation note

The diary unit headed 14 January 1889 was accepted in commit `5b7dc01`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag. The source has the unusual sequence `<ins>14 января</ins> 12 Я. М. 89.`; the official 90-volume electronic edition confirms the same reading, so the English preserves both as `<ins>14 January</ins> 12 Jan. M. 89.` rather than reconciling the dates or opening a source erratum. The clipped diary phrases `Письма сочувственные и посещения. Ершов с книгой.` remain “Letters of sympathy and visits. Ershov with a book.” `Анархисты совсем правы, только не в насилии. Удивительное затмение.` is rendered “The anarchists are entirely right, except about violence. Astonishing blindness.” The obscure `весь изуродован наркотическим` is kept close as “he is entirely disfigured by narcotics,” without supplying a particular substance or diagnosis. The familiar names Sonya, Masha, and Posha are preserved as written. No apparatus or footnotes occur in this unit.

## P003.25 translation note

The diary entry of 15 July 1909 was accepted in commit `bce9c55`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag. The surrounding June 1909 diary and the volume 57 commentary identify `молитве Соничке` as the prayer Tolstoy was composing for his granddaughter Sonichka; the body therefore uses the restrained “a prayer for Sonichka” without adding the granddaughter identification to Tolstoy's text. `Написал и послал, но нехорошо` remains clipped as “Wrote it and sent it, but it is not good.” `живу не перед людьми, а перед Богом` is preserved as “I live not before people but before God,” and both occurrences of `забота о суде людском` remain “concern about people's judgment.” The concrete path image in `стоит на моем пути к Богу` is retained, as is the paired `Буду учиться и приучаться` → “I will learn and train myself.” `письмецо об устройстве общин` is rendered “a little letter about the organization of communities,” consistent with the nearby Abramov correspondence about a religious community rather than importing a narrower political meaning. No source erratum was found.

## P003.26 translation/source-QA note

The diary entry of 3 September 1862 was accepted in commit `7cdd907`. Its exact source SHA-256 matched the mounted audited Russian snapshot and it raised no MEDIUM/HIGH boundary flag. The official volume 48 text agrees with the diary body but confirms that the audited Markdown's empty definition for footnote `[^1]` is a source-layer defect: the missing gloss after Latin `Memento` is `Помни,` (“Remember,”). The erratum is recorded in `metadata/source_errata.yml` and `qa/source_suspected/v48_042_043_1862_09_03.json`; the English restores only the verified gloss, retains the original source hash, and leaves the Russian repository unchanged. The opening reported phrases and isolated `лорнет` remain deliberately unexpanded. The four alternatives in `либо... либо...` and the masculine forms in `нынче один, завтра другой` and `к чему отъезжающий` are preserved. `будущее с женой` remains the concrete “the future with a wife,” and `тихое обманывание друг друга — счеты` is kept as “the quiet deceiving of one another—keeping accounts,” preserving its unresolved accounting/score-keeping image. The source form `Дублицкой` is transliterated “Dublitskoy,” while the volume commentary's identification with the character Dublitsky is recorded only in coverage QA rather than inserted into Tolstoy's text. Latin `Memento` and German `mein schönes Herz` remain visible as language switches, with translated footnote glosses.

## P003.27 translation note

The diary entry of 17 March 1865 was accepted in commit `0f7af91`. Its exact source SHA-256, `524dec4d5e730d29f90c4d84d9b372d2ca6adeb672a310368e012a2649defbbd`, matched the mounted audited Russian snapshot, and its direct boundary result was CLEAR. The official volume 48 commentary identifies the funeral as that of Nikolai, the young son of Tolstoy's brother Sergei Nikolaevich, but the body remains the source's restrained “At the funeral at Seryozha's” rather than inserting that identity. In the overlapping-track image, grammatical feminine `собака` does not establish the dog's sex, so English uses gender-neutral “it/its,” while `точка опоры` remains “point of support.” The paradoxical repetitions in `премудрость Бога ... не премудрость, не ум ... инстинкт Божества` are preserved as “the wisdom of God ... not wisdom, not intelligence ... the instinct of the Deity,” and the following `ум` remains “intelligence.” The printed and audited body reads `Пашковых`; although the official commentary calls this a probable authorial slip for `Пашковских`, English preserves “Pashkovs” and records the uncertainty in coverage QA rather than emending Tolstoy. Mixed `Mémoire Ragus’a` is rendered *Ragusa's Memoirs* and recorded as a French switch. No Russian-source defect was found, and the Russian repository was not changed.

## P003.28 translation/source-QA note

The diary entry on volume 49, pp. 94–95 was accepted in commit `246227b`. Its exact source SHA-256, `1583173e53b515bed2265a72925ca850d4ea92ebc3295bf14e3e4ace6122a2da`, matched the mounted audited Russian snapshot, and its direct boundary result was CLEAR. The unit exposed a confirmed source-metadata defect: the audited filename, subtitle, `creation` field, and manifest row say 17 May 1883, while the file's own source-edition citation says `Дневник 1884 г.` The official volume places the entry inside the 1884 diary, and its manuscript description and commentary independently cite the 1884 agenda and contemporary correspondence. The stable source path and original hash remain unchanged, but English subtitle/creation metadata uses 17 May 1884. Both readings are recorded in `metadata/source_errata.yml` and `qa/source_suspected/v49_094_095_1883_05_17.json`; the Russian repository was not changed. French `pas de géants` remains visible with the translated gloss “giant steps.” The substantivized `Красное, заманчивое, похотливое` is “Beautiful, enticing, lustful,” continuing to describe the pagan element. Dialectal `Телятенской` is rendered “a man from Telyatinki,” `прогульную лошадь` is “a stray horse,” and `становой` is “district police officer.” The official commentary identifies Seryozha as Tolstoy's brother Sergei Nikolaevich, while the body preserves Bibikov's abrupt disruption: “Bibikov threw me off by saying that Seryozha would come.” Both `обратил` and `поворотить` remain forms of “turn,” preserving the link between Tolstoy's prayer and his realization that he himself had remained silent beside his wife.

## P003.29 translation/source-QA note

The diary entry of 22 February 1889 was accepted in commit `a0b27f7`. Its exact source SHA-256, `b1117e687e7b3533a04c13f558a9662c852c899cf0f93a804418516ba5560ab8`, matched the mounted audited Russian snapshot, and its direct boundary result was CLEAR. The apparatus audit found a confirmed source-layer omission: the audited Markdown retains footnote `[^1]`, `Можно прочесть: истопил`, after `потом`, but the official volume 50 p. 40 body reads `потом[34] [?] пришел Желтов`; note 34 gives the alternative as `Можно прочесть: истоп[ил]`. English restores only the verified `[?]` after the existing footnote marker, translates the note as “May be read: *lit the stove*,” retains the original hash, and leaves the Russian repository unchanged. Singular `написал письмо Семенову и Rod’y` remains “wrote a letter to Semenov and to Rod.” The author-as-book shorthand remains “Took Robertson from Gautier's,” while `учение 12 Апостолов` is *The Teaching of the Twelve Apostles*. The singular agreement and comma in `Мудрость, знание у нас распалось на два` remain “Wisdom, knowledge, among us has split into two,” and the five existential questions and repeated `только не` contrast are preserved separately.

## Repository maintenance note

The P003.01–08 manifest rows had `english_edit_status: "passed"`, while the repository validator requires the established value `"complete"`. This metadata-only mismatch was normalized in commit `036d650`; no translated text was changed. The translation validator then returned 0 errors (with only two longstanding intentional-Cyrillic warnings elsewhere in the corpus).

## Essential editorial preference

Decision D0001 remains governing policy: favor a close, conservative rendering when Tolstoy's Russian maps naturally into intelligible contemporary English. Do not replace concrete or mildly unusual source phrasing with smoother abstractions simply because they sound more idiomatic. A settled example is “the whole world of people,” which is preferred to the stylistically freer “all humanity.”

See `WORKBENCH.md` for the precise production sequence and current counters.


## P005.01 restoration checkpoint

P005.01 (`corpus/works/v01_226_228_S_teh_por_kak_ja_pomnju_svoju_zhizn.md`) has now been freshly reconstructed and reviewed. It is an 1847 untitled philosophical fragment in two variants. The translation deliberately preserves Tolstoy's rough draft logic, two illegible spans, repeated limited/unlimited and activity/inactivity terminology, and the I/not-I formulation. All three editorial notes are translated and structured coverage passes. The pinned source hash is retained, but—like the P004 emergency reconstruction—the exact Russian byte-level validator must be rerun when the audited Russian snapshot is physically mountable. Next target: P005.02.


## P005.02 restoration checkpoint

P005.02 (`corpus/works/v01_229_232_O_tseli_filosofii.md`), *On the Aim of Philosophy*, has now been freshly reconstructed and reviewed. It preserves the young Tolstoy's schematic a)–e) notebook form, internal numbering, manuscript uncertainty/expansion marks, abrupt person shifts, and repeated philosophical vocabulary rather than regularizing them into polished doctrine. The full official volume 1 witness and the single editorial note were checked; structured coverage passes. Exact Russian byte-level validation remains pending with the repository-wide recovery gate. Next target is P005.03; unlike P005.01–02, it contains graphic musical notation, so its exact Markdown/image representation should be recovered or inspected before final acceptance.
