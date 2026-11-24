---
title: TileTransitionVariantLayout
tags: [factorio-api, prototype, type]
---
# TileTransitionVariantLayout

> **Parent:** [[TileSpriteLayoutVariant]]

The properties from the parent TileSpriteLayoutVariant provide defaults for the properties defined here.

The `{inner_corner | outer_corner | side | double_side | u_transition | o_transition}_*` properties provide defaults for the properties inside the specific variant. They are used to specify select values for the variant without creating the table for the variant.

These various ways to define the variants are also shown in the examples below.

## Properties

### x_offset
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`

### y_offset
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`

### inner_corner
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `inner_corner_*` properties.

### outer_corner
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `outer_corner_*` properties.

### side
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `side_*` properties.

### double_side
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `double_side_*` properties.

### u_transition
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `u_transition_*` properties.

### o_transition
- **Type:** [[TileSpriteLayoutVariant]]
- **Optional**
Defaults to the values set in the `o_transition_*` properties.

### inner_corner_scale
- **Type:** [[float (type)]]
- **Optional**

### inner_corner_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### inner_corner_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### inner_corner_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### inner_corner_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### inner_corner_count
- **Type:** [[uint8 (type)]]
- **Optional**

### outer_corner_scale
- **Type:** [[float (type)]]
- **Optional**

### outer_corner_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### outer_corner_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### outer_corner_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### outer_corner_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### outer_corner_count
- **Type:** [[uint8 (type)]]
- **Optional**

### side_scale
- **Type:** [[float (type)]]
- **Optional**

### side_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### side_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### side_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### side_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### side_count
- **Type:** [[uint8 (type)]]
- **Optional**

### double_side_scale
- **Type:** [[float (type)]]
- **Optional**

### double_side_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### double_side_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### double_side_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### double_side_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### double_side_count
- **Type:** [[uint8 (type)]]
- **Optional**

### u_transition_scale
- **Type:** [[float (type)]]
- **Optional**

### u_transition_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### u_transition_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### u_transition_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### u_transition_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### u_transition_count
- **Type:** [[uint8 (type)]]
- **Optional**

### o_transition_scale
- **Type:** [[float (type)]]
- **Optional**

### o_transition_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Horizontal position of the sprite in the source file in pixels.

### o_transition_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Vertical position of the sprite in the source file in pixels.

### o_transition_tile_height
- **Type:** [[uint8 (type)]]
- **Optional**

### o_transition_line_length
- **Type:** [[uint8 (type)]]
- **Optional**

### o_transition_count
- **Type:** [[uint8 (type)]]
- **Optional**

## Examples

```
-- longest version, using TileSpriteLayoutVariant tables for each variant
{
  inner_corner =
  {
    scale = 0.5,
    count = 8,
  },
  outer_corner =
  {
    scale = 0.5,
    count = 8,
    x = 576
  },
  u_transition  =
  {
    scale = 0.5,
    count = 1,
    x = 1728
  },
  [...]
}
```

```
-- The above version is quite verbose, scale is duplicated in each variant layout.
-- So it is possible to define default value of each property of TileSpriteLayoutVariant directly in TileTransitionVariantLayout:
{
  scale = 0.5,
  inner_corner =
  {
    count = 8,
  },
  outer_corner =
  {
    count = 8,
    x = 576
  },
  u_transition  =
  {
    count = 1,
    x = 1728
  },
  [...]
}
```

```
-- The above version is creating a table to just specify inner_corner has 8 count. It can be shorter by using variant prefix properties:
{
  scale = 0.5,
  inner_corner_count = 8,
  outer_corner_count = 8,
  u_transition_count = 1,
  outer_corner_x = 576,
  u_transition_x = 1728,
  [...]
}
```
