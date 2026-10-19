---
name: jww-git-workflow
description: Apply Justin's detailed Git and pull-request workflow. Use when planning or performing branches, commits, rebases, history cleanup, pushes, pull requests, or GitHub work. Do not use for read-only Git inspection or when a repository's own workflow documentation already covers the task.
---

# Git Workflow

Follow repository-specific instructions first. Treat them as the source of truth for branch names, remotes, checks, and pull-request conventions. Read them before changing Git state.

This skill assumes the general Git-safety rules supplied by the environment (preserve unrelated work, approval before destructive remote changes, verbatim CLI output). What it adds:

- commit subjects that name delivered behavior, with a body whenever rationale is not evident from the diff (see Commit Workflow)
- rebase a feature branch onto its base rather than merging the base in
- apply pull-request feedback by amending the relevant existing commit, not a follow-up commit
- when a push rewrites a published branch, use `--force-with-lease` and reconcile a stale lease before overwriting
- pushing a validated branch and opening or updating its PR is a routine step that needs no separate approval; merging, deleting, and other remote mutations still do

## Before Changing Git State

1. Inspect `git status`, the current branch, and relevant repository instructions.
2. Preserve unrelated changes. Do not discard work or clean history without the required approval. Amend commits only as directed in the commit workflow.
3. Separate exploratory work from completed implementation. Only stage and commit the latter.

## Commit Workflow

1. Review the intended diff and stage only files belonging to the completed change.
2. Run the validation required by the repository and review the staged diff before committing.
3. Keep each commit cohesive. When applying feedback to an existing pull request or work in progress, amend the applicable existing commit instead of adding a follow-up commit, unless Justin or repository conventions require separate commits.
4. Write a capitalized imperative subject that describes the delivered behavior, not the implementation phase or files changed. Omit a trailing period and keep it under about 60 characters. Do not use type or scope prefixes.
5. Add a body whenever the rationale is not evident from the diff. Always do so for security, concurrency, or default changes, and for changes that remove or restrict existing behavior. Explain the problem first, then the change, then any consequence the reader needs. Wrap the commit body at 72 columns; do not enumerate changed files.
6. Never use literal `\\n` escape sequences as line breaks in commit messages. For a multiline message, write actual newlines to a temporary file and commit with `git commit --file`; after committing, inspect the stored message with `git log -1 --format=%B`.
7. When a commit resolves an issue, close with exactly one issue reference on its final line, such as `Closes #231` or `Fixes #253`. Do not mention an assistant, model, agent, or tool, and do not add generated-by trailers.
8. Rewrite a consolidated commit message to describe the delivered feature, rather than the final working checkpoint.

## Updating and Publishing

1. Rebase a feature branch onto its remote base branch rather than merging the base branch into it, unless the repository explicitly requires otherwise.
2. Before pushing, verify the branch, remote, and exact commits that will be sent.
3. Push a validated feature branch and create or update its pull request when that completes Justin's request; no separate approval is needed for those routine publication steps. Do not merge, delete branches or tags, change repository settings, or make another destructive remote mutation without explicit approval.
4. When an amendment rewrites a published branch, force-push only with `--force-with-lease`. If the lease is stale, fetch and compare remote work before deciding how to proceed; preserve equivalent or concurrent work rather than overwriting it.

## Pull Requests and GitHub

1. Follow repository-specific pull-request requirements before general guidance.
2. Preserve decision-relevant Git and GitHub CLI output verbatim, especially errors and remote-state conflicts.
3. For review feedback, CI failures, or pull-request triage, use the harness's GitHub integration or the `gh` CLI. Do not claim connector or CLI output includes information it does not provide.
