---
title: TileTransitionSpritesheetLayout
tags: [factorio-api, prototype, type]
---
# TileTransitionSpritesheetLayout

> **Parent:** [[TileSpriteLayoutVariant]]

The properties from the parent TileSpriteLayoutVariant provide defaults for the TileTransitionVariantLayouts.

The `{inner_corner | outer_corner | side | double_side | u_transition | o_transition}_*` properties provide defaults for the corresponding properties in the TileTransitionVariantLayouts. They are used when the TileTransitionVariantLayouts have the same layout. See the example below.

## Properties

### overlay
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#overlay_layout|TileTransitions::overlay_layout]] is not defined in the TileTransitions that load this.

### mask
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#mask_layout|TileTransitions::mask_layout]] is not defined in the TileTransitions that load this.

### background
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#background_layout|TileTransitions::background_layout]] is not defined in the TileTransitions that load this.

### background_mask
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#background_mask_layout|TileTransitions::background_mask_layout]] is not defined in the TileTransitions that load this.

### effect_map
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#effect_map_layout|TileTransitions::effect_map_layout]] is not defined in the TileTransitions that load this.

### lightmap
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#lightmap_layout|TileTransitions::lightmap_layout]] is not defined in the TileTransitions that load this.

### auxiliary_effect_mask
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Only loaded if [[TileTransitions#auxiliary_effect_mask_layout|TileTransitions::auxiliary_effect_mask_layout]] is not defined in the TileTransitions that load this.

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
-- all the layers use the same layout, at different offsets inside the spritesheet
layout =
{
  scale = 0.5,
  inner_corner_count = 8,
  outer_corner_count = 8,
  o_transition_count = 1,
  outer_corner_x = 576,
  u_transition_x = 1728,

  overlay = { y_offset = 0 },  -- 0 is default, but by defining overlay property, we enable the layer
  mask = { y_offset = 512 },
  background = { y_offset = 1024 }
}
```
