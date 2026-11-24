---
title: ArtilleryFlarePrototype
tags: [factorio-api, prototype]
---
# ArtilleryFlarePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `artillery-flare`

The entity spawned by the [artillery targeting remote](https://wiki.factorio.com/Artillery_targeting_remote).

## Properties

### pictures
- **Type:** [[AnimationVariations]]
- **Optional**
Picture variation count and individual frame count must be equal to shadow variation count.

### life_time
- **Type:** [[uint16 (type)]]

### shadows
- **Type:** [[AnimationVariations]]
- **Optional**
Shadow variation variation count and individual frame count must be equal to picture variation count.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### render_layer_when_on_ground
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`

### regular_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### regular_trigger_effect_frequency
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### ended_in_water_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### movement_modifier_when_on_ground
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.8`

### movement_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### creation_shift
- **Type:** [[Vector (type)]]
- **Optional**

### initial_speed
- **Type:** [[Vector (type)]]
- **Optional**

### initial_height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### initial_vertical_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### initial_frame_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### shots_per_flare
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many artillery shots should be fired at the position of this flare.

### early_death_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `180`
How long this flare stays alive after `shots_per_flare` amount of shots have been shot at it.

### shot_category
- **Type:** [[AmmoCategoryID (type)]]
- **Optional**
Only artillery turrets/wagons whose ammo's [[AmmoItemPrototype#ammo_category|ammo_category]] matches this category will shoot at this flare. Defaults to all ammo categories being able to shoot at this flare.

### map_color
- **Type:** [[Color (type)]]
- **Overrides parent**

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
