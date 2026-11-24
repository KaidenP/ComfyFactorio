---
title: DisplayPanelPrototype
tags: [factorio-api, prototype]
---
# DisplayPanelPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `display-panel`

Entity that display a signal icon and some text, either configured directly in the entity or through the circuit network.

## Properties

### sprites
- **Type:** [[Sprite4Way]]
- **Optional**
The display panel's graphics.

### max_text_width
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `400`
The maximum display width of the text on the display panel. If the text exceeds this width it will be wrapped so that it continues on the next line.

### max_text_length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `500`
Maximum length of the text. If the text exceeds this length all characters beyond the limit will be discarded.

### max_records_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `100`
Maximum amount of message records that can be configured in this display panel when it is connected to circuit network. Must be >= 1.

### text_shift
- **Type:** [[Vector (type)]]
- **Optional**
The shift of the text on the display panel.

### text_color
- **Type:** [[Color (type)]]
- **Optional**
The color of the text on the display panel.

### background_color
- **Type:** [[Color (type)]]
- **Optional**
The background color of the display panel text.

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
