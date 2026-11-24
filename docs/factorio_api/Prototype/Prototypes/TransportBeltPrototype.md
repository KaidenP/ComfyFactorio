---
title: TransportBeltPrototype
tags: [factorio-api, prototype]
---
# TransportBeltPrototype

> **Parent:** [[TransportBeltConnectablePrototype]] · **Type name:** `transport-belt`

A [transport belt](https://wiki.factorio.com/Transport_belt).

## Properties

### connector_frame_sprites
- **Type:** [[TransportBeltConnectorFrame]]
- **Optional**

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
Set of 7 [[CircuitConnectorDefinition|circuit connector definitions]] in order: X, H, V, SE, SW, NE and NW.

### belt_animation_set
- **Type:** [[TransportBeltAnimationSetWithCorners]]
- **Optional**
- **Overrides parent**

### related_underground_belt
- **Type:** [[EntityID (type)]]
- **Optional**
The name of the [[UndergroundBeltPrototype]] which is used in quick-replace fashion when the smart belt dragging behavior is triggered.
