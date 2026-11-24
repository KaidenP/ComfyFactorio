---
title: ArtilleryProjectilePrototype
tags: [factorio-api, prototype]
---
# ArtilleryProjectilePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `artillery-projectile`

The projectile shot by [artillery](https://wiki.factorio.com/Artillery).

## Properties

### reveal_map
- **Type:** [[boolean (type)]]

### picture
- **Type:** [[Sprite]]
- **Optional**

### shadow
- **Type:** [[Sprite]]
- **Optional**

### chart_picture
- **Type:** [[Sprite]]
- **Optional**

### action
- **Type:** [[Trigger]]
- **Optional**

### final_action
- **Type:** [[Trigger]]
- **Optional**

### height_from_ground
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### rotatable
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the picture of the projectile is rotated to match the direction of travel.

### map_color
- **Type:** [[Color (type)]]
- **Overrides parent**

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

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
