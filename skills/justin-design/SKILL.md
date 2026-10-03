---
name: justin-design
description: Design, build, or review production frontend interfaces with Apple-like clarity, restraint, material depth, and fluid interaction while avoiding generic AI-looking layouts. Use for websites, landing pages, dashboards, product UI, components, redesigns, or motion polish when the user wants clean, premium, distinctive visual craft. Not for backend-only work or literal cloning of Apple pages.
---

# Justin Design

Create interfaces that feel inevitable: clear at first glance, distinctive to the product, quiet where people need to work, and expressive where the surface needs to persuade.

Apple-like means clarity, hierarchy, spatial continuity, responsive feedback, careful typography, and restrained material depth. It does not mean copying Apple.com, using glass everywhere, or turning every product into a monochrome hardware launch.

## Authority

Resolve competing guidance in this order:

1. The user's explicit brief and supplied references.
2. Product truth, accessibility, and platform conventions.
3. The existing repository's design system, stack, and interaction patterns.
4. The surface mode and actual usage frequency.
5. The preferences in this skill.

Never replace factual copy, introduce unsupported claims, change product behavior, or add dependencies merely to satisfy an aesthetic preference. For a refinement, preserve the incumbent identity. For an explicit redesign, preserve product truth and function while allowing a new visual system.

## Start with a design read

Inspect the relevant implementation and assets before editing. Determine:

- surface: landing page, product UI, documentation, or portfolio/showcase;
- audience and the one job they need to complete;
- existing visual truth that should be preserved;
- desired emotional register;
- one memorable idea that belongs specifically to this product.

State a compact design read before implementation. If two materially different directions remain plausible, ask one focused question. Otherwise proceed.

Choose a mode:

- **Persuade:** marketing, landing, or pricing. Earn attention and action.
- **Operate:** dashboards, settings, editors, and workflows. Scanability and predictability outrank spectacle.
- **Read:** documentation and editorial surfaces. Structure for comprehension.
- **Experience:** portfolios and showcases. Let the work lead and make the interface recede.

## Visual direction

- Build the direction from the subject matter, audience, and brand rather than from a fashionable template.
- Establish a small token system for color, type, spacing, radius, elevation, and motion. Reuse existing tokens when present.
- Use typography as the primary hierarchy. Choose a characterful display face only when the product benefits from one; use a highly legible body face. System fonts are appropriate for native-feeling operational UI.
- Prefer one dominant neutral family and one intentional accent. Additional colors must encode content or state.
- Use asymmetry, overlap, or unusual composition only when it improves the story. Clean does not mean centered, empty, or identical.
- Use cards only for real grouping or elevation. Prefer spacing, alignment, and dividers for ordinary structure.
- Give each major section a distinct compositional job. Avoid repeating the same card grid or text-image split down the page.
- Use real product content and imagery. Never invent precise metrics, testimonials, customer logos, or capabilities.

## Anti-template filter

Reject unearned defaults:

- purple-on-white gradients, generic mesh glows, and gradient text;
- centered hero plus three equal icon cards as the whole page structure;
- glass, blur, grain, grids, or huge rounded rectangles used as decoration;
- excessive pills, badges, section numbers, uppercase eyebrows, or monospace used as a technology costume;
- fake dashboard screenshots made from meaningless rectangles;
- generic headings, inflated copy, vague errors, or clever labels that obscure the action;
- identical entrance animations on every section;
- a visual idea borrowed from the last project rather than earned by this one.

A brief may legitimately require one of these devices. When it does, execute it deliberately and consistently rather than reflexively.

## Apple-like interaction

- Feedback begins on pointer-down and stays continuous during direct manipulation.
- Dragged elements track the pointer from the grabbed offset. Use rubber-banding at boundaries rather than a hard stop.
- Gesture-driven motion must be interruptible, start from the current presentation value, and carry velocity into its destination.
- Use critically damped or lightly damped springs for drag, swipe, sheet, and spatial transitions. Use short ease-out transitions for ordinary non-gesture UI.
- Do not animate frequent keyboard actions. Do not block input while animation completes.
- Enter and exit along spatially consistent paths. Popovers originate from their trigger; centered modals may originate from the center.
- Add motion only for feedback, hierarchy, explanation, or state continuity. One authored moment is stronger than scattered effects.
- Honor `prefers-reduced-motion`. Reduced motion preserves state understanding with fades, instant transitions, or shorter travel.
- Animate transforms and opacity where possible; measure performance on realistic content and devices.

## Product-quality floor

Ship the whole interaction, not a beauty shot:

- real responsive behavior at narrow mobile and desktop widths;
- visible keyboard focus, semantic controls, readable contrast, and usable touch targets;
- loading, empty, error, disabled, hover, active, and success states when applicable;
- clear user-facing names, active voice, and recovery-oriented error copy;
- no horizontal overflow, clipped text, unstable viewport height, or layout shift from unreserved media;
- no new library until the existing dependencies and native platform capabilities are checked.

For implementation work, render and inspect desktop and mobile together in one bounded pass, fix the observed defects, confirm once, and stop. Preserve unrelated code and avoid open-ended polishing.

## Deliver the result

Lead with the implemented outcome. Mention the chosen design direction, the signature decision, meaningful accessibility or responsive behavior, and what was verified. Call out missing real assets or unresolved product decisions plainly.

When the user wants help writing a request or deciding what information to provide, read [references/prompts.md](references/prompts.md).

## Sources of inspiration

This is a standalone synthesis informed by Apple interface principles, Emil Kowalski's interaction craft, anti-template design guidance from Taste and Impeccable, and Anthropic's `frontend-design` emphasis on subject-specific visual direction. These sources do not need to be installed for this skill to work.
