# Upstream sources

The imported directories are flattened under `skills/` so the Skills CLI can
discover them consistently. The named packs in `packs.json` retain source and
stability boundaries without requiring every skill to be installed.

| Source | Imported revision | Local pack |
| --- | --- | --- |
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | `d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7` | `emil` |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `3cca18b368ae95cdbdebbff572ccafa662551015` | `matt` |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | `15581d14007fd01fb3f132016741962f34936ca2` | `caveman-all` |

## Collision policy

- Identical existing copies were refreshed in place, not duplicated.
- Matt Pocock's engineering `prototype` keeps the canonical `prototype` name
  because the rest of his workflow refers to it.
- Emil Kowalski's distinct UI-variant workflow is preserved as
  `emil-ui-prototype`.
- The obsolete local `design-taste-frontend-v1` copy was removed; the current
  `design-taste-frontend` skill remains.
- Legacy folder names were renamed to match each skill's declared YAML name.

Upstream licenses are preserved in `licenses/`.

## Other retained sources

- `find-skills`: [vercel-labs/skills](https://github.com/vercel-labs/skills)
- `impeccable`: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- `pptx`: [anthropics/skills](https://github.com/anthropics/skills)
- `junior-dev`: [Cadastrophi/junior-dev](https://github.com/Cadastrophi/junior-dev), revision `28f483be150594701e73232651cf604291e55b53`
- `capture-intent-docs`: Vellum's `.agents/skills/capture-intent-docs`, revision `9ceed7a`
