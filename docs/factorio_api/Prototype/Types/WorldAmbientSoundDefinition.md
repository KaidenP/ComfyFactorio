---
title: WorldAmbientSoundDefinition
tags: [factorio-api, prototype, type]
---
# WorldAmbientSoundDefinition

## Type

struct | [[Sound]]

## Properties

### sound
- **Type:** [[Sound]]
- **Optional**

### radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `10`

### min_entity_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `5`
Has to be less than or equal to `max_entity_count`.

### max_entity_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `15`

### entity_to_sound_ratio
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.2`

### average_pause_seconds
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
