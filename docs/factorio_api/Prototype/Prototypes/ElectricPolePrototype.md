---
title: ElectricPolePrototype
tags: [factorio-api, prototype]
---
# ElectricPolePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `electric-pole`

An electric pole - part of the [electric system](https://wiki.factorio.com/Electric_system).

## Properties

### pictures
- **Type:** [[RotatedSprite]]
- **Optional**

### supply_area_distance
- **Type:** [[double (type)]]
The "radius" of this pole's supply area. Corresponds to *half* of the "supply area" in the item tooltip. If this is 3.5, the pole will have a 7x7 supply area.

Max value is 64.

### connection_points
- **Type:** array<[[WireConnectionPoint]]>

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**

### active_picture
- **Type:** [[Sprite]]
- **Optional**
Drawn above the `pictures` when the electric pole is connected to an electric network.

### maximum_wire_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum distance between this pole and any other connected pole - if two poles are farther apart than this, they cannot be connected together directly. Corresponds to "wire reach" in the item tooltip.

Max value is 64.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### light
- **Type:** [[LightDefinition]]
- **Optional**
Drawn when the electric pole is connected to an electric network.

### track_coverage_during_drag_building
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### auto_connect_up_to_n_wires
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `5`
`0` means disable auto-connect.

### rewire_neighbours_when_destroying
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
