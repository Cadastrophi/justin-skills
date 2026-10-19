---
name: jww-repository-validation
description: Select, run, and report proportionate validation for repository changes when no more specific validation workflow applies. Use after editing code, configuration, templates, documentation, or automation; do not use when a language-specific skill already covers the change.
---

# Repository Validation

This is the general-purpose fallback for deciding how to validate a change when nothing else has specified it. Repository instructions and documented validation commands take precedence over these defaults.

Proportionate means matching the checks' scope and cost to the blast radius of
the change. Run the smallest sufficient set that covers the changed artifact
and behavior, widening to integration or end-to-end checks as the change's
reach grows.

## Discover the Checks

1. Read applicable `AGENTS.md`, `README`, contributor guidance, and nearby automation before choosing commands.
2. Inspect changed file types and available configuration such as `.editorconfig`, package manifests, CI workflows, task runners, and formatter or linter settings.
3. Prefer an existing documented check over inventing a new one.

## Choose Proportionate Validation

- Documentation: review readability and run `git diff --check`; run an available Markdown check when the repository uses one.
- Source code: when edits are authorized, format only changed files. Run focused tests, static analysis, or builds that exercise the change. For read-only review, report formatting differences without changing files.
- Configuration, templates, and scripts: render, parse, or dry-run the affected artifact, and run a syntax check when applicable.
- Broad or risky changes: add the relevant integration or end-to-end check when available.

Start with read-only checks. Do not install dependencies, apply configuration, migrate data, publish artifacts, or otherwise change external state merely to validate unless the task authorizes those effects.

## Report Results

1. Review failures against the changed behavior before declaring them regressions.
2. Report each exact command or named check and classify its result as passed,
   change-related failure, pre-existing failure, environment blocker, or skipped.
3. For skipped checks, state why they were unavailable or disproportionate and
   identify the remaining risk.
