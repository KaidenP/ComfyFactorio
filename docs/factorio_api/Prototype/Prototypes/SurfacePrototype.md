---
title: SurfacePrototype
tags: [factorio-api, prototype]
---
# SurfacePrototype

> **Parent:** [[Prototype]] · **Type name:** `surface`

## Properties

### surface_properties
- **Type:** dictionary<[[SurfacePropertyID (type)]] → [[double (type)]]>
- **Optional**

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.
