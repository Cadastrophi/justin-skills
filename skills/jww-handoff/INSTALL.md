# Installing Handoff

`SKILL.md` is the procedure and the only required file. Everything else adapts
it to a harness.

## Install the Skill

One command covers all three harnesses. Repeat `-a` per agent; a comma-
separated list is rejected.

```sh
npx skills add justin/jww-skills \
  --skill jww-handoff \
  -a claude-code -a codex -a github-copilot \
  --global
```

The skill installs to `~/.agents/skills/jww-handoff/` and is wired into each
agent's own skills directory from there. The whole directory is preserved, so
`hooks/` and `prompts/` arrive with it. Invoke it as `/jww-handoff` in Claude
Code, or as `$jww-handoff` in Codex.

This installs from the published repository, so a skill that has not been
pushed yet will report `No matching skills found`. Until then, install from a
local checkout:

```sh
npx skills add . --skill jww-handoff -a claude-code -a codex -a github-copilot --global
```

## Claude Code

Custom commands and skills are the same mechanism, so no command file is
needed. The command name comes from the installed directory, so the skill is
`/jww-handoff`. Both you and Claude can invoke it, and arguments reach the
skill as `$ARGUMENTS` whether typed after the command or passed by Claude.

Do not add `disable-model-invocation: true` while the `PreCompact` hook is in
use. That hook works by asking Claude to write the handoff, which requires
Claude to load the skill itself; blocking model invocation disables the capture
the hook exists to trigger. Without the hook, the field is a reasonable way to
keep `/jww-handoff` manual, at the cost of Claude no longer reaching for it
when a session is winding down.

The hooks are optional and Claude Code only. They make resuming and capturing
deterministic rather than dependent on the model noticing the moment. Point the
configuration at the installed skill rather than copying the scripts, so that
`npx skills update` keeps them current:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear",
        "hooks": [
          {
            "type": "command",
            "command": "~/.agents/skills/jww-handoff/hooks/session-start.sh",
            "timeout": 10,
            "statusMessage": "Checking for a work handoff..."
          }
        ]
      }
    ],
    "PreCompact": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "~/.agents/skills/jww-handoff/hooks/pre-compact.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

Merge that into `~/.claude/settings.json`, or into a project's
`.claude/settings.json` to scope it to one repository. Confirm the scripts kept
their executable bit after installation:

```sh
chmod +x ~/.agents/skills/jww-handoff/hooks/*.sh
```

`session-start.sh` reads the most recently modified file in `.handoffs/` at the
repository root and injects it as context, truncating at 8,000 characters to
stay under the 10,000-character limit on injected values. It requires
`python3`. It exits 0 and emits `{}` when there is no repository, no
`.handoffs/` directory, no handoff file, or no interpreter, so it cannot block
a session from starting.

`pre-compact.sh` injects context only and never blocks compaction.

## Codex

The skill is invocable as `$jww-handoff` once installed. The prompt wrapper is
optional and only shortens that to `/handoff write` or `/handoff resume`:

```sh
cp ~/.agents/skills/jww-handoff/prompts/codex/handoff.md ~/.codex/prompts/handoff.md
```

Codex scans only top-level Markdown files in `~/.codex/prompts/`, so keep the
file directly in that directory. Codex documents custom prompts as no longer
the recommended approach, so prefer the skill and treat this wrapper as a
convenience.

Codex has no hook equivalent, so capture before an interruption is manual.

## Copilot

The install command above covers Copilot. The prompt wrapper is optional and
adds a `/handoff` entry with prompted arguments:

```sh
mkdir -p .github/prompts
cp ~/.agents/skills/jww-handoff/prompts/copilot/handoff.prompt.md .github/prompts/
```

Prompt files are workspace-scoped, so this is per repository.

Copilot has no hook equivalent.

## Ignoring the Handoff Directory

The skill writes to `.handoffs/` at the repository root and expects that path
to be ignored. Prefer a global ignore file so each repository does not need its
own entry:

```sh
git config --global core.excludesfile ~/.gitignore_global
printf '.handoffs/\n' >> ~/.gitignore_global
```
