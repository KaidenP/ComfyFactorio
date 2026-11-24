---
title: RadarPrototype
tags: [factorio-api, prototype]
---
# RadarPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `radar`

A [radar](https://wiki.factorio.com/Radar).

## Properties

### energy_usage
- **Type:** [[Energy]]
The amount of energy this radar uses.
**Examples:**

```
energy_usage = "300kW"
```

### energy_per_sector
- **Type:** [[Energy]]
The amount of energy it takes to scan a sector. This value doesn't have any effect on nearby scanning.
**Examples:**

```
energy_per_sector = "10MJ"
```

### energy_per_nearby_scan
- **Type:** [[Energy]]
The amount of energy the radar has to consume for nearby scan to be performed. This value doesn't have any effect on sector scanning.

Performance warning: nearby scan causes re-charting of many chunks, which is expensive operation. If you want to make a radar that updates map more in real time, you should keep its range low. If you are making radar with high range, you should set this value such that nearby scan is performed once a second or so. For example if you set `energy_usage` to 100kW, setting `energy_per_nearby_scan` to 100kJ will cause nearby scan to happen once per second.
**Examples:**

```
energy_per_nearby_scan = "250kJ"
```

### energy_source
- **Type:** [[EnergySource]]
The energy source for this radar.

### pictures
- **Type:** [[RotatedSprite]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite]]
- **Optional**

### max_distance_of_sector_revealed
- **Type:** [[uint32 (type)]]
The radius of the area this radar can chart, in chunks.

### max_distance_of_nearby_sector_revealed
- **Type:** [[uint32 (type)]]
The radius of the area constantly revealed by this radar, in chunks.

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

### radius_minimap_visualisation_color
- **Type:** [[Color (type)]]
- **Optional**

### rotation_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.01`

### connects_to_other_radars
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If set to true, radars on the same surface will connect to other radars on the same surface using hidden wires with [[defines.wire_origin#radars|radar]] origin.

### reset_orientation_when_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### energy_fraction_to_connect
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.9`
Must be between 0 and 1. Must be larger than or equal to `energy_fraction_to_disconnect`.

### energy_fraction_to_disconnect
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`
Must be between 0 and 1. Must be less than or equal to `energy_fraction_to_connect`.

### default_universe_channel
- **Type:** [[SignalIDConnector]]
- **Optional**
The default channel for the circuit network connection in universe mode.

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).
