# Tolstoy English Corpus — New Chat Handoff

This repository is the current resumable master. It contains the complete local Git history.

## What to upload in the new chat

Upload this English repository ZIP and the authoritative Russian repository ZIP (`tolstoy-russian-md-audited`). Use a unique filename for each upload if the interface has previously seen the same filename.

## First instruction for the new chat

Use this instruction:

> Resume the Tolstoy English corpus from the saved repository. Before doing any translation, verify that both ZIPs are actually mounted/readable. Read `HANDOFF_NEW_CHAT.md`, `TRANSLATION.md`, `metadata/DECISIONS.md`, `WORKBENCH.md`, and `qa/batches/P003.md`. Treat the Russian repository as read-only. Run `tools/check_source.py` and the P003 boundary preflight against the uploaded Russian snapshot. If the snapshot matches cleanly, resume at P003.11. Preserve the conservative-fidelity policy and commit each accepted unit separately. Do not redo completed units for stylistic preference.

## Current state

- P001: complete (7 units)
- P002: complete (25 units)
- P002 cold audit: complete (10 sampled units; no hard fidelity defects)
- P003: in progress, 10 / 50 accepted
- Last accepted unit: P003.10 — letter to M. N. Longinov, 19 November 1865
- Next unit: P003.11 — letter to A. A. Fet, 24 December 1877
- Total reviewed translations: 42
- Approximate reviewed source-body words: 8,759
- Structured bilingual coverage records: 35
- Git working tree at handoff: clean after this handoff commit

## Exact Russian source verification

The previously provisional P003.01–08 source check is now closed. In the resumed 2026-08-31 runtime, the uploaded Russian repository was physically mounted and `tools/check_source.py` checked all 15,766 manifest sources: 0 missing, 0 changed. P003.01–08 were also confirmed individually against their recorded SHA-256 hashes; all eight matched exactly.

The P003 boundary preflight on that exact snapshot produced only two MEDIUM flags among the 50 selected units: P003.39 and P003.45. Both were inspected. Their apparent nonterminal endings are caused by deletion markup with terminal punctuation inside the deleted span, and neighboring page units are independently segmented. They are intentional draft boundaries, not `SOURCE_SUSPECTED` cases.

A future runtime should still run the source check against whatever Russian ZIP is actually uploaded, because the repository's source identity is intentionally verified per runtime. If it is the same audited snapshot and the check is clean, do not reopen P003.01–10.

## Repository maintenance note

The P003.01–08 manifest rows had `english_edit_status: "passed"`, while the repository validator requires the established value `"complete"`. This metadata-only mismatch was normalized in commit `036d650`; no translated text was changed. The translation validator then returned 0 errors (with only two longstanding intentional-Cyrillic warnings elsewhere in the corpus).

## Essential editorial preference

Decision D0001 remains governing policy: favor a close, conservative rendering when Tolstoy's Russian maps naturally into intelligible contemporary English. Do not replace concrete or mildly unusual source phrasing with smoother abstractions simply because they sound more idiomatic. A settled example is “the whole world of people,” which is preferred to the stylistically freer “all humanity.”

See `WORKBENCH.md` for the precise production sequence and current counters.
