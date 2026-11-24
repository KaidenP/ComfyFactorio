---
title: PlaySoundTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# PlaySoundTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"play-sound"`

### sound
- **Type:** [[Sound]]

### min_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Negative values are silently clamped to 0.

### max_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** 1e21
Negative values are silently clamped to 0.

### play_on_target_position
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
