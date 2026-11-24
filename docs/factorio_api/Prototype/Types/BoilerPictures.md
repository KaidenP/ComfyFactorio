---
title: BoilerPictures
tags: [factorio-api, prototype, type]
---
# BoilerPictures

## Properties

### structure
- **Type:** [[Animation]]

### patch
- **Type:** [[Sprite]]
- **Optional**
Drawn above the `structure`, in the "higher-object-under" [[RenderLayer (type)|RenderLayer]]. May be useful to correct problems with neighboring pipes overlapping the structure graphics.

### fire
- **Type:** [[Animation]]
- **Optional**
Animation that is drawn on top of the `structure` when `burning_cooldown` is larger than 1. The animation alpha can be controlled by the energy source light intensity, depending on `fire_flicker_enabled`.

The secondary draw order of this is higher than the secondary draw order of `fire_glow`, so this is drawn above `fire_glow`.

### fire_glow
- **Type:** [[Animation]]
- **Optional**
Animation that is drawn on top of the `structure` when `burning_cooldown` is larger than 1. The animation alpha can be controlled by the energy source light intensity, depending on `fire_glow_flicker_enabled`.

The secondary draw order of this is lower than the secondary draw order of `fire`, so this is drawn below `fire`.
