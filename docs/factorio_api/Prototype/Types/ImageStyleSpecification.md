---
title: ImageStyleSpecification
tags: [factorio-api, prototype, type]
---
# ImageStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"image"`

## Properties

### type
- **Type:** `"image_style"`

### graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### stretch_image_to_widget_size
- **Type:** [[boolean (type)]]
- **Optional**
Required on the root style.

### invert_colors_of_picture_when_hovered_or_toggled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

## Examples

```
data.raw["gui-style"]["default"]["stretchy-sprite"] =
{
  type = "image_style",
  vertically_stretchable = "on",
  horizontally_stretchable = "on",
  stretch_image_to_widget_size = true,
}
```
