#!/usr/bin/env bash
# Claude Code PreCompact hook. Compaction summarizes what was said, not what
# was verified, so this asks for the handoff to be brought current while the
# full context is still available.
#
# Injects context only. It never blocks compaction: a handoff is worth less
# than a session that cannot continue.

set -uo pipefail

cat <<'JSON'
{
  "hookSpecificOutput": {
    "hookEventName": "PreCompact",
    "additionalContext": "Context is about to be compacted. Before it is, write or update the canonical work handoff for this task using the jww-handoff skill, so that verified state survives in a file rather than only in this conversation. Record only checks that actually ran and whose output was read, and keep proposed work separate from observed facts. Skip this if the current work completes within this session or no durable state has accumulated."
  }
}
JSON
