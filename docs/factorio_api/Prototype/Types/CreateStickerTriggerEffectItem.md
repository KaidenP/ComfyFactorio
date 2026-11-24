---
title: CreateStickerTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# CreateStickerTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"create-sticker"`

### sticker
- **Type:** [[EntityID (type)]]
Name of a [[StickerPrototype]] that should be created.

### show_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**

### trigger_created_entity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, [[on_trigger_created_entity]] will be triggered when the sticker is created.
