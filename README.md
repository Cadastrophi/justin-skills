# Justin Skills

Personal agent skills, installable into other repositories with the [Skills CLI](https://github.com/vercel-labs/skills).

On the source Mac, the personal collection lives at `~/.agents/skills`.
`~/.codex/skills` and several other agent directories may contain synchronized
copies; this repository is the portable copy for other devices.

## Install

Run from the repository where you want to use the skills:

```sh
npx skills add Cadastrophi/justin-skills
```

Choose the skills and agents interactively, or install selected skills for Codex:

```sh
npx skills add Cadastrophi/justin-skills --skill junior-dev capture-intent-docs --agent codex --yes
```

Add `--global` to make them available across repositories on your machine. To inspect the collection without installing:

```sh
npx skills add Cadastrophi/justin-skills --list
```

## Packs

Instead of picking skills one at a time, install a named bundle. Definitions live in [`packs.json`](packs.json).

| Pack | What's in it |
| --- | --- |
| `design` | Taste, brand systems, UI direction, and aesthetic vocabularies (apple-design, emil-design-eng, taste-skill, brandkit, shadcn-ui, awesome-design-md, pptx, and more). |
| `animation` | Motion craft: animate, animate-expo, animation-vocabulary, review/improve/find-animation-opportunities, ask-sonner. |
| `3d` | img2threejs (image → procedural Three.js). |
| `swe` | junior-dev, impeccable, prototype, write-swift. |
| `research` | capture-intent-docs, grill-with-docs, find-skills. |
| `slides` | Curated slice for building a strong slide deck (pptx + taste + brand refs + shadcn-ui). |
| `all` | Everything. |

### Install a pack

Clone the repo first (packs are driven by scripts in it), then run:

```sh
git clone https://github.com/Cadastrophi/justin-skills.git ~/justin-skills
cd ~/justin-skills

# macOS / Linux / Git Bash
scripts/install-pack.sh design --global --yes
scripts/install-pack.sh slides swe --global --yes   # union of two packs
scripts/install-pack.sh --list                      # show every pack

# Windows PowerShell
./scripts/install-pack.ps1 design -Global -Yes
./scripts/install-pack.ps1 slides swe -Global -Yes
./scripts/install-pack.ps1 -List
```

The scripts resolve pack → skill list and shell out to `npx skills add Cadastrophi/justin-skills --skill …`. Drop `--global` / `-Global` to install into the current repo instead of your machine.

`scripts/install-pack.sh` requires `jq`; the PowerShell version has no extra dependencies. Both need Node.js (for `npx`).

## Included skills

| Skill | Purpose | Repository expectations |
| --- | --- | --- |
| [animate](skills/animate/SKILL.md) | Build considered web animations. | Framework-agnostic; inspect the host project's motion and token conventions. |
| [animate-expo](skills/animate-expo/SKILL.md) | Build fluid React Native and Expo animations. | Requires an Expo/React Native project when the implementation is used. |
| [animation-vocabulary](skills/animation-vocabulary/SKILL.md) | Name an animation or motion pattern from a description. | Read-only guidance; no project-specific setup. |
| [apple-design](skills/apple-design/SKILL.md) | Apply Apple's principles for fluid, physical interfaces. | Adapt the guidance to the host platform and existing design system. |
| [ask-sonner](skills/ask-sonner/SKILL.md) | Integrate and troubleshoot Sonner toasts. | Requires a React project using Sonner. |
| [emil-design-eng](skills/emil-design-eng/SKILL.md) | Apply Emil Kowalski's design-engineering principles. | Read-only guidance unless paired with an implementation request. |
| [find-animation-opportunities](skills/find-animation-opportunities/SKILL.md) | Identify UI interactions that would benefit from motion. | Read-only audit; does not implement changes. |
| [find-skills](skills/find-skills/SKILL.md) | Discover and install skills. | Requires the Skills CLI for installation. |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Interview a plan or design and capture decisions. | Calls the grilling and domain-modeling skills when invoked. |
| [impeccable](skills/impeccable/SKILL.md) | Design, redesign, critique, and polish frontend interfaces. | Follow its project-context and visual-verification workflow. |
| [improve-animations](skills/improve-animations/SKILL.md) | Audit existing motion and produce implementation plans. | Read-only audit; does not implement changes. |
| [junior-dev](skills/junior-dev/SKILL.md) | Implement small changes in isolated worktrees and publish draft pull requests. | Written for Vellum: uses `origin/dev`, draft PRs into `dev`, and Vellum architecture and validation commands. Adapt those conventions before using it in a different project. |
| [capture-intent-docs](skills/capture-intent-docs/SKILL.md) | Record agreed product behavior, with explicit approval before writing intent documents. | Uses `docs/README.md` as the documentation guide and template, with `docs/pages/` and `docs/features/`. |
| [pick-ui-library](skills/pick-ui-library/SKILL.md) | Choose a frontend library for a specific UI problem. | Recommendations should be checked against the host project's stack and constraints. |
| [pptx](skills/pptx/SKILL.md) | Create and edit PowerPoint presentations. | Requires the supporting scripts and a presentation task. |
| [prototype](skills/prototype/SKILL.md) | Build multiple genuinely different UI variants behind a visual picker. | Requires a runnable frontend surface for visual comparison. |
| [review-animations](skills/review-animations/SKILL.md) | Review motion implementation against a high craft bar. | Read-only review of existing code or a diff. |
| [write-swift](skills/write-swift/SKILL.md) | Write and review modern Swift, including concurrency. | Requires a Swift project for implementation work. |

Installation copies the skill instructions; it does not create branches, change project settings, or run the workflows. The original instructions and supporting files are preserved.

## Sources

- `animate`, `animate-expo`, `animation-vocabulary`, `apple-design`, `ask-sonner`, `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `pick-ui-library`, `prototype`, `review-animations`, and `write-swift`: [emilkowalski/skills](https://github.com/emilkowalski/skills).
- `find-skills`: [vercel-labs/skills](https://github.com/vercel-labs/skills).
- `grill-with-docs`: [mattpocock/skills](https://github.com/mattpocock/skills).
- `impeccable`: [pbakaus/impeccable](https://github.com/pbakaus/impeccable).
- `pptx`: [anthropics/skills](https://github.com/anthropics/skills).
- `junior-dev`: [Cadastrophi/junior-dev](https://github.com/Cadastrophi/junior-dev), revision `28f483be150594701e73232651cf604291e55b53`.
- `capture-intent-docs`: Vellum's `.agents/skills/capture-intent-docs`, revision `9ceed7a`.

The newly added skills are mirrored from the personal `~/.agents/skills`
collection so they can be installed on another device without adding anything
to a project repository. Upstream skill files and supporting assets are
preserved; review their source repositories for the applicable license and
attribution terms.
