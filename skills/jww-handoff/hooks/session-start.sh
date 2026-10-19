#!/usr/bin/env bash
# Claude Code SessionStart hook. Surfaces the most recently updated handoff so
# a resumed session starts from recorded state instead of rediscovering it.
#
# Always exits 0 and always emits valid JSON. A missing handoff, a repository
# without one, or a missing interpreter must never block a session from
# starting.

set -uo pipefail

emit_nothing() {
  printf '{}\n'
  exit 0
}

command -v python3 >/dev/null 2>&1 || emit_nothing

root=$(git rev-parse --show-toplevel 2>/dev/null) || emit_nothing
[ -n "$root" ] || emit_nothing
[ -d "$root/.handoffs" ] || emit_nothing

HANDOFF_DIR="$root/.handoffs" python3 <<'PY'
import json
import os
import pathlib

limit = 8000
directory = pathlib.Path(os.environ["HANDOFF_DIR"])

files = [p for p in directory.glob("*.md") if p.is_file()]
if not files:
    print("{}")
    raise SystemExit(0)

newest = max(files, key=lambda p: p.stat().st_mtime)

try:
    body = newest.read_text(encoding="utf-8", errors="replace")
except OSError:
    print("{}")
    raise SystemExit(0)

truncated = len(body) > limit
if truncated:
    body = body[:limit] + "\n\n[truncated; read the file for the rest]"

others = sorted(p.name for p in files if p != newest)

lines = [
    "A work handoff exists for this repository at "
    f"{newest}. It records state from an earlier session.",
    "",
    "Read it before reading source, and verify it against the current branch, "
    "the working tree, and any file it claims to have changed. Report any "
    "divergence before acting on it.",
]

if others:
    lines += ["", "Other handoffs present: " + ", ".join(others) + "."]

lines += ["", "--- handoff contents ---", body]

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n".join(lines),
    }
}))
PY
