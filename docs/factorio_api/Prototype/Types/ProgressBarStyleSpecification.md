---
title: ProgressBarStyleSpecification
tags: [factorio-api, prototype, type]
---
# ProgressBarStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"progressbar"`

## Properties

### type
- **Type:** `"progressbar_style"`

### bar_width
- **Type:** [[uint32 (type)]]
- **Optional**
The thickness of the bar, not the horizontal size.

Required on the root style.

### color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### other_colors
- **Type:** array<[[OtherColors]]>
- **Optional**
Required on the root style.

### bar
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### bar_background
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### font
- **Type:** [[string (type)]]
- **Optional**
Name of a [[FontPrototype]].

Required on the root style.

### font_color
- **Type:** [[Color (type)]]
- **Optional**
Required on the root style.

### filled_font_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Uses font_color for all text

### embed_text_in_bar
- **Type:** [[boolean (type)]]
- **Optional**
Required on the root style.

### side_text_padding
- **Type:** [[int16 (type)]]
- **Optional**
Required on the root style.
