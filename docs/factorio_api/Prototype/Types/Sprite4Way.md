---
title: Sprite4Way
tags: [factorio-api, prototype, type]
---
# Sprite4Way

Sprites for the 4 major directions of the entity. If this is loaded as a single Sprite, it applies to all directions.

This struct is either loaded as `sheets` or `sheet` or a map of one sprite per direction. For per direction sprites, the sprites are loaded via `north`, `east`, `south` and `west`.

## Type

struct | [[Sprite]]

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
Only loaded if both `sheets` and `sheet` are not defined.

### east
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

Only loaded if `north` is defined.

### south
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

Only loaded if `north` is defined.

### west
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if both `sheets` and `sheet` are not defined.

Only loaded if `north` is defined.

## Examples

```
-- separate sprites per direction
{
  north =
  {
    filename = "__base__/graphics/entity/assembling-machine-3/assembling-machine-3-pipe-N.png",
    priority = "extra-high",
    width = 71,
    height = 38,
    shift = util.by_pixel(2.25, 13.5),
    scale = 0.5
  },
  east =
  {
    filename = "__base__/graphics/entity/assembling-machine-3/assembling-machine-3-pipe-E.png",
    priority = "extra-high",
    width = 42,
    height = 76,
    shift = util.by_pixel(-24.5, 1),
    scale = 0.5
  },
  south =
  {
    filename = "__base__/graphics/entity/assembling-machine-3/assembling-machine-3-pipe-S.png",
    priority = "extra-high",
    width = 88,
    height = 61,
    shift = util.by_pixel(0, -31.25),
    scale = 0.5
  },
  west =
  {
    filename = "__base__/graphics/entity/assembling-machine-3/assembling-machine-3-pipe-W.png",
    priority = "extra-high",
    width = 39,
    height = 73,
    shift = util.by_pixel(25.75, 1.25),
    scale = 0.5
  }
}
```
