---
title: VehiclePrototype
tags: [factorio-api, prototype]
---
# VehiclePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

Abstract base of all vehicles.

## Properties

### weight
- **Type:** [[double (type)]]
Must be positive. Weight of the entity used for physics calculation when car hits something.

### braking_force
- **Type:** [[double (type)]]
Must be positive.

### friction_force
- **Type:** [[double (type)]]
Must be positive.

### energy_per_hit_point
- **Type:** [[double (type)]]
The (movement) energy used per hit point (1 hit point = 1 health damage) taken and dealt for this vehicle during collisions. The smaller the number, the more damage this vehicle and the rammed entity take during collisions: `damage = energy / energy_per_hit_point`.

### terrain_friction_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be in the [0, 1] interval.

### impact_speed_to_volume_ratio
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `5.0`

### stop_trigger_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### crash_trigger
- **Type:** [[TriggerEffect]]
- **Optional**

### stop_trigger
- **Type:** [[TriggerEffect]]
- **Optional**

### equipment_grid
- **Type:** [[EquipmentGridID]]
- **Optional**
The name of the [[EquipmentGridPrototype]] this vehicle has.

### minimap_representation
- **Type:** [[Sprite]]
- **Optional**
The sprite that represents this vehicle on the map/minimap.

### selected_minimap_representation
- **Type:** [[Sprite]]
- **Optional**
The sprite that represents this vehicle on the map/minimap when it is selected.

### allow_passengers
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Determines whether this vehicle accepts passengers. This includes both drivers and gunners, if applicable.

### deliver_category
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
Name of a [[DeliverCategory]].

### chunk_exploration_radius
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
In chunks. The radius of the radar range of the vehicle, so how many chunks it charts around itself.

### allow_remote_driving
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
