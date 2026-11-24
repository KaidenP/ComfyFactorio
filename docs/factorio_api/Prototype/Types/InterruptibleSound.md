---
title: InterruptibleSound
tags: [factorio-api, prototype, type]
---
# InterruptibleSound

## Properties

### sound
- **Type:** [[Sound]]
- **Optional**
At least one of sound and stopped_sound has to be defined.

### minimal_change_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### stopped_sound
- **Type:** [[Sound]]
- **Optional**
At least one of sound and stopped_sound has to be defined.

### minimal_sound_duration_for_stopped_sound
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `1`
Has to be greater or equal to `1`.

### fade_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
