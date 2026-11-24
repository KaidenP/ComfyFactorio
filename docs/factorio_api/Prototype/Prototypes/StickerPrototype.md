---
title: StickerPrototype
tags: [factorio-api, prototype]
---
# StickerPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `sticker`

Entity that sticks to another entity, and damages/slows it. Stickers can only be attached to [[UnitPrototype]], [[CharacterPrototype]], [[CarPrototype]] and [[SpiderVehiclePrototype]].

## Properties

### duration_in_ticks
- **Type:** [[uint32 (type)]]
Must be > 0.

### animation
- **Type:** [[Animation]]
- **Optional**

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### damage_interval
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
Interval between application of `damage_per_tick`, in ticks.

### spread_fire_entity
- **Type:** [[EntityID (type)]]
- **Optional**
If this is given, this sticker is considered a "fire sticker" for some functions, such as [[BaseAttackParameters#fire_penalty|BaseAttackParameters::fire_penalty]] and [[EntityPrototypeFlags (type)#not_flammable|EntityPrototypeFlags::not-flammable]].

### fire_spread_cooldown
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `30`

### fire_spread_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### stickers_per_square_meter
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `15`

### force_visibility
- **Type:** [[ForceCondition (type)]]
- **Optional**
- **Default:** `"all"`

### single_particle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### use_damage_substitute
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### damage_per_tick
- **Type:** [[DamageParameters (type)]]
- **Optional**
Applied every `damage_interval` ticks, so may not necessarily be "per tick".

### target_movement_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Less than 1 to reduce movement speed, more than 1 to increase it.

### target_movement_modifier_from
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `target_movement_modifier`
The modifier value when the sticker is attached. It linearly changes over time to reach `target_movement_modifier_to`.

### target_movement_modifier_to
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `target_movement_modifier`
The modifier value when the sticker expires. It linearly changes over time starting from `target_movement_modifier_from`.

### target_movement_max
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-1`
The maximum movement speed for the target.

Negative values are ignored.

### target_movement_max_from
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `target_movement_speed`
The maximum movement speed for the target when the sticker is attached. It linearly changes over time to reach `target_movement_max_to`.

Negative values are ignored.

### target_movement_max_to
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `target_movement_speed`
The maximum movement speed for the target when the sticker expires. It linearly changes over time starting from `target_movement_max_from`.

Negative values are ignored.

### ground_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, causes the target entity to become "grounded", disabling flight. This only applies to Character entities wearing mech armor.

### vehicle_speed_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Less than 1 to reduce vehicle speed, more than 1 to increase it.

### vehicle_speed_modifier_from
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_speed_modifier`
Works similarly to `target_movement_modifier_from`.

### vehicle_speed_modifier_to
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_speed_modifier`
Works similarly to `target_movement_modifier_to`.

### vehicle_speed_max
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-1`
The maximum movement speed for vehicles.

Negative values are ignored.

### vehicle_speed_max_from
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_speed_max`
The maximum movement speed for vehicles when the sticker is attached. It linearly changes over time to reach `vehicle_speed_max_to`.

Negative values are ignored.

### vehicle_speed_max_to
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_speed_max`
The maximum movement speed for vehicles when the sticker expires. It linearly changes over time starting from `vehicle_speed_max_from`.

Negative values are ignored.

### vehicle_friction_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### vehicle_friction_modifier_from
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_friction_modifier`
Works similarly to `target_movement_modifier_from`.

### vehicle_friction_modifier_to
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `vehicle_friction_modifier`
Works similarly to `target_movement_modifier_to`.

### selection_box_type
- **Type:** [[CursorBoxType]]
- **Optional**
- **Default:** `"entity"`
Using this property marks the sticker as a "selection sticker", meaning that the selection box will be rendered around the entity when the sticker is on it.

### update_effects
- **Type:** array<[[TriggerEffectWithCooldown (type)]]>
- **Optional**
Effects (with cooldowns) to trigger every tick.

### hidden
- **Type:** `true`
- **Overrides parent**
The `hidden` property of stickers is hardcoded to `true`.

### hidden_in_factoriopedia
- **Type:** `true`
- **Overrides parent**
The `hidden_in_factoriopedia` property of stickers is hardcoded to `true`.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
