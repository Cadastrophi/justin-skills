---
name: shadcn-ui
description: Reference for shadcn/ui — an unstyled, copy-in React component library built on Radix + Tailwind. Use when adding, styling, or composing shadcn components; when starting a new Next.js/Vite/Astro/React-Router/TanStack app that should use shadcn; when picking a component for a UI (forms, dialogs, data tables, charts, sidebars, command palettes); or when the user references "shadcn", "shadcn/ui", or a specific component name from the list below.
---

# shadcn/ui

Copy-in component library. Components are added to `components/ui/` in your repo, not installed as a dep — you own and edit them. Built on Radix Primitives + Tailwind CSS + CVA. Not a runtime package: `shadcn` is the CLI that scaffolds files.

## Init a project

```bash
pnpm dlx shadcn@latest init -t [next|vite|tanstack-start|react-router|astro|laravel]
```

Requires Tailwind already configured. The init writes `components.json` (the config the CLI reads on every `add`) and drops shared files: `lib/utils.ts` (with `cn`), CSS variables for theming in `globals.css`, and the `components/ui/` folder.

For a fully-configured starter, point users at the web builder: <https://ui.shadcn.com/create>.

## Add a component

```bash
pnpm dlx shadcn@latest add <name>
```

- `<name>` is the slug from the table below (e.g. `alert-dialog`, `data-table`).
- Multiple names in one call are fine: `shadcn add button card dialog`.
- The command writes the component source into `components/ui/<name>.tsx` and installs any Radix/other deps it needs. Re-running an `add` overwrites — commit before re-adding.
- Import as `import { Button } from "@/components/ui/button"`.

## Components (76)

Base primitives: `accordion`, `alert`, `alert-dialog`, `aspect-ratio`, `avatar`, `badge`, `breadcrumb`, `button`, `button-group`, `calendar`, `card`, `carousel`, `checkbox`, `collapsible`, `combobox`, `command`, `context-menu`, `dialog`, `drawer`, `dropdown-menu`, `hover-card`, `input`, `input-group`, `input-otp`, `label`, `menubar`, `native-select`, `navigation-menu`, `pagination`, `popover`, `progress`, `radio-group`, `resizable`, `scroll-area`, `select`, `separator`, `sheet`, `sidebar`, `skeleton`, `slider`, `spinner`, `switch`, `table`, `tabs`, `textarea`, `toast`, `toggle`, `toggle-group`, `tooltip`, `typography`.

Composed / higher-level: `chart` (Recharts wrapper), `data-table` (TanStack Table wrapper), `date-picker` (Calendar + Popover), `form` (react-hook-form + zod bindings via `field`), `questionnaire`.

Chat / AI surfaces: `attachment`, `bubble`, `marker`, `message`, `message-scroller`, `item`, `empty`, `field`, `kbd`.

Utility / meta: `direction` (RTL), `native-select`.

Each has a live doc page at `https://ui.shadcn.com/docs/components/base/<slug>` — WebFetch that page when a component's props or composition pattern are needed.

## Theming

CSS variables in `globals.css` (`--background`, `--foreground`, `--primary`, `--muted`, `--accent`, `--border`, `--ring`, plus chart tokens). Dark mode via `class` strategy on `<html>`. Change palette by editing the variables — do NOT rewrite the components.

Prebuilt themes: <https://ui.shadcn.com/themes>. Preset generator: <https://ui.shadcn.com/create>.

## When Claude is working with shadcn

- Check `components.json` first — its `aliases`, `tsx` flag, and `style` field decide where new files land and their idiom.
- Before writing a component from scratch, check if a shadcn primitive already covers it. Prefer `add <name>` over rolling your own.
- To modify a shadcn component's behavior, edit the file in `components/ui/` directly. That's the intended workflow — there is no "eject."
- For a component's exact prop surface, fetch its doc page rather than guessing: `https://ui.shadcn.com/docs/components/base/<slug>`.
- The library is React only. Do not suggest it for Vue/Svelte/Solid — point at ports (`shadcn-vue`, `shadcn-svelte`, `shadcn-solid`) instead.

## Registry / MCP

shadcn ships an MCP server that exposes the registry to agents:

```bash
pnpm dlx shadcn@latest mcp
```

If the user wants Claude to query and install components without hard-coded names, offer to add this MCP to their Claude config.
