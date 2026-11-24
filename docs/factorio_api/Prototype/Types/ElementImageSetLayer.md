---
title: ElementImageSetLayer
tags: [factorio-api, prototype, type]
---
# ElementImageSetLayer

If this is loaded as a Sprite, it gets used as `center`.

## Type

struct | [[Sprite]]

## Properties

### draw_type
- **Type:** `"inner"` | `"outer"`
- **Optional**
- **Default:** `"inner"`
Defines whether the border should be drawn inside the widget, which affects the padding and content size of the widget, or outside of the widget which doesn't affect size. The outer draw type is most commonly used for shadows, glows and insets.

### type
- **Type:** `"none"` | `"composition"`
- **Optional**
- **Default:** `"none"` if this has no other properties, otherwise `"composition"`

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1}`
Only loaded if `type` is `"composition"`.

### center
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### left
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### left_top
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### left_bottom
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### right
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### right_top
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### right_bottom
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### top
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### bottom
- **Type:** [[Sprite]]
- **Optional**
Only loaded if `type` is `"composition"`.

### corner_size
- **Type:** [[uint16 (type)]] | ([[uint16 (type)]], [[uint16 (type)]])
- **Optional**
If this is a tuple, the first member of the tuple is width and the second is height. Otherwise the size is both width and height.

Only loaded if `type` is `"composition"`.
**Examples:**

```
{
  -- How an ElementImageSet is loaded which has only one layer, which uses the corner_size shown in the diagram
  base = {position = {0, 17}, corner_size = 8}
}
```

![[ElementImageSetLayer_base_sizes.png]]
*In base game, the corner size is 8 and the sides are 1px long and 8px wide.*

### filename
- **Type:** [[FileName]]
- **Optional**
- **Default:** The `default_tileset` set in GuiStyle
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### position
- **Type:** [[MapPosition (type)]]
- **Optional**
Mandatory if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### load_in_minimal_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### top_width
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### bottom_width
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### left_height
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### right_height
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### center_width
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### center_height
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `corner_size` is defined. Only loaded if `type` is `"composition"`.

### top_border
- **Type:** [[int32 (type)]]
- **Optional**
Only loaded if `type` is `"composition"`.

### right_border
- **Type:** [[int32 (type)]]
- **Optional**
Only loaded if `type` is `"composition"`.

### bottom_border
- **Type:** [[int32 (type)]]
- **Optional**
Only loaded if `type` is `"composition"`.

### left_border
- **Type:** [[int32 (type)]]
- **Optional**
Only loaded if `type` is `"composition"`.

### border
- **Type:** [[int32 (type)]]
- **Optional**
Sets `top_border`, `right_border`, `bottom_border` and `left_border`.

Only loaded if `corner_size` is not defined. Only loaded if `type` is `"composition"`.

### stretch_monolith_image_to_size
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only loaded if `type` is `"composition"`.

### left_tiling
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Tiling is used to make a side (not corner) texture repeat instead of being stretched.

### right_tiling
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### top_tiling
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### bottom_tiling
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### center_tiling_vertical
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### center_tiling_horizontal
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### overall_tiling_horizontal_size
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Overall tiling is used to make the overall texture repeat instead of being stretched.

### overall_tiling_horizontal_spacing
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### overall_tiling_horizontal_padding
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### overall_tiling_vertical_size
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### overall_tiling_vertical_spacing
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### overall_tiling_vertical_padding
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### custom_horizontal_tiling_sizes
- **Type:** array<[[uint32 (type)]]>
- **Optional**

### opacity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### background_blur
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### background_blur_sigma
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `4` if `background_blur` is `true`

### top_outer_border_shift
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### bottom_outer_border_shift
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### right_outer_border_shift
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### left_outer_border_shift
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

## Images

![[ElementImageSetLayer_properties.png]]
*How the sprites are laid out graphically when using a composition type element image set layer.*

![[ElementImageSetLayer_stretching.png]]
*How the sprites are stretched when using a composition type element image set layer.*
