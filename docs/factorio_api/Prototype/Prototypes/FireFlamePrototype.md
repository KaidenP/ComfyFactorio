---
title: FireFlamePrototype
tags: [factorio-api, prototype]
---
# FireFlamePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `fire`

A fire.

## Properties

### damage_per_tick
- **Type:** [[DamageParameters (type)]]

### spread_delay
- **Type:** [[uint32 (type)]]

### spread_delay_deviation
- **Type:** [[uint32 (type)]]

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### initial_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### secondary_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### small_tree_fire_pictures
- **Type:** [[AnimationVariations]]
- **Optional**

### pictures
- **Type:** [[AnimationVariations]]
- **Optional**

### smoke_source_pictures
- **Type:** [[AnimationVariations]]
- **Optional**

### secondary_pictures
- **Type:** [[AnimationVariations]]
- **Optional**

### burnt_patch_pictures
- **Type:** [[SpriteVariations]]
- **Optional**

### secondary_picture_fade_out_start
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### secondary_picture_fade_out_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `30`

### spawn_entity
- **Type:** [[EntityID (type)]]
- **Optional**

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**

### maximum_spread_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `200`

### initial_flame_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Spawns this many `secondary_pictures` around the entity when it first spawns. It waits `delay_between_initial_flames` between each spawned `secondary_pictures`. This can be used to make fires look less repetitive.

For example, spitters use this to make several smaller splashes around the main one.

### uses_alternative_behavior
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `false`, then all animations loop. If `true`, they run once and stay on the final frame. Also changes the behavior of several other fire properties as mentioned in their descriptions.

For example, spitters use alternate behavior, flamethrower flames don't.

### limit_overlapping_particles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### tree_dying_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### fade_in_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `30`

### fade_out_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `30`

### initial_lifetime
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `300`

### damage_multiplier_decrease_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### damage_multiplier_increase_per_added_fuel
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### maximum_damage_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### lifetime_increase_by
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `20`

### lifetime_increase_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`

### maximum_lifetime
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Max uint32

### add_fuel_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`

### delay_between_initial_flames
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`

### smoke_fade_in_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `30`

### smoke_fade_out_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `30`

### on_fuel_added_action
- **Type:** [[Trigger]]
- **Optional**

### on_damage_tick_effect
- **Type:** [[Trigger]]
- **Optional**

### light
- **Type:** [[LightDefinition]]
- **Optional**

### light_size_modifier_per_flame
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### light_size_modifier_maximum
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_alpha_blend_duration
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### burnt_patch_lifetime
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1800`

### burnt_patch_alpha_default
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_alpha
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `uses_alternative_behavior` is true.

### particle_alpha_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `uses_alternative_behavior` is true.

### flame_alpha
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `uses_alternative_behavior` is false.

### flame_alpha_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `uses_alternative_behavior` is false.

### burnt_patch_alpha_variations
- **Type:** array<[[TileAndAlpha]]>
- **Optional**

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
