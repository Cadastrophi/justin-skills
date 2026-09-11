# Justin Skills

Personal agent skills, installable into other repositories with the [Skills CLI](https://github.com/vercel-labs/skills).

## Install

Run from the repository where you want to use the skills:

```sh
npx skills add Cadastrophi/justin-skills
```

Choose the skills and agents interactively, or install both skills for Codex:

```sh
npx skills add Cadastrophi/justin-skills --skill junior-dev capture-intent-docs --agent codex --yes
```

Add `--global` to make them available across repositories on your machine. To inspect the collection without installing:

```sh
npx skills add Cadastrophi/justin-skills --list
```

## Included skills

| Skill | Purpose | Repository expectations |
| --- | --- | --- |
| [junior-dev](skills/junior-dev/SKILL.md) | Implement small changes in isolated worktrees and publish draft pull requests. | Written for Vellum: uses `origin/dev`, draft PRs into `dev`, and Vellum architecture and validation commands. Adapt those conventions before using it in a different project. |
| [capture-intent-docs](skills/capture-intent-docs/SKILL.md) | Record agreed product behavior, with explicit approval before writing intent documents. | Uses `docs/README.md` as the documentation guide and template, with `docs/pages/` and `docs/features/`. |

Installation copies the skill instructions; it does not create branches, change project settings, or run the workflows. The original instructions and supporting files are preserved.

## Sources

- `junior-dev`: [Cadastrophi/junior-dev](https://github.com/Cadastrophi/junior-dev), revision `28f483be150594701e73232651cf604291e55b53`.
- `capture-intent-docs`: Vellum's `.agents/skills/capture-intent-docs`, revision `9ceed7a`.
