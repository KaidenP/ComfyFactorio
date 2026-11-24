---
title: BeamPrototype
tags: [factorio-api, prototype]
---
# BeamPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `beam`

Used as a laser beam.

## Properties

### action
- **Type:** [[Trigger]]
- **Optional**

### width
- **Type:** [[float (type)]]

### damage_interval
- **Type:** [[uint32 (type)]]
Damage interval can't be 0. A value of 1 will cause the attack to be applied each tick.

### target_offset
- **Type:** [[Vector (type)]]
- **Optional**

### random_target_offset
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### action_triggered_automatically
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this beams should trigger its action every `damage_interval`. If false, the action is instead triggered when its owner triggers shooting.

### graphics_set
- **Type:** [[BeamGraphicsSet]]

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
