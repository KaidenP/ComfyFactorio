---
title: PodOpacityProcessionBezierControlPoint
tags: [factorio-api, prototype, type]
---
# PodOpacityProcessionBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `cutscene_opacity` or `outside_opacity` is defined.

### cutscene_opacity
- **Type:** [[double (type)]]
- **Optional**
`cutscene_opacity` and `cutscene_opacity_t` interpolate a double smoothly over time.

### cutscene_opacity_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### outside_opacity
- **Type:** [[double (type)]]
- **Optional**
`outside_opacity` and `outside_opacity_t` interpolate a double smoothly over time.

### outside_opacity_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### lut_blend
- **Type:** [[double (type)]]
- **Optional**
`lut_blend` and `lut_blend_t` interpolate a double smoothly over time.

LUT won't be overridden however, until the pod is drawn above the game via `draw_switch_tick`.

### lut_blend_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.
