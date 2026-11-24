---
title: MiningDrillGraphicsSet
tags: [factorio-api, prototype, type]
---
# MiningDrillGraphicsSet

> **Parent:** [[WorkingVisualisations]]

Used by [[MiningDrillPrototype]].

## Properties

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### reset_animation_when_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### drilling_vertical_movement_duration
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### animation_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Only loaded if this graphics set is used in a property called `graphics_set`, refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
