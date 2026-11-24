---
title: OffshorePumpPrototype
tags: [factorio-api, prototype]
---
# OffshorePumpPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `offshore-pump`

An [offshore pump](https://wiki.factorio.com/Offshore_pump).

## Properties

### fluid_box
- **Type:** [[FluidBox]]

### pumping_speed
- **Type:** [[FluidAmount (type)]]
How many units of fluid are produced per tick. Must be > 0.

### fluid_source_offset
- **Type:** [[Vector (type)]]

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed.

### graphics_set
- **Type:** [[OffshorePumpGraphicsSet]]
- **Optional**

### energy_source
- **Type:** [[EnergySource]]
Defines how the offshore pump is powered.

When using an electric energy source and `drain` is not specified, it will be set to `energy_usage ÷ 30` automatically.

### energy_usage
- **Type:** [[Energy]]
Sets how much energy this offshore pump consumes. Energy usage has to be positive.
**Examples:**

```
energy_usage = "60kW"
```

### remove_on_tile_collision
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### always_draw_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If false, the offshore pump will not show fluid present (visually) before there is an output connected. The pump will also animate yet not show fluid when the fluid is 100% extracted (e.g. such as with a pump).

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
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.
