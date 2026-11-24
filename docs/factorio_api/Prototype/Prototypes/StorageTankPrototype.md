---
title: StorageTankPrototype
tags: [factorio-api, prototype]
---
# StorageTankPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `storage-tank`

A [storage tank](https://wiki.factorio.com/Storage_tank).

## Properties

### fluid_box
- **Type:** [[FluidBox]]

### window_bounding_box
- **Type:** [[BoundingBox (type)]]
The location of the window showing the contents. Note that for `window_background` the width and height are determined by the sprite and window_bounding_box only determines the drawing location. For `fluid_background` the width is determined by the sprite and the height and drawing location are determined by window_bounding_box.

### pictures
- **Type:** [[StorageTankPictures]]
- **Optional**

### flow_length_in_ticks
- **Type:** [[uint32 (type)]]
Must be positive.

Used for determining the x position inside the `flow_sprite` when drawing the storage tank. Does not affect gameplay.

The x position of the sprite will be `((game.tick % flow_length_in_ticks) ÷ flow_length_in_ticks) × (flow_sprite.width - 32)`. This means, that over `flow_length_in_ticks` ticks, the part of the `flow_sprite` that is drawn in-game is incrementally moved from most-left to most-right inside the actual sprite, that part always has a width of 32px. After `flow_length_in_ticks`, the part of the `flow_sprite` that is drawn will start from the left again.

### two_direction_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### show_fluid_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the "alt-mode icon" should be drawn at all.

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

### default_fluid_temperature_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, fluid pipelines will be visualized when this entity is held in the cursor.
