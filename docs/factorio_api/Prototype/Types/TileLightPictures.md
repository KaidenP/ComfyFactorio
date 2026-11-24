---
title: TileLightPictures
tags: [factorio-api, prototype, type]
---
# TileLightPictures

> **Parent:** [[TileSpriteLayout]]

## Properties

### size
- **Type:** [[uint32 (type)]]
Only powers of 2 from 1 to 128 can be used. Square size of the tile arrangement this sprite is used for. Used to calculate the `width` and `height` of the sprite which cannot be set directly. (width or height) = size * 32 / scale.
