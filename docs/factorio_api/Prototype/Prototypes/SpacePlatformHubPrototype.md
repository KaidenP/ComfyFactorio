---
title: SpacePlatformHubPrototype
tags: [factorio-api, prototype]
---
# SpacePlatformHubPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `space-platform-hub` · **Requires:** `space_age`

## Properties

### graphics_set
- **Type:** [[CargoBayConnectableGraphicsSet]]
- **Optional**

### inventory_size
- **Type:** [[ItemStackIndex (type)]]

### persistent_ambient_sounds
- **Type:** [[PersistentWorldAmbientSoundsDefinition]]
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
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

### default_speed_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_damage_taken_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_empty_slots_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### platform_repair_speed_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Repair speed of entities is multiplied by this value when they are on a space platform with this hub prototype.

### weight
- **Type:** [[Weight (type)]]
- **Optional**
- **Default:** `0`
Mass which this entity adds to total space platform mass when placed.

### cargo_station_parameters
- **Type:** [[CargoStationParameters (type)]]

### build_grid_size
- **Type:** `256`
- **Optional**
- **Default:** `256`
- **Overrides parent**
Has to be 256 to make blueprints snap to (0, 0) most of the time.
