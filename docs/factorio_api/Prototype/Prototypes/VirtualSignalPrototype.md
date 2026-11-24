---
title: VirtualSignalPrototype
tags: [factorio-api, prototype]
---
# VirtualSignalPrototype

> **Parent:** [[Prototype]] · **Type name:** `virtual-signal`

A [virtual signal](https://wiki.factorio.com/Circuit_network#Virtual_signals).

## Properties

### icons
- **Type:** array<[[IconData]]>
- **Optional**
The icon that is used to represent this virtual signal. Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file that is used to represent this virtual signal.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.
