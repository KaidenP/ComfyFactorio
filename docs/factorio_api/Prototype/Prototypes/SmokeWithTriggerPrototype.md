---
title: SmokeWithTriggerPrototype
tags: [factorio-api, prototype]
---
# SmokeWithTriggerPrototype

> **Parent:** [[SmokePrototype]] · **Type name:** `smoke-with-trigger`

An entity with animation and a trigger.

## Properties

### action
- **Type:** [[Trigger]]
- **Optional**

### action_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
0 means never apply.

### particle_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`

### particle_distance_scale_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### spread_duration_variation
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### particle_duration_variation
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### particle_spread
- **Type:** [[Vector (type)]]
- **Optional**

### particle_scale_factor
- **Type:** [[Vector (type)]]
- **Optional**

### wave_distance
- **Type:** [[Vector (type)]]
- **Optional**

### wave_speed
- **Type:** [[Vector (type)]]
- **Optional**

### attach_to_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, causes the smoke to move with the target entity if one is specified.

### fade_when_attachment_is_destroyed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, the smoke will immediately start fading away when the entity it is attached to is destroyed. If it was never attached to an entity in the first place, then the smoke will fade away immediately after being created.
