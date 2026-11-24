---
title: ConstantCombinatorPrototype
tags: [factorio-api, prototype]
---
# ConstantCombinatorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `constant-combinator`

A [constant combinator](https://wiki.factorio.com/Constant_combinator).

## Properties

### sprites
- **Type:** [[Sprite4Way]]
- **Optional**

### activity_led_sprites
- **Type:** [[Sprite4Way]]
- **Optional**

### activity_led_light_offsets
- **Type:** ([[Vector (type)]], [[Vector (type)]], [[Vector (type)]], [[Vector (type)]])

### circuit_wire_connection_points
- **Type:** ([[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]], [[WireConnectionPoint]])

### activity_led_light
- **Type:** [[LightDefinition]]
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

### pulse_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
When not zero, toggle entity will enable constant combinator for that amount of ticks and then turn it off.
