---
title: WallPrototype
tags: [factorio-api, prototype]
---
# WallPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `wall`

A [wall](https://wiki.factorio.com/Wall).

## Properties

### pictures
- **Type:** [[WallPictures]]
- **Optional**

### visual_merge_group
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Different walls will visually connect to each other if their merge group is the same.

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

### default_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### wall_diode_green
- **Type:** [[Sprite4Way]]
- **Optional**

### wall_diode_red
- **Type:** [[Sprite4Way]]
- **Optional**

### wall_diode_green_light_top
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_green_light_right
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_green_light_bottom
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_green_light_left
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_red_light_top
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_red_light_right
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_red_light_bottom
- **Type:** [[LightDefinition]]
- **Optional**

### wall_diode_red_light_left
- **Type:** [[LightDefinition]]
- **Optional**

### connected_gate_visualization
- **Type:** [[Sprite]]
- **Optional**
