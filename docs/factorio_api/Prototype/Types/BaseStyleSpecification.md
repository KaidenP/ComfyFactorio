---
title: BaseStyleSpecification
tags: [factorio-api, prototype, type]
---
# BaseStyleSpecification

> **Abstract**

The abstract base of all [[StyleSpecification|StyleSpecifications]].

## Properties

### parent
- **Type:** [[string (type)]]
- **Optional**
Name of a [[StyleSpecification]]. This style inherits all property values from its parent.

Styles without a parent property default to the root style for their type. The exception to this are the root styles themselves, as they cannot have a parent set. Due to this, for root styles, some style properties are mandatory and behavior may be unexpected, such as an element not showing up because its size defaults to `0`.

### horizontal_align
- **Type:** [[HorizontalAlign]]
- **Optional**
- **Default:** `"left"`

### vertical_align
- **Type:** [[VerticalAlign]]
- **Optional**
- **Default:** `"top"`

### ignored_by_search
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### never_hide_by_search
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### horizontally_stretchable
- **Type:** [[StretchRule]]
- **Optional**
- **Default:** `"auto"`

### vertically_stretchable
- **Type:** [[StretchRule]]
- **Optional**
- **Default:** `"auto"`

### horizontally_squashable
- **Type:** [[StretchRule]]
- **Optional**
- **Default:** `"auto"`

### vertically_squashable
- **Type:** [[StretchRule]]
- **Optional**
- **Default:** `"auto"`

### natural_size
- **Type:** [[uint32 (type)]] | ([[uint32 (type)]], [[uint32 (type)]])
- **Optional**
If this is a tuple, the first member sets `natural_width` and the second sets `natural_height`. Otherwise, both `natural_width` and `natural_height` are set to the same value.

### size
- **Type:** [[uint32 (type)]] | ([[uint32 (type)]], [[uint32 (type)]])
- **Optional**
If this is a tuple, the first member sets `width`, and the second sets `height`. Otherwise, both `width` and `height` are set to the same value.

### width
- **Type:** [[uint32 (type)]]
- **Optional**
Sets `minimal_width`, `maximal_width` and `natural_width` to the same value.

### minimal_width
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Minimal width ensures that the widget will never be smaller than than that size. It can't be squashed to be smaller.

### maximal_width
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Maximal width ensures that the widget will never be bigger than than that size. It can't be stretched to be bigger.

### natural_width
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Natural width specifies the width of the element tries to have, but it can still be squashed/stretched to have a different size.

### height
- **Type:** [[uint32 (type)]]
- **Optional**
Sets `minimal_height`, `maximal_height` and `natural_height` to the same value.

### minimal_height
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Minimal height ensures that the widget will never be smaller than than that size. It can't be squashed to be smaller.

### maximal_height
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Maximal height ensures that the widget will never be bigger than than that size. It can't be stretched to be bigger.

### natural_height
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Natural height specifies the height of the element tries to have, but it can still be squashed/stretched to have a different size.

### padding
- **Type:** [[int16 (type)]]
- **Optional**
Sets `top_padding`, `right_padding`, `bottom_padding` and `left_padding` to the same value.

### top_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### right_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### bottom_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### left_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### margin
- **Type:** [[int16 (type)]]
- **Optional**
Sets `top_margin`, `right_margin`, `bottom_margin` and `left_margin` to the same value.

### top_margin
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### right_margin
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### bottom_margin
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### left_margin
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### effect
- **Type:** `"compilatron-hologram"`
- **Optional**
Name of a custom GUI effect, which are hard-coded in the game's engine. Only has one option currently.

### effect_opacity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### tooltip
- **Type:** [[LocalisedString (type)]]
- **Optional**

## Examples

```
-- Adding a custom frame_style-type style via GuiStyle
data.raw["gui-style"]["default"]["custom_style_for_a_frame"] =
{
  type = "frame_style",
  parent = "frame",
  use_header_filler = false,
  drag_by_title = false
}
```
