---
title: PipeToGroundPrototype
tags: [factorio-api, prototype]
---
# PipeToGroundPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `pipe-to-ground`

A [pipe to ground](https://wiki.factorio.com/Pipe_to_ground).

## Properties

### fluid_box
- **Type:** [[FluidBox]]

### pictures
- **Type:** [[Sprite4Way]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### visualization
- **Type:** [[Sprite4Way]]
- **Optional**

### disabled_visualization
- **Type:** [[Sprite4Way]]
- **Optional**

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
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

### default_fluid_temperature_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### draw_fluid_icon_override
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Causes fluid icon to always be drawn, ignoring the usual pair requirement.

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.
