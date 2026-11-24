---
title: SpritePrototype
tags: [factorio-api, prototype]
---
# SpritePrototype

> **Type name:** `sprite`

Specifies an image that can be used with [[SpritePath]] at runtime.

## Properties

### type
- **Type:** `"sprite"`

### name
- **Type:** [[string (type)]]
Name of the sprite. Can be used as a [[SpritePath]] at runtime.

### layers
- **Type:** array<[[Sprite]]>
- **Optional**
If this property is present, all Sprite definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

If this property is present, all other properties besides `name` and `type` are ignored.

### filename
- **Type:** [[FileName]]
- **Optional**
Only loaded, and mandatory if `layers` is not defined.

The path to the sprite file to use.

### dice
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Number of slices this is sliced into when using the "optimized atlas packing" option. If you are a modder, you can just ignore this property. Example: If this is 4, the sprite will be sliced into a 4x4 grid.

### dice_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Same as `dice` above, but this specifies only how many slices there are on the x axis.

### dice_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined.

Same as `dice` above, but this specifies only how many slices there are on the y axis.

### priority
- **Type:** [[SpritePriority]]
- **Optional**
- **Default:** `"medium"`
Only loaded if `layers` is not defined.

### flags
- **Type:** [[SpriteFlags]]
- **Optional**
Only loaded if `layers` is not defined.

### size
- **Type:** [[SpriteSizeType]] | ([[SpriteSizeType]], [[SpriteSizeType]])
- **Optional**
Only loaded if `layers` is not defined.

The width and height of the sprite. If this is a tuple, the first member of the tuple is the width and the second is the height. Otherwise the size is both width and height. Width and height may only be in the range of 0-4096.

### width
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `size` is not defined.

Width of the picture in pixels, from 0-4096.

### height
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `size` is not defined.

Height of the picture in pixels, from 0-4096.

### x
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Horizontal position of the sprite in the source file in pixels.

### y
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Vertical position of the sprite in the source file in pixels.

### position
- **Type:** ([[SpriteSizeType]], [[SpriteSizeType]])
- **Optional**
Only loaded if `layers` is not defined.

Loaded only when `x` and `y` are both `0`. The first member of the tuple is `x` and the second is `y`.

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Only loaded if `layers` is not defined.

The shift in tiles. `util.by_pixel()` can be used to divide the shift by 32 which is the usual pixel height/width of 1 tile in normal resolution. Note that 32 pixel tile height/width is not enforced anywhere - any other tile height or width is also possible.

### rotate_shift
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### apply_special_effect
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

Values other than `1` specify the scale of the sprite on default zoom. A scale of `2` means that the picture will be two times bigger on screen (and thus more pixelated).

### draw_as_shadow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true. This takes precedence over `draw_as_glow` and `draw_as_light`.

### draw_as_glow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true. This takes precedence over `draw_as_light`.

Draws first as a normal sprite, then again as a light layer. See [https://forums.factorio.com/91682](https://forums.factorio.com/91682).

### draw_as_light
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Only one of `draw_as_shadow`, `draw_as_glow` and `draw_as_light` can be true.

### mipmap_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Only loaded if this is an icon, that is it has the flag `"group=icon"` or `"group=gui"`.

### apply_runtime_tint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### tint_as_overlay
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### invert_colors
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1}`
Only loaded if `layers` is not defined.

### blend_mode
- **Type:** [[BlendMode]]
- **Optional**
- **Default:** `"normal"`
Only loaded if `layers` is not defined.

### load_in_minimal_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Minimal mode is entered when mod loading fails. You are in it when you see the gray box after (part of) the loading screen that tells you a mod error. Modders can ignore this property.

### premul_alpha
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only loaded if `layers` is not defined.

Whether alpha should be pre-multiplied.

### allow_forced_downscale
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

If `true`, the sprite may be downsampled to half its size on load even when 'Sprite quality' graphics setting is set to 'High'. Whether downsampling happens depends on detected hardware and other graphics settings.

### generate_sdf
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

Unused.

### surface
- **Type:** [[SpriteUsageSurfaceHint]]
- **Optional**
- **Default:** `"any"`
Only loaded if `layers` is not defined.

Provides hint to sprite atlas system, so it can try to put sprites that are intended to be used at the same locations to the same sprite atlas.

### usage
- **Type:** [[SpriteUsageHint]]
- **Optional**
- **Default:** `"any"`
Only loaded if `layers` is not defined.

Provides hint to sprite atlas system, so it can pack sprites that are related to each other to the same sprite atlas.

## Example

```
{
  type = "sprite"
  name = "accumulator-sprite",
  filename = "__base__/graphics/entity/basic-accumulator/basic-accumulator.png",
  priority = "extra-high",
  width = 124,
  height = 103,
  shift = {0.7, -0.2}
}
```
