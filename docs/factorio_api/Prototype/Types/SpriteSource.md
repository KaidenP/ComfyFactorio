---
title: SpriteSource
tags: [factorio-api, prototype, type]
---
# SpriteSource

> **Abstract**

## Properties

### filename
- **Type:** [[FileName]]
The path to the sprite file to use.

### size
- **Type:** [[SpriteSizeType]] | ([[SpriteSizeType]], [[SpriteSizeType]])
- **Optional**
The width and height of the sprite. If this is a tuple, the first member of the tuple is the width and the second is the height. Otherwise the size is both width and height. Width and height may only be in the range of 0-4096.

### width
- **Type:** [[SpriteSizeType]]
- **Optional**
Mandatory if `size` is not defined.

Width of the sprite in pixels, from 0-4096.

### height
- **Type:** [[SpriteSizeType]]
- **Optional**
Mandatory if `size` is not defined.

Height of the sprite in pixels, from 0-4096.

### x
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Horizontal position of the sprite in the source file in pixels.

### y
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `0`
Vertical position of the sprite in the source file in pixels.

### position
- **Type:** ([[SpriteSizeType]], [[SpriteSizeType]])
- **Optional**
Loaded only when `x` and `y` are both `0`. The first member of the tuple is `x` and the second is `y`.

### load_in_minimal_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Minimal mode is entered when mod loading fails. You are in it when you see the gray box after (part of) the loading screen that tells you a mod error. Modders can ignore this property.

### premul_alpha
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether alpha should be pre-multiplied.

### allow_forced_downscale
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the sprite may be downsampled to half its size on load even when 'Sprite quality' graphics setting is set to 'High'. Whether downsampling happens depends on detected hardware and other graphics settings.

### color_channels
- **Type:** `1` | `2` | `3` | `4`
- **Optional**
- **Default:** `4`
All textures have 4 channels by default. This property can be used for no-atlas textures to force their format to R, RG, RGB or RGBA with 8 bytes for each channel and save VRAM space. Compression setting is based on player config.

We use BC4 compression for R, BC5 for RG, BC1 for RGB, and DXT5_BC3 for RGBA, see "[S3 Texture Compression](https://en.wikipedia.org/wiki/S3_Texture_Compression)" to read more about compression ratios.
