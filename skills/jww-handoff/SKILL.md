---
name: jww-handoff
description: Write and resume a canonical handoff file for work that spans sessions, interruptions, or phases. Takes an optional mode argument, write or resume, and an optional task slug. Use when a task is paused, resumed, approaching a context limit, or split across review and implementation. Do not use for work that completes within the current session.
when_to_use: Trigger on requests like "write a handoff", "pick this up tomorrow", "I'm stopping here", "where did we leave off", or "resume that work", and before compaction when verified state would otherwise be lost.
argument-hint: "[write|resume] [task-slug]"
---

# Work Handoff

Preserve continuity in one durable file rather than in conversation history.
Automatic context compaction is not a handoff: it summarizes what was said, not
what was verified, and it does not survive a new session.

## Xcode Availability

Xcode can use the Write and Resume procedure when asked directly, but does not
run this skill's Codex or Claude prompt wrappers and hooks. Invoke the skill in
an Xcode conversation and state `write` or `resume` plus the optional task slug
in the request; capture remains manual before an interruption.

## Select the Mode

Read `$ARGUMENTS` when the harness provides it.

- `resume`, or an invocation naming an existing handoff: follow **Resume**.
- `write`, or no argument during active work: follow **Write**.
- No argument and no active work: follow **Resume** when a handoff exists for
  this repository, and otherwise report that none exists.

A second argument names the task slug. Infer it from the branch or the stated
objective when absent. When several handoffs could apply and neither the branch
nor the request identifies one, list the candidates and ask which to resume.

## Locate the Canonical File

1. Follow a handoff or planning-document location documented by the repository
   when one exists.
2. Otherwise use `.handoffs/<task-slug>.md` at the repository root. Confirm the
   path is ignored by version control before writing. If it is not ignored,
   report the needed `.handoffs/` entry and ask before changing either the
   repository or global ignore configuration. Ask before committing a handoff.
3. Update the existing file for a task. Do not create a parallel version, and do
   not split one outcome across several files. Link related tasks by path
   instead of repeating their content.
4. State the file path in the reply whenever the handoff is written or updated.

## Write

Write at a stable decision point, before a risky or long operation, and before
any expected interruption. Follow a repository-defined handoff format when one
exists; otherwise include these sections:

```markdown
# <Task title>

Updated: <YYYY-MM-DD>
Branch: <branch name, when the work is in Git>

## Objective
<The outcome, and the constraints that cannot be traded away.>

## Decisions
<Each decision with the evidence that settled it, cited by file and line.>

## Touched
<Files inspected, files changed, and why each matters.>

## Validation
<Each check run, its exact command, result, and when it was observed.>

## Open
<Unresolved risks, checks not run and why, and decisions needing Justin.>

## Next
<The exact next command or edit, precise enough to run without rereading this
whole file.>
```

Keep observed facts and proposed work in separate sections. Record a check as
current-session evidence only when its output was read in this session. Preserve
useful validation recorded by an earlier handoff with its observation date, but
do not present it as newly rerun. Record a failure with the smallest excerpt
that identifies it.

When an evidence ledger was kept during investigation, its lines populate
Decisions and Touched directly. Do not re-derive them from the conversation.

When updating an existing handoff, revise each section against current state.
Do not append a second copy of a section or leave a superseded claim in place.

## Resume

1. Read the handoff before reading source.
2. Verify the current state matches it: check the branch, the working tree, and
   any file the handoff claims to have changed.
3. Re-inspect source only where the handoff is stale, conflicts with the
   current state, or lacks evidence the next decision needs.
4. Report any divergence between the handoff and the repository before acting
   on it.
