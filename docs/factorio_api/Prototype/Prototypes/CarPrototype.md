---
title: CarPrototype
tags: [factorio-api, prototype]
---
# CarPrototype

> **Parent:** [[VehiclePrototype]] · **Type name:** `car`

Entity with specialized properties for acceleration, braking, and turning.

## Properties

### animation
- **Type:** [[RotatedAnimation]]
- **Optional**
Animation speed 1 means 1 frame per tile.

### effectivity
- **Type:** [[double (type)]]
Modifies the efficiency of energy transfer from burner output to wheels.

### consumption
- **Type:** [[Energy]]

### rotation_speed
- **Type:** [[double (type)]]

### rotation_snap_angle
- **Type:** [[double (type)]]
Vehicle will snap the vertical, horizontal or diagonal axis if it's within this angle

### energy_source
- **Type:** [[BurnerEnergySource]] | [[VoidEnergySource]]

### turret_animation
- **Type:** [[RotatedAnimation]]
- **Optional**
Animation speed 1 means 1 frame per tile.

### light_animation
- **Type:** [[RotatedAnimation]]
- **Optional**
Must have the same frame count as `animation`.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### tank_driving
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car prototype uses tank controls to drive.

### auto_sort_inventory
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car prototype keeps the trunk inventory sorted.

### has_belt_immunity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car is immune to movement by belts.

### immune_to_tree_impacts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car gets damaged by driving over/against [[TreePrototype|trees]].

### immune_to_rock_impacts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car gets damaged by driving over/against [[SimpleEntityPrototype#count_as_rock_for_filtered_deconstruction|rocks]].

### immune_to_cliff_impacts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If this car gets damaged by driving against [[CliffPrototype|cliffs]].

### immune_to_all_impacts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this car gets damaged by driving into anything.

### turret_rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.01`

### turret_return_timeout
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `60`
Timeout in ticks specifying how long the turret must be inactive to return to the default position.

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
Size of the car inventory.

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`
If set to 0 then the car will not have a Logistics tab.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### sound_no_fuel
- **Type:** [[Sound]]
- **Optional**

### driving_sound_volume_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Cannot be negative.

### darkness_to_render_light_animation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.3`

### track_particle_triggers
- **Type:** [[FootstepTriggerEffectList]]
- **Optional**

### guns
- **Type:** array<[[ItemID (type)]]>
- **Optional**
The names of the  [[GunPrototype]]s this car prototype uses.
