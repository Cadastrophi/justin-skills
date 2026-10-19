---
name: jww-bounded-investigation
description: Keep a written evidence ledger and delegate whole-repository searches during investigation that spans many files. Use for debugging, audits, and archaeology where the relevant code's location is unknown. Do not use when the relevant files are already identified, or for ordinary edits to known code.
---

# Bounded Investigation

Keep a multi-file investigation bounded by delegating broad discovery and
recording the evidence needed to verify the conclusion. Targeted reads and
narrow commands are assumed; they are not what this skill adds.

## When to Use

Invoke this when the work is investigation and the relevant code is not yet
located, such as:

- a stack trace or error with no obvious owning file
- a "why does X happen" question naming a behavior but no source
- an audit or archaeology pass that will span many files

Skip it once the relevant files are identified, or for ordinary edits to known
code.

## Delegate Fan-Out Searches

Delegate a sweep to a read-only search agent when the harness provides one,
delegation is authorized, and both conditions hold:

- the location is unknown — many candidate files, uncertain naming, or a
  whole-repository code search
- you need the conclusion, not the surrounding code

Run the search yourself when the target is specific enough that the output is
small, or when judging the surrounding code matters more than finding it.
Keep synthesis and verification in the primary agent: inspect the cited source
before relying on a delegated conclusion.

## Keep an Evidence Ledger

Keep the ledger in your working notes or a scratch file for the session; it is
not committed. Record one line per finding: the source, the observation, and
what it rules in or out.

```text
src/Session/Store.swift:88 — writes cache off the main actor — explains the
crash, rules out the decoder path
```

Record ruled-out branches and sources that were checked and added nothing.
Without them, the same file gets read again later in the same investigation.

The ledger is the raw material for a handoff: its lines become the Decisions
and Touched sections of `jww-handoff`, so keeping it makes that handoff nearly
free to write.

## Report

Lead with the conclusion, then the evidence that supports it and the caveats
that affect trusting it. Cite by file and line so the reasoning can be
rechecked without reproducing the search.
