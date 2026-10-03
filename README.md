# Justin Skills

Personal agent skills plus complete mirrored collections from Emil Kowalski,
Matt Pocock, and Caveman. Install only the focused packs you need so `/skills`
stays useful.

## Recommended setup

Keep a small router pack global, then install specialist packs per project:

```sh
# Once, globally
./scripts/install-pack.sh starter --global --yes

# Inside a frontend project
./scripts/install-pack.sh emil design animation --yes

# Inside an application/codebase project
./scripts/install-pack.sh matt-engineering code-discipline --yes
```

On Windows PowerShell, use `./scripts/install-pack.ps1` and the `-Global` and
`-Yes` switches. This is more effective than nesting skill directories: the
agent's `/skills` view reflects what is installed, not the visual layout of the
source repository.

## One catalog across devices and agents

Treat this Git repository and `packs.json` as the catalog for the skills you
choose to manage. Clone or pull it on each device, then run the same pack
selection there. The repository is the source; installed folders are copies.

For a preview that does not change your configuration:

```sh
python scripts/audit-local-skills.py > skill-inventory.json
python scripts/sync-local-skills.py starter --target agents --target claude
```

To install missing skills from this exact checkout:

```sh
python scripts/sync-local-skills.py starter --target agents --target claude --apply
```

The sync script reports `CONFLICT` for an existing skill it does not manage or
one changed locally. It updates its own unchanged copies after `git pull`,
keeping the prior version under `~/.justin-skills/backups/`. It accepts multiple
pack names and deduplicates their union. Python 3 is required.

`~/.agents/skills` is the shared global target for Codex and other agents that
read the Agent Skills directory. Claude Code also uses `~/.claude/skills`.
Antigravity's global config target can be included with `--target antigravity`
(`~/.gemini/config/skills`). Before adding the same skill to both `agents` and
`antigravity`, check whether your installed Antigravity version already reads
`~/.agents/skills`; otherwise it may show the name twice. Conductor and Paseo
run underlying agents, so install to those agents' skill locations on each host.
Paseo's own orchestration skills are managed in Paseo settings.

Keep built-in and plugin-provided skills in their own tool or plugin. A matching
name in this catalog does not mean its installed copy is safe to replace.
Use the audit's hashes to review such collisions first.

## Install individual skills

Use the [Skills CLI](https://github.com/vercel-labs/skills) from the repository
where you want the skills:

```sh
npx skills add Cadastrophi/justin-skills
npx skills add Cadastrophi/justin-skills --skill tdd diagnosing-bugs --agent codex --yes
npx skills add Cadastrophi/justin-skills --list
```

Add `--global` only for skills useful in almost every repository.

## Packs

Definitions live in [`packs.json`](packs.json). Packs may overlap; the install
scripts deduplicate their union.

| Pack | Scope |
| --- | --- |
| `starter` | Five global-friendly routers and concise-mode helpers. |
| `emil` | Complete `emilkowalski/skills` collection. |
| `matt-engineering` | Stable engineering workflows from Matt Pocock. |
| `matt-productivity` | Stable interview, handoff, teaching, and writing workflows. |
| `matt-misc` | Stable setup and migration utilities. |
| `matt-experimental` | Matt Pocock's in-progress skills, kept separate on purpose. |
| `matt` | Complete Matt Pocock collection. |
| `caveman-core` | Concise communication, review, commit, help, and compression. |
| `caveman-cloud` | Caveman gateway, evidence, and optimization workflows. |
| `code-discipline` | Generic focused-build, diagnosis, migration, refactor, and verification patterns. |
| `caveman-all` | Complete Caveman collection. |
| `design` | Personal visual design and frontend taste toolkit. |
| `animation` | Focused motion design subset. |
| `graphics` | Image-to-3D and procedural Three.js. |
| `slides` | PowerPoint plus selected design guidance. |
| `legal` | Privacy-policy drafting and structured legal-risk assessment. |
| `personal-workflows` | Locally curated documentation, discovery, and implementation helpers. |
| `all` | Every skill; expect a crowded `/skills` list. |

### Install a pack

```sh
git clone https://github.com/Cadastrophi/justin-skills.git ~/justin-skills
cd ~/justin-skills

# macOS / Linux / Git Bash
scripts/install-pack.sh matt-engineering code-discipline --yes
scripts/install-pack.sh --list

# Windows PowerShell
./scripts/install-pack.ps1 matt-engineering code-discipline -Yes
./scripts/install-pack.ps1 -List
```

The scripts call `npx skills add` with an explicit, deduplicated skill list.
The shell script requires `jq`; the PowerShell version has no extra dependency.
Both require Node.js.

## Repository layout

- `skills/<declared-name>/` contains one discoverable skill and all its assets.
- `packs.json` provides installation profiles without hiding skills from the CLI.
- `SOURCES.md` records upstream revisions and collision decisions.
- `licenses/` preserves upstream licenses.
- `scripts/validate-skills.py` rejects duplicate names, folder/name mismatches,
  missing pack entries, and ungrouped skills.

Run validation before publishing:

```sh
python scripts/validate-skills.py
```

Installation copies skill instructions; it does not run the workflows, change
project settings, create branches, or configure Matt Pocock's skills. Run
`/setup-matt-pocock-skills` once in repositories that use his engineering pack.

## Sources

The three complete imported collections and their pinned revisions are listed
in [`SOURCES.md`](SOURCES.md). Other retained skills preserve the original
sources previously documented by this repository, including Vercel Labs,
Impeccable, Anthropic, and local project-specific skills.
