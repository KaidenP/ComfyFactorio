---
title: RotatedAnimation8Way
tags: [factorio-api, prototype, type]
---
# RotatedAnimation8Way

A map of rotated animations for all 8 directions of the entity. If this is loaded as a single RotatedAnimation, it applies to all directions.

Any direction that is not defined defaults to the rotated animation of the opposite direction. If that is also not defined, it defaults to the north rotated animation.

## Type

struct | [[RotatedAnimation]]

## Properties

### north
- **Type:** [[RotatedAnimation]]

### north_east
- **Type:** [[RotatedAnimation]]
- **Optional**

### east
- **Type:** [[RotatedAnimation]]
- **Optional**

### south_east
- **Type:** [[RotatedAnimation]]
- **Optional**

### south
- **Type:** [[RotatedAnimation]]
- **Optional**

### south_west
- **Type:** [[RotatedAnimation]]
- **Optional**

### west
- **Type:** [[RotatedAnimation]]
- **Optional**

### north_west
- **Type:** [[RotatedAnimation]]
- **Optional**
