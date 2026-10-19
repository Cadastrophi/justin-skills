---
name: jww-swift-style
description: Style Swift code for JWW projects. Use when generating, editing, or reviewing application, package, extension, or test code that must match Justin's conventions; do not use for non-Swift work or as a substitute for platform-specific implementation skills.
---

# JWW Swift Style

**The primary rule: generate code that looks as though it belongs beside the code being changed.** The nearest surrounding Swift source and the applicable `AGENTS.md` are the final authority. Everything below is the default only where the surrounding code is silent — chiefly new top-level files.

## Inputs and Output

- Take as inputs the target Swift file or diff, a nearby comparable source file, and every applicable `AGENTS.md`.
- Produce a minimal Swift edit or style review that matches those local conventions. State the validation performed when making an edit.

## Before Writing

1. Read the target file and a nearby comparable file. Read each applicable nested `AGENTS.md`.
2. Preserve existing structure, import ordering, access-control style, and all `MARK` and section dividers. Do not perform unrelated formatting or style cleanup.
3. Select APIs appropriate to the target platform and module. Keep shared code compatible with every platform the module supports unless narrow platform conditionals are required.

## Source Layout

- Use four-space indentation and blank lines to group declarations and logical steps.
- Use the applicable SwiftLint `line_length` setting for the line-length limit; default to 150 characters when no limit is configured. Follow an explicit repository override, including a disabled `line_length` rule.
- Match Xcode’s Control-I (Re-Indent) output for indentation and continuation alignment using the project’s indentation settings. Apply this to calls, declarations, conditions, chains, and closures; follow the wrapping examples for line-break placement.
- Add sections to substantial types only when the repository already uses the divider style shown below. Match the neighboring files exactly: some use only the `// MARK:` line, others follow it with the box comment. Keep existing section names and ordering when extending a type.

```swift
// MARK: View Lifecycle
// ====================================
// View Lifecycle
// ====================================
```

- Use the same divider at file scope for extension files when it matches neighboring files, with the contextual section name.
- For new top-level files, prefer one primary type. Do not split existing files solely for style; follow nearby grouping conventions for supporting types, extensions, and protocols.
- Prefer separate extensions or files for distinct protocol responsibilities when that matches neighboring code.
- Name focused extension files `Type+Purpose.swift` when creating a new file. Group related extensions by subject when the surrounding module already does so.
- Keep initializers, lifecycle methods, actions/delegate methods, and private conveniences in the local order. Put simple stored properties before those sections.
- Follow the enclosing file's `self.` convention. In view-controller code, use explicit `self.` consistently where the file does; do not add or remove it globally.
- When the SwiftLint configuration defines `always_on_same_line` or `always_on_line_above`, follow those rules. Otherwise, put `@available`, `@Test`, `@ViewBuilder`, and `@Model` on the line above their declaration. Keep property-wrapper attributes on the same declaration and follow local wrapping when a declaration would exceed configured limits.
- Match local wrapping and configured line-length limits; do not reflow unrelated code. When wrapping is ambiguous, read [references/line-wrapping.md](references/line-wrapping.md) for examples. Follow the repository's complexity limits, and use the smallest scoped `swiftlint:disable` only when a legitimate local exception remains.

## Naming, Access, and Documentation

- Use clear, idiomatic Swift names and explicit access levels consistent with the surrounding target. Keep implementation details `private` unless an interface requires wider access.
- Prefer `final` for non-subclassed reference types when that matches the type's role.
- Use `private(set)` when callers need observation but not mutation.
- Write English documentation comments for public/shared APIs and comments for intent or non-obvious platform constraints. Do not add comments that merely repeat the code, temporal labels, or LLM/process references.
- Preserve useful comments and `MARK` and section dividers. Update a comment only when it becomes inaccurate.

## Swift and Apple APIs

- Prefer standard Swift language features and platform frameworks already available to the deployment targets. Avoid introducing third-party dependencies for routine work.
- Use `guard` for required early exits and return promptly. Make expected failure handling explicit.
- Keep closures and asynchronous work readable; capture `self` weakly when a stored callback or lifecycle can retain a controller unnecessarily.
- Use `#if os(...)` or `#if targetEnvironment(...)` narrowly in shared code and preserve a consistent shared interface where practical.
- Match the local availability-check style. Do not alter deployment compatibility without an explicit requirement.

## Tests

- Follow the existing test file's framework and structure. For a new test in an XCTest target, use XCTest unless the target is actively migrating. Otherwise, prefer Swift Testing—`import Testing`, `@Test`, `#expect`, and `#require`.
- Keep tests focused, named for behavior, and use the repository's existing fixtures and helpers. Retain existing XCTest tests when not changing their behavior; do not migrate them merely for style.

## Final Check

Before presenting Swift code, reread the changed context and verify that it preserves dividers, local ordering, imports, visibility, platform boundaries, and relevant SwiftLint limits. When making an actual change, run the repository's targeted lint command when configured, plus the most relevant build or test verification.
