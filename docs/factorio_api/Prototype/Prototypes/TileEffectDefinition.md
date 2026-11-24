---
title: TileEffectDefinition
tags: [factorio-api, prototype]
---
# TileEffectDefinition

> **Type name:** `tile-effect` · **Instance limit:** 255

Used to define the parameters for tile shaders.

## Properties

### type
- **Type:** `"tile-effect"`

### name
- **Type:** [[string (type)]]
Name of the tile-effect.

### shader
- **Type:** `"water"` | `"space"` | `"puddle"`

### water
- **Type:** [[WaterTileEffectParameters]]
- **Optional**
Only loaded, and mandatory if `shader` is `"water"`.

### space
- **Type:** [[SpaceTileEffectParameters]]
- **Optional**
- **Requires:** `space_age`
Only loaded, and mandatory if `shader` is `"space"`.

### puddle
- **Type:** [[PuddleTileEffectParameters]]
- **Optional**
- **Requires:** `space_age`
Only loaded, and mandatory if `shader` is `"puddle"`.
