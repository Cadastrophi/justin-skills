# Justin Skills

Personal agent skills plus complete mirrored collections from Emil Kowalski,
Matt Pocock, and Caveman. Install only the focused packs you need so `/skills`
stays useful.

## Recommended setup

Keep a small router pack global, then install specialist packs per project:

```sh
# Once, globally; repeat after git pull to add or update selected skills
python scripts/sync-local-skills.py starter --apply

# Inside a frontend project
./scripts/install-pack.sh emil design animation --yes

# Inside an application/codebase project
./scripts/install-pack.sh matt-engineering code-discipline --yes
```

On Windows PowerShell, use `./scripts/install-pack.ps1` and the `-Yes`
switch for project installs. The agent's `/skills` view reflects installed
paths, not the visual layout of the source repository.

## One catalog across devices and agents

Treat this Git repository and `packs.json` as the catalog for the skills you
choose to manage. Clone it **once per device outside any scanned skills
directory**. A clone is only a source checkout, so it does not add entries to
`/skills`. Later, `git pull` transfers Git's changes into that same checkout;
do not clone again to update it.

For a preview that does not change your configuration:

```sh
python scripts/audit-local-skills.py > skill-inventory.json
python scripts/sync-local-skills.py starter
```

To install missing skills from this exact checkout:

```sh
git pull
python scripts/sync-local-skills.py starter --apply
```

The sync script installs one real copy in `~/.agents/skills` and links
`~/.claude/skills` to that copy (a junction on Windows). Repeated runs skip
unchanged skills, install newly selected skills, and update previously managed
copies when the repository changes. It keeps replaced versions under
`~/.justin-skills/backups/`. An identical existing Claude copy is backed up
and converted to a link; a differing copy reports `CONFLICT` for review.
Existing same-name skills in `~/.codex/skills` block a new shared install so
Codex does not discover both. The script accepts multiple pack names and
deduplicates their union. Python 3 is required.

`~/.agents/skills` is the shared global target for Codex and other agents that
read the Agent Skills directory. Claude Code also uses `~/.claude/skills`.
Only add `--target antigravity` if that installation does not already read
`~/.agents/skills`; it creates a link in `~/.gemini/config/skills`. If
Antigravity scans both paths, even a link can appear twice in its menu.
Conductor and Paseo run underlying agents, so use the underlying agent's
skill location on each host. Paseo's own orchestration skills are managed in
Paseo settings.

Use this sync command as the single global installation method for these
skills. Running `npx skills add` or the pack installer globally as well can
create another discovered path for the same skill. Project-specific installs
remain useful when they are intentionally scoped to one project.

Keep built-in and plugin-provided skills in their own tool or plugin. A matching
name in this catalog does not mean its installed copy is safe to replace.
Use the audit's hashes to review such collisions first.

The [skill catalog](docs/skill-catalog.md) and [CSV version](docs/skill-catalog.csv)
list the distinct skills found during the 3 October 2026 local inventory, with
one-line usage guidance and suggested configuration scope. They are a dated
snapshot; re-audit a device before making cleanup decisions from it.

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
