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

- `justin-design`: [Cadastrophi/justin-design-skill](https://github.com/Cadastrophi/justin-design-skill), revision `76cee9dd85e4dae277f1085827018d43bc69cf26`; copied with its `agents/openai.yaml` and `references/prompts.md` files. The imported revision has no license file.
- `find-skills`: [vercel-labs/skills](https://github.com/vercel-labs/skills)
- `impeccable`: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- `pptx`: [anthropics/skills](https://github.com/anthropics/skills)
- `junior-dev`: [Cadastrophi/junior-dev](https://github.com/Cadastrophi/junior-dev), revision `28f483be150594701e73232651cf604291e55b53`
- `capture-intent-docs`: Vellum's `.agents/skills/capture-intent-docs`, revision `9ceed7a`

## Legal policy and review imports

Selected skills, not complete collections:

| Skill | Source path | Pinned revision | License |
| --- | --- | --- | --- |
| `privacy-policy` | [phuryn/pm-skills: pm-toolkit/skills/privacy-policy](https://github.com/phuryn/pm-skills/tree/8607e3b077817f89bf4a9b623246219734ac3be0/pm-toolkit/skills/privacy-policy) | `8607e3b077817f89bf4a9b623246219734ac3be0` | MIT, `licenses/phuryn-pm-skills-LICENSE` |
| `legal-risk-assessment` | [anthropics/knowledge-work-plugins: legal/skills/legal-risk-assessment](https://github.com/anthropics/knowledge-work-plugins/tree/da38ec1ee89d41e5380e652a97382695003396e7/legal/skills/legal-risk-assessment) | `da38ec1ee89d41e5380e652a97382695003396e7` | Apache-2.0, `licenses/anthropic-knowledge-work-plugins-LICENSE` |

Imported unchanged into the `legal` pack. These are drafting/review aids, not legal authority. In particular, the privacy template's shorthand about GDPR consent and CCPA applicability must be checked against current primary sources and the user's actual circumstances; do not treat consent as the only lawful basis or assume every California-facing business is CCPA-covered. Keep internal review markers out of final customer-facing copy and do not invent missing operational commitments.
