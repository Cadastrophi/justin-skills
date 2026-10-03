# Prompting Justin Design

Explicitly invoke `$justin-design` when visual quality is central. A strong request supplies product truth and constraints while leaving room for a coherent design decision.

## Useful input

Include what you know:

- **Surface:** route, component, or screen to build or refine.
- **Audience:** who uses it and in what setting.
- **Primary job:** the one action or understanding the surface must support.
- **Mode:** Persuade, Operate, Read, or Experience, if known.
- **Feel:** three to five qualities, plus qualities to avoid.
- **Keep/change:** existing behavior, copy, brand tokens, or components that are fixed.
- **References:** what to learn from each reference, not merely a URL or brand name.
- **Truth:** approved copy, product capabilities, metrics, and assets.
- **Technical constraints:** framework, dependencies, accessibility, performance, and supported breakpoints.
- **Acceptance:** observable behavior and visual checks that define done.

Do not prescribe every CSS value. Describe the product, desired effect, and constraints, then let the skill form a system.

## New landing page

```text
Use $justin-design to design and implement [route] for [product].

Audience: [who they are].
Primary action: [what they should do].
Feel: calm, precise, premium, and human. Take Apple's clarity and pacing as inspiration, but do not clone Apple.com or default to generic glassmorphism.
Avoid: purple gradients, repeated card grids, fake metrics, inflated marketing copy, and decorative motion.
Content/assets: [approved material and locations].
Constraints: preserve [stack/design system]; meet WCAG AA; support [viewports].
Signature idea: infer one visual or interactive moment from the product itself.
Implement the page, inspect mobile and desktop, fix observed defects, and report what you verified.
```

## Product dashboard or workflow

```text
Use $justin-design in Operate mode to refine [route/component].

Users need to [primary task] quickly and repeatedly. Preserve all behavior, data semantics, and existing design tokens. Make it feel clean and native through hierarchy, spacing, typography, immediate feedback, and excellent empty/error/loading states—not through spectacle.

Pay special attention to [dense table/form/navigation/mobile behavior]. Do not animate frequent keyboard actions. Verify keyboard access, contrast, touch targets, overflow, and narrow-screen behavior. Implement only changes supported by the current product truth.
```

## Existing-page redesign

```text
Use $justin-design to redesign [route]. First inspect the current implementation and identify what is product truth versus replaceable visual treatment.

Keep: [behavior, copy, assets, components].
Change: [visual identity or usability problems].
Direction: [qualities]. Reference [site/product] only for [specific principle], not for literal copying.
Avoid: [known dislikes].

State a one-sentence design read, implement a coherent replacement system, and verify it at [viewports]. Do not modify unrelated surfaces.
```

## Motion polish

```text
Use $justin-design to improve the interaction feel of [component]. The interaction occurs [frequency] and is triggered by [pointer/touch/keyboard].

Preserve behavior. Decide whether motion is justified. For gestures, require continuous 1:1 tracking, interruptibility, velocity handoff, and reduced-motion behavior. For ordinary UI, prefer short ease-out feedback. Test rapid reversal, repeated activation, keyboard use, and touch input.
```

## Design review only

```text
Use $justin-design to review [route/files] without editing. Evaluate whether the interface is specific to the product, visually coherent, usable in its real mode, accessible, responsive, and free of generic AI-design tells. Rank findings by user impact and distinguish correctness problems from optional taste improvements.
```

## Short prompt

```text
Use $justin-design on [target]. Audience: [audience]. Job: [primary job]. Feel: [three qualities]. Preserve: [constraints]. Avoid: [anti-goals]. Implement and verify mobile plus desktop.
```
