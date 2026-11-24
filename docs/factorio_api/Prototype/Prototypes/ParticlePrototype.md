---
title: ParticlePrototype
tags: [factorio-api, prototype]
---
# ParticlePrototype

> **Parent:** [[Prototype]] · **Type name:** `optimized-particle`

An entity with a limited lifetime that can use trigger effects.

## Properties

### pictures
- **Type:** [[AnimationVariations]]
- **Optional**
Picture variation count and individual frame count must be equal to shadow variation count.

### life_time
- **Type:** [[uint16 (type)]]
Can't be 1.

### shadows
- **Type:** [[AnimationVariations]]
- **Optional**
Shadow variation variation count and individual frame count must be equal to picture variation count.

### draw_shadow_when_on_ground
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### regular_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### ended_in_water_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### ended_on_ground_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### render_layer_when_on_ground
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`

### regular_trigger_effect_frequency
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Can't be 1.

### movement_modifier_when_on_ground
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.8`

### movement_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### vertical_acceleration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.004`
Has to be >= -0.01 and <= 0.01.

### mining_particle_frame_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### fade_away_duration
- **Type:** [[uint16 (type)]]
- **Optional**
Defaults to `life_time` / 5, but at most 60. If this is 0, it is silently changed to 1.
