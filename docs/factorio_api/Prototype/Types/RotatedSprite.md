---
title: RotatedSprite
tags: [factorio-api, prototype, type]
---
# RotatedSprite

> **Parent:** [[SpriteParameters]]

Specifies series of sprites used to visualize different rotations of the object.

## Properties

### layers
- **Type:** array<[[RotatedSprite]]>
- **Optional**
If this property is present, all RotatedSprite definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

If this property is present, all other properties, including those inherited from SpriteParameters, are ignored.

### direction_count
- **Type:** [[uint16 (type)]]
- **Optional**
Only loaded, and mandatory if `layers` is not defined.

Count of direction (frames) specified.

### filename
- **Type:** [[FileName]]
- **Optional**
- **Overrides parent**
Only loaded if `layers` is not defined.

The path to the sprite file to use.

### filenames
- **Type:** array<[[FileName]]>
- **Optional**
Only loaded, and mandatory if both `layers` and `filename` are not defined.

### lines_per_file
- **Type:** [[uint64 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined. Mandatory if `filenames` is defined.

### dice
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Number of slices this is sliced into when using the "optimized atlas packing" option. If you are a modder, you can just ignore this property. Example: If this is 4, the sprite will be sliced into a 4x4 grid.

### dice_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Same as `dice` above, but this specifies only how many slices there are on the x axis.

### dice_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Same as `dice` above, but this specifies only how many slices there are on the y axis.

### generate_sdf
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Only loaded if `layers` is not defined.

Unused.

### back_equals_front
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### apply_projection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only loaded if `layers` is not defined.

Used to fix the inconsistency of direction of the entity in 3d when rendered and direction on the screen (where the 45 degree angle for projection is used).

### counterclockwise
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Set to `true` to indicate sprites in the spritesheet are in counterclockwise order.

### line_length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Once the specified number of pictures is loaded, other pictures are loaded on other line. This is to allow having more sprites in matrix, to input files with too high width. The game engine limits the width of any input files to 8192px, so it is compatible with most graphics cards. 0 means that all the pictures are in one horizontal line.

### allow_low_quality_rotation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### frames
- **Type:** array<[[RotatedSpriteFrame]]>
- **Optional**
A list of overrides and customizations for each specific frame within the rotated sprite. This can be used to adjust each individual frame's width, height, and other properties. If this property is present, then it must contain at least as many `RotatedSpriteFrame` as there are sprites in this RotatedSprite.

## Examples

```
pictures =
{
  layers =
  {
    {
      filename = "__base__/graphics/entity/radar/radar.png",
      priority = "low",
      width = 196,
      height = 254,
      apply_projection = false,
      direction_count = 64,
      line_length = 8,
      shift = util.by_pixel(1, -16),
      scale = 0.5
    },
    {
      filename = "__base__/graphics/entity/radar/radar-shadow.png",
      priority = "low",
      width = 343,
      height = 186,
      apply_projection = false,
      direction_count = 64,
      line_length = 8,
      shift = util.by_pixel(39.25,3),
      draw_as_shadow = true,
      scale = 0.5
    }
  }
}
```
