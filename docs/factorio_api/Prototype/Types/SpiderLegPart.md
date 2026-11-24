---
title: SpiderLegPart
tags: [factorio-api, prototype, type]
---
# SpiderLegPart

## Properties

### top_end
- **Type:** [[RotatedSprite]]
- **Optional**

### middle
- **Type:** [[RotatedSprite]]
- **Optional**

### bottom_end
- **Type:** [[RotatedSprite]]
- **Optional**

### middle_offset_from_top
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### middle_offset_from_bottom
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### top_end_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### bottom_end_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### top_end_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The number of tiles in screen space to shift the top end of the leg part AWAY from the top joint.

### bottom_end_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The number of tiles in screen space to shift the bottom end of the leg part AWAY from the bottom joint.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"higher-object-above"`
The sprite layer in which to draw this leg part.
