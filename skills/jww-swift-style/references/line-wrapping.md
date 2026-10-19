# Swift Line Wrapping

Use these examples when nearby code does not settle a wrapping decision.
Repository instructions, formatter settings, and surrounding code take
precedence. The snippets illustrate layout, not application behavior; their
supporting types and functions are omitted.

The examples below reflect Justin’s formatting preferences.

## Line-Length Limit

Use the applicable SwiftLint `line_length` setting; default to 150 characters
when no limit is configured. If warning and error thresholds differ, use the
warning threshold for wrapping. Respect explicit repository overrides,
including a disabled `line_length` rule. References to the limit below mean
this effective limit, not a fixed 150 characters.

## Alignment

For every example, match the indentation and continuation alignment produced
by Xcode’s Control-I (Re-Indent) command using the project’s indentation
settings. This applies to arguments, parameters, conditions, chained calls,
and closure bodies. Do not substitute a different manual alignment style.
The examples specify where to break lines; Control-I is the reference for
how those lines align.

## Calls That Fit on One Line

Keep a short call on one line when it fits the configured limit and matches
nearby code. Multiple arguments alone do not require wrapping.

```swift
let request = makeRequest(query: query, limit: 20)
```

## Longer Calls That Fit

Keep longer calls on one line when they fit the effective limit. Do not
wrap solely because a call has several arguments.

```swift
let request = makeRequest(query: searchQuery, sortOrder: selectedSortOrder, includeArchived: shouldIncludeArchived, limit: maximumResultCount)
```

## Function Declarations

Keep the parameter list, effects, return type, and opening brace on one line
when the declaration fits the limit.

```swift
func loadItems(matching query: String, sortOrder: SortOrder, limit: Int) async throws -> [Item] {
    try await store.fetch(query: query, sortOrder: sortOrder, limit: limit)
}
```

## Conditions

Keep the first condition beside `guard`, align subsequent conditions with it,
and put `else` on its own line.

```swift
guard let selectedItem = selection,
      selectedItem.isEditable,
      !isSaving
else {
    return
}
```

## Chained Calls

Keep the first transformation on the same line as the receiver. Indent
subsequent transformations one level.

```swift
let titles = items.filter { $0.isVisible }
    .map { $0.title }
    .sorted()
```

## Trailing Closures

Keep the arguments and opening trailing-closure declaration on one line when
they fit the limit. Indent the closure body one level.

```swift
loadItems(matching: searchQuery, limit: maximumResultCount) { result in
    updateResults(result)
}
```

## Declarations That Exceed the Limit

When a declaration exceeds the effective limit, keep the first parameter on the
declaration line and put each subsequent parameter on its own line. Align
subsequent parameters with the first parameter, matching Xcode’s Control-I
indentation. Keep the closing parenthesis, effects, return type, and opening
brace on the last parameter’s line.

```swift
func loadItems(matching query: String,
               sortOrder: SortOrder,
               includeArchived: Bool,
               maximumResultCount: Int,
               continuationToken: String?,
               preferredLanguageIdentifier: String) async throws -> [Item] {
    fatalError("Example body omitted")
}
```
