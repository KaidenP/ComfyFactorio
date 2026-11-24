---
title: ConstructionRobotPrototype
tags: [factorio-api, prototype]
---
# ConstructionRobotPrototype

> **Parent:** [[RobotWithLogisticInterfacePrototype]] · **Type name:** `construction-robot`

A [construction robot](https://wiki.factorio.com/Construction_robot).

## Properties

### construction_vector
- **Type:** [[Vector (type)]]

### working
- **Type:** [[RotatedAnimation]]
- **Optional**

### shadow_working
- **Type:** [[RotatedAnimation]]
- **Optional**

### smoke
- **Type:** [[Animation]]
- **Optional**

### sparks
- **Type:** [[AnimationVariations]]
- **Optional**

### repairing_sound
- **Type:** [[Sound]]
- **Optional**

### mined_sound_volume_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### working_light
- **Type:** [[LightDefinition]]
- **Optional**

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
- **Overrides parent**
Must have a collision box size of zero.
**Examples:**

```
collision_box = {{0, 0}, {0, 0}}
```
