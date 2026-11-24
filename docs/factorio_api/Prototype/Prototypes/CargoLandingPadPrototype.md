---
title: CargoLandingPadPrototype
tags: [factorio-api, prototype]
---
# CargoLandingPadPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `cargo-landing-pad`

## Properties

### graphics_set
- **Type:** [[CargoBayConnectableGraphicsSet]]
- **Optional**

### inventory_size
- **Type:** [[ItemStackIndex (type)]]

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

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

### default_empty_slots_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### cargo_station_parameters
- **Type:** [[CargoStationParameters (type)]]

### robot_door
- **Type:** [[RobotDoorSpecification]]
- **Optional**

### radar_range
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
In chunks. The radius of how many chunks this cargo landing pad charts around itself.

### radar_visualisation_color
- **Type:** [[Color (type)]]
- **Optional**
The visualisation used when showing cargo bay unloading distance limits.

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**
