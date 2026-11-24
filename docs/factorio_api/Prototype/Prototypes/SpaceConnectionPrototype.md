---
title: SpaceConnectionPrototype
tags: [factorio-api, prototype]
---
# SpaceConnectionPrototype

> **Parent:** [[Prototype]] · **Type name:** `space-connection`

## Properties

### from
- **Type:** [[SpaceLocationID (type)]]

### to
- **Type:** [[SpaceLocationID (type)]]

### length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `600`
Length of the space connection in km.

Cannot be 0.

### origin
- **Type:** [[MapPosition (type)]]
- **Optional**
- **Default:** `{0, 0}`

### shape
- **Type:** `"arc"` | `"line"`
- **Optional**
- **Default:** `"arc"`

### asteroid_spawn_definitions
- **Type:** array<[[SpaceConnectionAsteroidSpawnDefinition (type)]]>
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
