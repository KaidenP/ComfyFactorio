---
title: AnimationPrototype
tags: [factorio-api, prototype]
---
# AnimationPrototype

> **Type name:** `animation`

Specifies an animation that can be used with [[LuaRendering#draw_animation|LuaRendering::draw_animation]] at runtime.

## Properties

### type
- **Type:** `"animation"`

### name
- **Type:** [[string (type)]]
Name of the animation. Can be used with [[LuaRendering#draw_animation|LuaRendering::draw_animation]] at runtime.

### layers
- **Type:** array<[[Animation]]>
- **Optional**
If this property is present, all Animation definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

`animation_speed` and `max_advance` of the first layer are used for all layers. All layers will run at the same speed.

If this property is present, all other properties besides `name` and `type` are ignored.

### filename
- **Type:** [[FileName]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if neither `stripes` nor `filenames` are defined.

The path to the sprite file to use.

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

The width and height of one frame. If this is a tuple, the first member of the tuple is the width and the second is the height. Otherwise the size is both width and height. Width and height may only be in the range of 0-4096.

### width
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `size` is not defined.

Width of one frame in pixels, from 0-4096.

### height
- **Type:** [[SpriteSizeType]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `size` is not defined.

Height of one frame in pixels, from 0-4096.

### x
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Horizontal position of the animation in the source file in pixels.

### y
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Vertical position of the animation in the source file in pixels.

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

Note that `mipmap_count` doesn't make sense in an animation, as it is not possible to layout mipmaps in a way that would load both the animation and the mipmaps correctly (besides animations with just one frame). See [here](https://forums.factorio.com/viewtopic.php?p=549058#p549058).

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

### run_mode
- **Type:** [[AnimationRunMode]]
- **Optional**
- **Default:** `"forward"`
Only loaded if `layers` is not defined.

### frame_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

Can't be `0`.

### line_length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

Once the specified number of pictures is loaded, other pictures are loaded on other line. This is to allow having longer animations in matrix, to input files with too high width. The game engine limits the width of any input files to 8192px, so it is compatible with most graphics cards. `0` means that all the pictures are in one horizontal line.

### animation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

Modifier of the animation playing speed, the default of `1` means one animation frame per tick (60 fps). The speed of playing can often vary depending on the usage (output of steam engine for example). Has to be greater than `0`.

If `layers` are used, the `animation_speed` only has to be defined in one layer. All layers will run at the same speed.

### max_advance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** MAX_FLOAT
Only loaded if `layers` is not defined.

If `layers` are used, `max_advance` of the first layer is used for all layers.

Maximum amount of frames the animation can move forward in one update.

### repeat_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

How many times to repeat the animation to complete an animation cycle. E.g. if one layer is 10 frames, a second layer of 1 frame would need `repeat_count = 10` to match the complete cycle.

### dice
- **Type:** [[uint8 (type)]]
- **Optional**
Only loaded if `layers` is not defined.

### dice_x
- **Type:** [[uint8 (type)]]
- **Optional**
Only loaded if `layers` is not defined.

### dice_y
- **Type:** [[uint8 (type)]]
- **Optional**
Only loaded if `layers` is not defined.

### frame_sequence
- **Type:** [[AnimationFrameSequence]]
- **Optional**
Only loaded if `layers` is not defined.

### stripes
- **Type:** array<[[Stripe]]>
- **Optional**
Only loaded if `layers` is not defined.

### filenames
- **Type:** array<[[FileName]]>
- **Optional**
Only loaded if neither `layers` nor `stripes` are defined.

### slice
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `frame_count`
Only loaded if `layers` is not defined and if `filenames` is defined.

### lines_per_file
- **Type:** [[uint32 (type)]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `filenames` is defined.
