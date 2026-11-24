---
title: HeatPipePrototype
tags: [factorio-api, prototype]
---
# HeatPipePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `heat-pipe`

A [heat pipe](https://wiki.factorio.com/Heat_pipe).

## Properties

### connection_sprites
- **Type:** [[ConnectableEntityGraphics]]
- **Optional**

### heat_glow_sprites
- **Type:** [[ConnectableEntityGraphics]]
- **Optional**

### heat_buffer
- **Type:** [[HeatBuffer]]

### heating_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be >= 0.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `45`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.

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
- **Type:** array<[[CircuitConnectorDefinition]]>
- **Optional**
Set of 16 circuit connector definitions. They correspond to the following sprites in this exact order: [[ConnectableEntityGraphics#single|single]], [[ConnectableEntityGraphics#ending_up|ending_up]], [[ConnectableEntityGraphics#ending_right|ending_right]], [[ConnectableEntityGraphics#corner_right_up|corner_right_up]], [[ConnectableEntityGraphics#ending_down|ending_down]], [[ConnectableEntityGraphics#straight_vertical|straight_vertical]], [[ConnectableEntityGraphics#corner_right_down|corner_right_down]], [[ConnectableEntityGraphics#t_right|t_right]], [[ConnectableEntityGraphics#ending_left|ending_left]], [[ConnectableEntityGraphics#corner_left_up|corner_left_up]], [[ConnectableEntityGraphics#straight_horizontal|straight_horizontal]], [[ConnectableEntityGraphics#t_up|t_up]], [[ConnectableEntityGraphics#corner_left_down|corner_left_down]], [[ConnectableEntityGraphics#t_left|t_left]], [[ConnectableEntityGraphics#t_down|t_down]], [[ConnectableEntityGraphics#cross|cross]].

### default_temperature_signal
- **Type:** [[SignalIDConnector]]
- **Optional**
