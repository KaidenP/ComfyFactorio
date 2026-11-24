---
title: ProxyContainerPrototype
tags: [factorio-api, prototype]
---
# ProxyContainerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `proxy-container`

A container that must be set to point at other entity and inventory index so it can forward all inventory interactions to the other entity.

## Properties

### direction_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
Amount of directions this container should have. Allowed values are 1, 2 and 4.

### picture
- **Type:** [[Sprite4Way]]
- **Optional**

### draw_inventory_content
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If the content of the inventory should be rendered in alt mode.

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
If given, there must be exactly `direction_count` elements in the table.

### default_empty_slots_signal
- **Type:** [[SignalIDConnector]]
- **Optional**
