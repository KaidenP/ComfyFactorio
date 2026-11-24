---
title: RoboportEquipmentPrototype
tags: [factorio-api, prototype]
---
# RoboportEquipmentPrototype

> **Parent:** [[EquipmentPrototype]] · **Type name:** `roboport-equipment`

Used by [personal roboport](https://wiki.factorio.com/Personal_roboport).

## Properties

### recharging_animation
- **Type:** [[Animation]]
- **Optional**
The animation played at each charging point when a robot is charging there.

### spawn_and_station_height
- **Type:** [[float (type)]]
Presumably states the height of the charging stations and thus an additive offset for the charging_offsets.

### charge_approach_distance
- **Type:** [[float (type)]]
Presumably, the distance from the roboport at which robots will wait to charge.

### construction_radius
- **Type:** [[float (type)]]
Can't be negative.

### charging_energy
- **Type:** [[Energy]]
**Examples:**

```
charging_energy = "1000kW"
```

### spawn_and_station_shadow_height_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### stationing_render_layer_swap_height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.87`
When robot ascends or descends to this roboport, at which height is should switch between `"air-object"` and `"object"` [[RenderLayer (type)|render layer]].

### draw_logistic_radius_visualization
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Unused, as roboport equipment does not have a logistic radius that could be drawn.

### draw_construction_radius_visualization
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### recharging_light
- **Type:** [[LightDefinition]]
- **Optional**
The light emitted when charging a robot.

### charging_station_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
How many charging points this roboport has. If this is 0, the length of the charging_offsets table is used to calculate the charging station count.

### charging_station_count_affected_by_quality
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### charging_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### charging_station_shift
- **Type:** [[Vector (type)]]
- **Optional**

### charging_threshold_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Distance in tiles. This defines how far away a robot can be from the charging spot and still be charged, however the bot is still required to reach a charging spot in the first place.

### robot_vertical_acceleration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.01`

### stationing_offset
- **Type:** [[Vector (type)]]
- **Optional**
The offset from the center of the roboport at which robots will enter and exit.

### robot_limit
- **Type:** [[ItemCountType (type)]]
- **Optional**
- **Default:** max uint
How many robots can exist in the network (cumulative).

### robots_shrink_when_entering_and_exiting
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### charging_offsets
- **Type:** array<[[Vector (type)]]>
- **Optional**
The offsets from the center of the roboport at which robots will charge. Only used if `charging_station_count` is equal to 0.

### spawn_minimum
- **Type:** [[Energy]]
- **Optional**
- **Default:** 0.2 * energy_source.buffer_capacity
Minimum amount of energy that needs to available inside the roboport's buffer so that robots can be spawned.

### burner
- **Type:** [[BurnerEnergySource]]
- **Optional**
Add this is if the roboport should be fueled directly instead of using power from the equipment grid.

### power
- **Type:** [[Energy]]
- **Optional**
Mandatory if `burner` is defined.

The size of the buffer of the burner energy source, so effectively the amount of power that the energy source can produce per tick.
