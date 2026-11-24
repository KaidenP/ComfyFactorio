---
title: PumpPrototype
tags: [factorio-api, prototype]
---
# PumpPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `pump`

The pump is used to transfer fluids between tanks, fluid wagons and pipes.

## Properties

### fluid_box
- **Type:** [[FluidBox]]
The area of the entity where fluid travels.

### energy_source
- **Type:** [[EnergySource]]
The type of energy the pump uses.

### energy_usage
- **Type:** [[Energy]]
The amount of energy the pump uses.

### pumping_speed
- **Type:** [[FluidAmount (type)]]
The amount of fluid this pump transfers per tick.

### animations
- **Type:** [[Animation4Way]]
- **Optional**
The animation for the pump.

### fluid_wagon_connector_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 / 64.0

### fluid_wagon_tank_valve_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `2.2`
counts from the "start of the arm", which is `pump's position + wagon_connection_graphics.part1_to_2_shift + wagon_connection_graphics.top_pivot_shift (depending on direction)`

### fluid_wagon_connector_frame_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`

### flow_scaling
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When true, pump will reduce pumping speed based on fullness of the input fluid segment.

### fluid_animation
- **Type:** [[Animation4Way]]
- **Optional**

### glass_pictures
- **Type:** [[Sprite4Way]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### wagon_connection_graphics
- **Type:** [[PumpWagonConnectionGraphics]]
- **Optional**

### base_lifting_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### arm_orienting_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### clamp_sound
- **Type:** [[Sound]]
- **Optional**

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.
