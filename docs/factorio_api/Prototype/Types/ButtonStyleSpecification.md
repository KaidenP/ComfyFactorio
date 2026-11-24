---
title: ButtonStyleSpecification
tags: [factorio-api, prototype, type]
---
# ButtonStyleSpecification

> **Parent:** [[StyleWithClickableGraphicalSetSpecification]]

Root style: `"button"`

## Properties

### type
- **Type:** `"button_style"`

### font
- **Type:** [[string (type)]]
- **Optional**
Name of a [[FontPrototype]].

Required on the root style.

### default_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### hovered_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### clicked_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### disabled_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### selected_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### selected_hovered_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### selected_clicked_font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### strikethrough_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### pie_progress_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### clicked_vertical_offset
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### draw_shadow_under_picture
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### draw_grayscale_picture
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### invert_colors_of_picture_when_hovered_or_toggled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### invert_colors_of_picture_when_disabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### icon_horizontal_align
- **Type:** [[HorizontalAlign]]
- **Optional**
- **Default:** `"left"`
