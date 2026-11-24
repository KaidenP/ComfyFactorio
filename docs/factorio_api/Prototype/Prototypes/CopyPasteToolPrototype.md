---
title: CopyPasteToolPrototype
tags: [factorio-api, prototype]
---
# CopyPasteToolPrototype

> **Parent:** [[SelectionToolPrototype]] · **Type name:** `copy-paste-tool`

A copy-paste or cut-paste tool.

## Properties

### cuts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```

### always_include_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
This property is hardcoded to `false`.

### select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The filters are parsed, but then ignored and forced to be empty.

### alt_select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The filters are parsed, but then ignored and forced to be empty.
