---
title: PipePrototype
tags: [factorio-api, prototype]
---
# PipePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `pipe`

An entity to transport fluids over a distance and between machines.

## Properties

### fluid_box
- **Type:** [[FluidBox]]
The area of the entity where fluid/gas inputs, and outputs.

### horizontal_window_bounding_box
- **Type:** [[BoundingBox (type)]]

### vertical_window_bounding_box
- **Type:** [[BoundingBox (type)]]

### pictures
- **Type:** [[PipePictures]]
- **Optional**
All graphics for this pipe.

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
- **Type:** array<[[CircuitConnectorDefinition]]>
- **Optional**
If given, there must be exactly 16 elements in the table.

### default_fluid_temperature_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.

### random_variation_on_create
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether a random graphics variation is chosen when placing the entity/creating it via script/creating it via map generation. If this is `false`, the entity will use the first variation instead of a random one.

### draw_window
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When this is `false`, pipe will never attempt drawing window.
