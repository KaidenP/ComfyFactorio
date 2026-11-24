---
title: TileSpriteLayout
tags: [factorio-api, prototype, type]
---
# TileSpriteLayout

> **Abstract**

## Properties

### picture
- **Type:** [[FileName]]

### scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

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

### line_length
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Once the specified number of pictures is loaded, other pictures are loaded on other line. This is to allow having longer animations in matrix, to input files with too high width. The game engine limits the width of any input files to 8192px, so it is compatible with most graphics cards. 0 means that all the pictures are in one horizontal line.

### count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Frame count.
