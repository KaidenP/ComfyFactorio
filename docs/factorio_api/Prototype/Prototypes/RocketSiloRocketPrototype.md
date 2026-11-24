---
title: RocketSiloRocketPrototype
tags: [factorio-api, prototype]
---
# RocketSiloRocketPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `rocket-silo-rocket`

The rocket inside the rocket silo.

## Properties

### shadow_slave_entity
- **Type:** [[EntityID (type)]]
- **Optional**

### cargo_pod_entity
- **Type:** [[EntityID (type)]]
Name of a [[CargoPodPrototype]].

### dying_explosion
- **Type:** [[EntityID (type)]]
- **Optional**

### glow_light
- **Type:** [[LightDefinition]]
- **Optional**

### rocket_sprite
- **Type:** [[Sprite]]
- **Optional**

### rocket_shadow_sprite
- **Type:** [[Sprite]]
- **Optional**

### rocket_glare_overlay_sprite
- **Type:** [[Sprite]]
- **Optional**

### rocket_smoke_bottom1_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_smoke_bottom2_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_smoke_top1_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_smoke_top2_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_smoke_top3_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_flame_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_flame_left_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_flame_right_animation
- **Type:** [[Animation]]
- **Optional**

### rocket_initial_offset
- **Type:** [[Vector (type)]]
- **Optional**

### rocket_rise_offset
- **Type:** [[Vector (type)]]

### cargo_attachment_offset
- **Type:** [[Vector (type)]]
- **Optional**

### rocket_flame_left_rotation
- **Type:** [[float (type)]]

### rocket_flame_right_rotation
- **Type:** [[float (type)]]

### rocket_render_layer_switch_distance
- **Type:** [[double (type)]]

### full_render_layer_switch_distance
- **Type:** [[double (type)]]

### rocket_launch_offset
- **Type:** [[Vector (type)]]

### effects_fade_in_start_distance
- **Type:** [[double (type)]]

### effects_fade_in_end_distance
- **Type:** [[double (type)]]

### shadow_fade_out_start_ratio
- **Type:** [[double (type)]]

### shadow_fade_out_end_ratio
- **Type:** [[double (type)]]

### rocket_visible_distance_from_center
- **Type:** [[float (type)]]

### rocket_above_wires_slice_offset_from_center
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-3`

### rocket_air_object_slice_offset_from_center
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-6`

### rocket_fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
- **Default:** `{rect={{-30, -30}, {30, rocket_above_wires_slice_offset_from_center}}, falloff=1}`

### rising_speed
- **Type:** [[double (type)]]

### engine_starting_speed
- **Type:** [[double (type)]]

### flying_speed
- **Type:** [[double (type)]]

### flying_acceleration
- **Type:** [[double (type)]]

### flying_trigger
- **Type:** [[TriggerEffect]]
- **Optional**

### flying_sound
- **Type:** [[Sound]]
- **Optional**

### inventory_size
- **Type:** [[ItemStackIndex (type)]]

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
