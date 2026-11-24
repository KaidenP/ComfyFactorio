---
title: LabelStyleSpecification
tags: [factorio-api, prototype, type]
---
# LabelStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"label"`

## Properties

### type
- **Type:** `"label_style"`

### font
- **Type:** [[string (type)]]
- **Optional**
Name of a [[FontPrototype]].

Required on the root style.

### font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### hovered_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of `font_color`

### game_controller_hovered_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of `font_color`

### clicked_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of `font_color`

### disabled_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of `font_color`

### parent_hovered_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of `font_color`

### rich_text_setting
- **Type:** [[RichTextSetting]]
- **Optional**
Required on the root style.

### single_line
- **Type:** [[boolean (type)]]
- **Optional**
Required on the root style.

### underlined
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### rich_text_highlight_error_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### rich_text_highlight_warning_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### rich_text_highlight_ok_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.
