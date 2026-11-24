---
title: ProgrammableSpeakerPrototype
tags: [factorio-api, prototype]
---
# ProgrammableSpeakerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `programmable-speaker`

A [programmable speaker](https://wiki.factorio.com/Programmable_speaker).

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]] | [[VoidEnergySource]]

### energy_usage_per_tick
- **Type:** [[Energy]]

### sprite
- **Type:** [[Sprite]]
- **Optional**

### maximum_polyphony
- **Type:** [[uint32 (type)]]

### instruments
- **Type:** array<[[ProgrammableSpeakerInstrument (type)]]>

### audible_distance_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

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
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**
