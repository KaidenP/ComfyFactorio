---
title: SpriteParameters
tags: [factorio-api, prototype, type]
---
# SpriteParameters

> **Parent:** [[SpriteSource]] · **Abstract**

## Properties

### priority
- **Type:** [[SpritePriority]]
- **Optional**
- **Default:** `"medium"`

### flags
- **Type:** [[SpriteFlags]]
- **Optional**

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
The shift in tiles. `util.by_pixel()` can be used to divide the shift by 32 which is the usual pixel height/width of 1 tile in normal resolution. Note that 32 pixel tile height/width is not enforced anywhere - any other tile height or width is also possible.

### rotate_shift
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether to rotate the `shift` alongside the sprite's rotation. This only applies to sprites which are procedurally rotated by the game engine (like projectiles, wires, inserter hands, etc).

### apply_special_effect
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Values other than `1` specify the scale of the sprite on default zoom. A scale of `2` means that the picture will be two times bigger on screen (and thus more pixelated).

### draw_as_shadow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true. This takes precedence over `draw_as_glow` and `draw_as_light`.

### draw_as_glow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true. This takes precedence over `draw_as_light`.

Draws first as a normal sprite, then again as a light layer. See [https://forums.factorio.com/91682](https://forums.factorio.com/91682).

### draw_as_light
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true.

### occludes_light
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Loaded only if `draw_as_shadow`, `draw_as_glow` and `draw_as_light` are `false`, and only by sprites used by tile renderer (decals and underwater patches). The purpose of setting this to `false` is to preserve water mask from sprites that are supposed to be drawn under the water.

### mipmap_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if this is an icon, that is it has the flag `"group=icon"` or `"group=gui"`. Will be clamped to range `[0, 5]`.

### apply_runtime_tint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### tint_as_overlay
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### invert_colors
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1}`

### blend_mode
- **Type:** [[BlendMode]]
- **Optional**
- **Default:** `"normal"`

### generate_sdf
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
This property is only used by sprites used in [[UtilitySprites]] that have the `"icon"` flag set.

If this is set to `true`, the game will generate an icon shadow (using signed distance fields) for the sprite.

![[Generate_sdf_example.png]]
*Example of the icon shadow in the character modifier icon used by the steel axe research*

### surface
- **Type:** [[SpriteUsageSurfaceHint]]
- **Optional**
- **Default:** `"any"`
Provides hint to sprite atlas system, so it can try to put sprites that are intended to be used at the same locations to the same sprite atlas.

### usage
- **Type:** [[SpriteUsageHint]]
- **Optional**
- **Default:** `"any"`
Provides hint to sprite atlas system, so it can pack sprites that are related to each other to the same sprite atlas.
