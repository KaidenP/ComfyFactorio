---
title: CombinatorPrototype
tags: [factorio-api, prototype]
---
# CombinatorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

Abstract base type for decider and arithmetic combinators.

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]] | [[VoidEnergySource]]
Defines how this combinator gets energy. The emissions set on the energy source are ignored so combinators cannot produce pollution.

### active_energy_usage
- **Type:** [[Energy]]
**Examples:**

```
active_energy_usage = "1kW"
```

### sprites
- **Type:** [[Sprite4Way]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### activity_led_sprites
- **Type:** [[Sprite4Way]]
- **Optional**

### input_connection_bounding_box
- **Type:** [[BoundingBox (type)]]

### output_connection_bounding_box
- **Type:** [[BoundingBox (type)]]

### activity_led_light_offsets
- **Type:** ([[Vector (type)]], [[Vector (type)]], [[Vector (type)]], [[Vector (type)]])

### screen_light_offsets
- **Type:** ([[Vector (type)]], [[Vector (type)]], [[Vector (type)]], [[Vector (type)]])

### input_connection_points
- **Type:** ([[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]])

### output_connection_points
- **Type:** ([[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]])

### activity_led_light
- **Type:** [[LightDefinition]]
- **Optional**

### screen_light
- **Type:** [[LightDefinition]]
- **Optional**

### activity_led_hold_time
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `5`

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

### emissions_per_second
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**
- **Overrides parent**
Emissions cannot be larger than zero, combinators cannot produce pollution.
