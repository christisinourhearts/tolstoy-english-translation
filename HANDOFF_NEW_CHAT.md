# Tolstoy English Corpus — New Chat Handoff

This repository is the current resumable master. It contains the complete local Git history.

## What to upload in the new chat

Upload this English repository ZIP and the authoritative Russian repository ZIP (`tolstoy-russian-md-audited`). Use a unique filename for each upload if the interface has previously seen the same filename.

## First instruction for the new chat

Use this instruction:

> Resume the Tolstoy English corpus from the saved repository. Before doing any translation, verify that both ZIPs are actually mounted/readable. Read `HANDOFF_NEW_CHAT.md`, `TRANSLATION.md`, `metadata/DECISIONS.md`, `WORKBENCH.md`, and `qa/batches/P003.md`. Treat the Russian repository as read-only. Run `tools/check_source.py` and the P003 boundary preflight against the uploaded Russian snapshot. If the snapshot matches cleanly, resume at P003.17. Preserve the conservative-fidelity policy and commit each accepted unit separately. Do not redo completed units for stylistic preference.

## Current state

- P001: complete (7 units)
- P002: complete (25 units)
- P002 cold audit: complete (10 sampled units; no hard fidelity defects)
- P003: in progress, 16 / 50 accepted
- Last accepted unit: P003.16 — letter to G. A. Ermolaev, 6 February 1892
- Next unit: P003.17 — letter to T. F. Gotoitsev, 19 October 1896
- Total reviewed translations: 48
- Approximate reviewed source-body words: 9,599
- Structured bilingual coverage records: 41
- Git working tree at handoff: clean after this handoff commit

## Exact Russian source verification

The previously provisional P003.01–08 source check is now closed. In the resumed 2026-08-31 runtime, the uploaded Russian repository was physically mounted and `tools/check_source.py` checked all 15,766 manifest sources: 0 missing, 0 changed. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly.

The P003 boundary preflight on that exact snapshot produced only two MEDIUM flags among the 50 selected units: P003.39 and P003.45. Both were inspected. Their apparent nonterminal endings are caused by deletion markup with terminal punctuation inside the deleted span, and neighboring page units are independently segmented. They are intentional draft boundaries, not `SOURCE_SUSPECTED` cases.

A future runtime should still run the source check against whatever Russian ZIP is actually uploaded, because the repository's source identity is intentionally verified per runtime. If it is the same audited snapshot and the check is clean, do not reopen P003.01–16.

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

## Repository maintenance note

The P003.01–08 manifest rows had `english_edit_status: "passed"`, while the repository validator requires the established value `"complete"`. This metadata-only mismatch was normalized in commit `036d650`; no translated text was changed. The translation validator then returned 0 errors (with only two longstanding intentional-Cyrillic warnings elsewhere in the corpus).

## Essential editorial preference

Decision D0001 remains governing policy: favor a close, conservative rendering when Tolstoy's Russian maps naturally into intelligible contemporary English. Do not replace concrete or mildly unusual source phrasing with smoother abstractions simply because they sound more idiomatic. A settled example is “the whole world of people,” which is preferred to the stylistically freer “all humanity.”

See `WORKBENCH.md` for the precise production sequence and current counters.
