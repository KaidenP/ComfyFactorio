---
title: AsteroidCollectorPrototype
tags: [factorio-api, prototype]
---
# AsteroidCollectorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `asteroid-collector` · **Requires:** `space_age`

## Properties

### arm_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `5`

### arm_inventory_size_quality_increase
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `39`

### inventory_size_quality_increase
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `5`

### graphics_set
- **Type:** [[AsteroidCollectorGraphicsSet]]

### passive_energy_usage
- **Type:** [[Energy]]

### arm_energy_usage
- **Type:** [[Energy]]

### arm_slow_energy_usage
- **Type:** [[Energy]]
If `arm_energy_usage` is not met, attempts to move slower at the cost of `arm_slow_energy_usage`.

### energy_usage_quality_scaling
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### arm_count_base
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `3`

### arm_count_quality_scaling
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`

### head_collection_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.6`

### collection_box_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### deposit_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.5`

### arm_speed_base
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### arm_speed_quality_scaling
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### arm_angular_speed_cap_base
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### arm_angular_speed_cap_quality_scaling
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### tether_size
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.4`

### unpowered_arm_speed_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.3`

### minimal_arm_swing_segment_retraction
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `6`

### held_items_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### held_items_spread
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.15`

### held_items_display_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `5`

### munch_sound
- **Type:** [[Sound]]
- **Optional**

### deposit_sound
- **Type:** [[Sound]]
- **Optional**

### arm_extend_sound
- **Type:** [[Sound]]
- **Optional**

### arm_retract_sound
- **Type:** [[Sound]]
- **Optional**

### energy_source
- **Type:** [[ElectricEnergySource]] | [[VoidEnergySource]]

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

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**

### collection_radius
- **Type:** [[double (type)]]
Must be positive.

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### arm_color_gradient
- **Type:** array<[[Color (type)]]>
- **Optional**
- **Default:** {{1, 1, 1}}
