---
title: GiveItemModifier
tags: [factorio-api, prototype, type]
---
# GiveItemModifier

> **Parent:** [[BaseModifier]]

Note that when any technology prototype changes (regardless of which mod it belongs to), the game re-applies all researched technology effects, including `"give-item"` modifiers. This means that players will receive the item again, even if they already received it previously. This can be undesirable.

## Properties

### type
- **Type:** `"give-item"`

### use_icon_overlay_constant
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `false`, do not draw the small "constant" icon over the technology effect icon.

### item
- **Type:** [[ItemID (type)]]

### quality
- **Type:** [[QualityID (type)]]
- **Optional**
- **Default:** `"normal"`

### count
- **Type:** [[ItemCountType (type)]]
- **Optional**
- **Default:** `1`
Must be >= `1`.
