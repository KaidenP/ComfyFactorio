---
title: AnimationElement
tags: [factorio-api, prototype, type]
---
# AnimationElement

## Properties

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
Used to determine render order for sprites with the same `render_layer` in the same position. Sprites with a higher `secondary_draw_order` are drawn on top.

### apply_tint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### always_draw
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### animation
- **Type:** [[Animation]]
- **Optional**
