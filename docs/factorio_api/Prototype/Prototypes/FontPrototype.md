---
title: FontPrototype
tags: [factorio-api, prototype]
---
# FontPrototype

> **Type name:** `font`

Fonts are used in all GUIs in the game.

## Properties

### type
- **Type:** `"font"`

### name
- **Type:** [[string (type)]]
Name of the font.

### size
- **Type:** [[int32 (type)]]
Size of the font.

### from
- **Type:** [[string (type)]]
The name of the fonts .ttf descriptor. This descriptor must be defined in the locale info.json. Refer to `data/core/locale/_language_/info.json` for examples.

### spacing
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### border
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the font has a border.

### filtered
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### border_color
- **Type:** [[Color (type)]]
- **Optional**
The color of the border, if enabled.

## Example

```
{
  type = "font",
  name = "default-button",
  from = "default-bold",
  size = 18
}
```
