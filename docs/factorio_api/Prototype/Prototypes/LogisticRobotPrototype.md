---
title: LogisticRobotPrototype
tags: [factorio-api, prototype]
---
# LogisticRobotPrototype

> **Parent:** [[RobotWithLogisticInterfacePrototype]] · **Type name:** `logistic-robot`

A [logistic robot](https://wiki.factorio.com/Logistic_robot).

## Properties

### idle_with_cargo
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the idle state cannot be animated.

### in_motion_with_cargo
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the in_motion state cannot be animated.

### shadow_idle_with_cargo
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the idle state cannot be animated.

### shadow_in_motion_with_cargo
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the in_motion state cannot be animated.

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
