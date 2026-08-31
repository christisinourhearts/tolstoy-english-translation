# Tolstoy English Corpus — New Chat Handoff

This repository is the current resumable master from the previous chat. It contains the complete local Git history.

## What to upload in the new chat

Upload this English repository ZIP and the authoritative Russian repository ZIP (`tolstoy-russian-md-audited`).

## First instruction for the new chat

Use this instruction:

> Resume the Tolstoy English corpus from the saved repository. Before doing any translation, verify that both ZIPs are actually mounted/readable. Read `HANDOFF_NEW_CHAT.md`, `TRANSLATION.md`, `metadata/DECISIONS.md`, `WORKBENCH.md`, and `qa/batches/P003.md`. Treat the Russian repository as read-only. Run the exact source/hash check and P003 boundary preflight against the uploaded Russian snapshot. Confirm P003.01–08 source hashes. If clean, resume at P003.09. Preserve the conservative-fidelity policy and commit each accepted unit separately. Do not redo completed units for stylistic preference.

## Current state

- P001: complete (7 units)
- P002: complete (25 units)
- P002 cold audit: complete (10 sampled units; no hard fidelity defects)
- P003: in progress, 8 / 50 accepted
- Next unit: P003.09 — letter to N. A. Nekrasov, 11 November 1857
- Total reviewed translations: 40
- Git working tree at handoff: clean

## Essential editorial preference

Decision D0001 is important: favor a close, conservative rendering when Tolstoy's Russian maps naturally into intelligible contemporary English. Do not replace concrete or mildly unusual source phrasing with smoother abstractions simply because they sound more idiomatic. A settled example is “the whole world of people,” which is preferred to the stylistically freer “all humanity.”

## Why the exact Russian ZIP must be rechecked

In the previous runtime, newly uploaded Russian ZIPs were received by the chat but failed to mount into the filesystem. P003.01–08 were therefore compared against authoritative 90-volume source text rather than the exact uploaded repository snapshot. They remain accepted provisionally, but the new runtime should confirm their source hashes before continuing.

See `WORKBENCH.md` for the precise sequence.
