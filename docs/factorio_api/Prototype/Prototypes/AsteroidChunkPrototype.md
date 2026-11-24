---
title: AsteroidChunkPrototype
tags: [factorio-api, prototype]
---
# AsteroidChunkPrototype

> **Parent:** [[Prototype]] · **Type name:** `asteroid-chunk`

## Properties

### minable
- **Type:** [[MinableProperties]]
- **Optional**

### dying_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### graphics_set
- **Type:** [[AsteroidGraphicsSet]]
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

### hide_from_signal_gui
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** unset
