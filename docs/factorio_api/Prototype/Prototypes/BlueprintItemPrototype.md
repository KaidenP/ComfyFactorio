---
title: BlueprintItemPrototype
tags: [factorio-api, prototype]
---
# BlueprintItemPrototype

> **Parent:** [[SelectionToolPrototype]] · **Type name:** `blueprint`

A [blueprint](https://wiki.factorio.com/Blueprint).

## Properties

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
Whether the item will draw its label when held in the cursor in place of the item count.

### select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"blueprint"`.

The filters are parsed, but then ignored and forced to be empty.

### alt_select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"blueprint"`.

The filters are parsed, but then ignored and forced to be empty.

### always_include_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
This property is hardcoded to `false`.

### build_preview_tints
- **Type:** [[BuildPreviewTints (type)]]
- **Optional**
Tints of the building preview when this blueprint is held in the cursor. Every property is optional here, any that are not given use the color from [[UtilityConstants (prototype)#build_preview_tints|UtilityConstants::build_preview_tints]].

### draw_collision_indicators
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the [[UtilitySprites#buildability_collision|collision indicators]] are drawn over entities that collide with the building preview when this blueprint is held in the cursor.
