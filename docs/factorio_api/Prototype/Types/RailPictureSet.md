---
title: RailPictureSet
tags: [factorio-api, prototype, type]
---
# RailPictureSet

## Properties

### north
- **Type:** [[RailPieceLayers]]

### northeast
- **Type:** [[RailPieceLayers]]

### east
- **Type:** [[RailPieceLayers]]

### southeast
- **Type:** [[RailPieceLayers]]

### south
- **Type:** [[RailPieceLayers]]

### southwest
- **Type:** [[RailPieceLayers]]

### west
- **Type:** [[RailPieceLayers]]

### northwest
- **Type:** [[RailPieceLayers]]

### front_rail_endings
- **Type:** [[Sprite16Way]]
- **Optional**
- **Default:** Value of `rail_endings`

### back_rail_endings
- **Type:** [[Sprite16Way]]
- **Optional**
- **Default:** Value of `rail_endings`

### rail_endings
- **Type:** [[Sprite16Way]]
- **Optional**
Can be used to load rail endings instead of the front and back variants.

Only loaded if `front_rail_endings` or `back_rail_endings` are not defined.

### segment_visualisation_endings
- **Type:** [[RotatedAnimation]]
- **Optional**
Must contain exactly 16 directions and 6 frames.

### render_layers
- **Type:** [[RailRenderLayers]]

### secondary_render_layers
- **Type:** [[RailRenderLayers]]
- **Optional**
- **Default:** Value of `render_layers`

### slice_origin
- **Type:** [[RailsSliceOffsets]]
- **Optional**

### fog_mask
- **Type:** [[RailsFogMaskDefinitions]]
- **Optional**
