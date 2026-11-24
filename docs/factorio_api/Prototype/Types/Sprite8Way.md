---
title: Sprite8Way
tags: [factorio-api, prototype, type]
---
# Sprite8Way

A map of sprites for 8 directions of the entity.

## Properties

### sheets
- **Type:** array<[[SpriteNWaySheet]]>
- **Optional**

### sheet
- **Type:** [[SpriteNWaySheet]]
- **Optional**
Only loaded if `sheets` is not defined.

### north
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### north_east
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### east
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### south_east
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### south
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### south_west
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### west
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

### north_west
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.
