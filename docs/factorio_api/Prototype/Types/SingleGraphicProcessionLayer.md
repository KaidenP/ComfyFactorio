---
title: SingleGraphicProcessionLayer
tags: [factorio-api, prototype, type]
---
# SingleGraphicProcessionLayer

## Properties

### type
- **Type:** `"single-graphic"`

### graphic
- **Type:** [[ProcessionGraphic]]

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### relative_to
- **Type:** [[EffectRelativeTo]]
- **Optional**
- **Default:** `"pod"`
Where the sprite is centered.

### compensated_pivot
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Swaps the order of sprite shift and rotation.

### rotates_with_pod
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### shift_rotates_with_pod
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only applied when the `relative_to` is `pod`.

### is_passenger_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### clip_with_hatches
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### animation_driven_by_curve
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### frames
- **Type:** array<[[SingleGraphicLayerProcessionBezierControlPoint]]>
