---
name: capture-intent-docs
description: Capture agreed product intent from a conversation in the repository's docs. Use when asked to document, record, save, or update the intended behavior of a page or feature. Exclude implementation and architecture documentation.
---

# Capture Intent Docs

Record settled product behavior without preserving implementation decisions.

## Workflow

1. Read `docs/README.md` and any related intent documents.
2. Inspect the related code and current behavior. Use this to find differences, not to invent intent.
3. Extract only agreed user outcomes, behavior, states, and boundaries from the discussion.
4. Leave out code structure, frameworks, data models, APIs, algorithms, styling techniques, and discarded options.
5. Choose the document's place in the hierarchy. Prefer an existing document; otherwise use `docs/pages/` for page-owned behavior or `docs/features/` for behavior that crosses pages or serves its own user goal. Use a short, lowercase, hyphenated file name and the template in `docs/README.md`.
6. Use plain language, short sections, and specific statements. Remove repetition and unnecessary jargon.
7. Record only settled decisions. Leave unresolved ideas out and mention the omission to the user.
8. Compare the draft with the current implementation. Do not rewrite intent merely to match the code.
9. Present the target files, the exact draft or a clear diff, and every meaningful difference from the implementation.
10. Wait for explicit user approval before creating, editing, moving, or deleting anything in `docs/`. Treat feedback as a request to revise the draft, not as approval.
11. After approval, write only the reviewed content. Ask for approval again before making any substantial additional change.

## Completion

Confirm which intent documents changed and list any differences found between intent and implementation. Change implementation only when the user also asks for that work.
