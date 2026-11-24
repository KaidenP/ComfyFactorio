---
title: DeconstructionItemPrototype
tags: [factorio-api, prototype]
---
# DeconstructionItemPrototype

> **Parent:** [[SelectionToolPrototype]] · **Type name:** `deconstruction-item`

A [deconstruction planner](https://wiki.factorio.com/Deconstruction_planner).

## Properties

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```

### select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"deconstruct"`.

The filters are parsed, but then ignored and forced to be empty.

### alt_select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"cancel-deconstruct"`.

The filters are parsed, but then ignored and forced to be empty.

### always_include_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
This property is hardcoded to `false`.
