---
title: TileMainPictures
tags: [factorio-api, prototype, type]
---
# TileMainPictures

> **Parent:** [[TileSpriteLayout]]

## Properties

### size
- **Type:** [[uint32 (type)]]
Only powers of 2 from 1 to 128 can be used. Square size of the tile arrangement this sprite is used for. Used to calculate the `width` and `height` of the sprite which cannot be set directly. (width or height) = size * 32 / scale.

### probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
Probability of 1x1 (size = 1) version of tile must be 1.

### weights
- **Type:** array<[[double (type)]]>
- **Optional**
