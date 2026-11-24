---
title: RoboportPrototype
tags: [factorio-api, prototype]
---
# RoboportPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `roboport`

A [roboport](https://wiki.factorio.com/Roboport).

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]] | [[VoidEnergySource]]
The roboport's energy source.

### energy_usage
- **Type:** [[Energy]]
The amount of energy the roboport uses when idle.
**Examples:**

```
energy_usage = "50kW"
```

### recharge_minimum
- **Type:** [[Energy]]
Minimum charge that the roboport has to have after a blackout (0 charge/buffered energy) to begin working again. Additionally, freshly placed roboports will have their energy buffer filled with `0.25 × recharge_minimum` energy.

Must be larger than or equal to `energy_usage` otherwise during low power the roboport will toggle on and off every tick.
**Examples:**

```
recharge_minimum = "40MJ"
```

### robot_slots_count
- **Type:** [[ItemStackIndex (type)]]
The number of robot slots in the roboport.

### material_slots_count
- **Type:** [[ItemStackIndex (type)]]
The number of repair pack slots in the roboport.

### base
- **Type:** [[Sprite]]
- **Optional**

### base_patch
- **Type:** [[Sprite]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite]]
- **Optional**

### base_animation
- **Type:** [[Animation]]
- **Optional**
The animation played when the roboport is idle.

### door_animation_up
- **Type:** [[Animation]]
- **Optional**

### door_animation_down
- **Type:** [[Animation]]
- **Optional**

### request_to_open_door_timeout
- **Type:** [[uint32 (type)]]

### radar_range
- **Type:** [[uint32 (type)]]
- **Optional**
In chunks. The radius of how many chunks this roboport charts around itself. Defaults to the max of logistic range or construction range rounded up to chunks.

### radar_visualisation_color
- **Type:** [[Color (type)]]
- **Optional**

### recharging_animation
- **Type:** [[Animation]]
- **Optional**
The animation played at each charging point when a robot is charging there.

### spawn_and_station_height
- **Type:** [[float (type)]]
Presumably states the height of the charging stations and thus an additive offset for the charging_offsets.

### charge_approach_distance
- **Type:** [[float (type)]]
The distance (in tiles) from the roboport at which robots will wait to charge. Notably, if the robot is already in range, then it will simply wait at its current position.

### logistics_radius
- **Type:** [[float (type)]]
Can't be negative.

### construction_radius
- **Type:** [[float (type)]]
Can't be negative.

### charging_energy
- **Type:** [[Energy]]
The maximum power provided to each charging station.
**Examples:**

```
charging_energy = "1000kW"
```

### open_door_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### close_door_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### default_available_logistic_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_total_logistic_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_available_construction_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_total_construction_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_roboport_count_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

### render_recharge_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether to render the [[UtilitySprites#recharge_icon|no charge]] icon if the roboport has less energy than `recharge_minimum` in its internal buffer and is recovering from a blackout.

### max_logistic_slots
- **Type:** [[LogisticFilterIndex (type)]]
- **Optional**

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
Unused.

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
Unused.

### robots_shrink_when_entering_and_exiting
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### charging_offsets
- **Type:** array<[[Vector (type)]]>
- **Optional**
The offsets from the center of the roboport at which robots will charge. Only used if `charging_station_count` is equal to 0.

### logistics_connection_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** value of `logistics_radius`
Must be >= `logistics_radius`.
