---
title: BlueprintBookPrototype
tags: [factorio-api, prototype]
---
# BlueprintBookPrototype

> **Parent:** [[ItemWithInventoryPrototype]] · **Type name:** `blueprint-book`

A [blueprint book](https://wiki.factorio.com/Blueprint_book).

## Properties

### inventory_size
- **Type:** [[ItemStackIndex (type)]] | `"dynamic"`
- **Overrides parent**
The inventory size of the item.

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```

### draw_label_for_cursor_render
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
If the item will draw its label when held in the cursor in place of the item count.
