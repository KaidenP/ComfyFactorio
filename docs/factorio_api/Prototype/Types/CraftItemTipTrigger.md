---
title: CraftItemTipTrigger
tags: [factorio-api, prototype, type]
---
# CraftItemTipTrigger

> **Parent:** [[CountBasedTipTrigger]]

## Properties

### type
- **Type:** `"craft-item"`

### item
- **Type:** [[ItemID (type)]]
- **Optional**

### event_type
- **Type:** `"crafting-of-single-item-ordered"` | `"crafting-of-multiple-items-ordered"` | `"crafting-finished"`

### consecutive
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Can only be used when `event_type` is `"crafting-finished"`.
