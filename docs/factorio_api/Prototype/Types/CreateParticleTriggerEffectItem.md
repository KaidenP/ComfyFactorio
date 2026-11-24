---
title: CreateParticleTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# CreateParticleTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"create-particle"`

### particle_name
- **Type:** [[ParticleID (type)]]

### initial_height
- **Type:** [[float (type)]]

### offset_deviation
- **Type:** [[SimpleBoundingBox (type)]]
- **Optional**

### show_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**

### tile_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**

### offsets
- **Type:** array<[[Vector (type)]]>
- **Optional**

### initial_height_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### initial_vertical_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### initial_vertical_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### speed_from_center
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### speed_from_center_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### frame_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### frame_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### movement_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### tail_length
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Silently capped to a maximum of 100.

### tail_length_deviation
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Silently capped to a maximum of 100.

### tail_width
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### rotate_offsets
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### only_when_visible
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Create the particle only when they are within a 200 tile range of any connected player.

### apply_tile_tint
- **Type:** [[ApplyTileTint (type)]]
- **Optional**

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{1, 1, 1, 1} (white)`
Only loaded if `apply_tile_tint` is not defined.
