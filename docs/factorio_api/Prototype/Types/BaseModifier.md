---
title: BaseModifier
tags: [factorio-api, prototype, type]
---
# BaseModifier

> **Abstract**

The abstract base of all [[Modifier|Modifiers]].

## Properties

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
