---
title: CraftingMachineGraphicsSet
tags: [factorio-api, prototype, type]
---
# CraftingMachineGraphicsSet

> **Parent:** [[WorkingVisualisations]]

## Properties

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### animation_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### reset_animation_when_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Only loaded if this graphics set is used in a property called `graphics_set`, refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
