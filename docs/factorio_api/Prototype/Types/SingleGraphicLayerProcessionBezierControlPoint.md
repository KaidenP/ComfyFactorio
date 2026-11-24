---
title: SingleGraphicLayerProcessionBezierControlPoint
tags: [factorio-api, prototype, type]
---
# SingleGraphicLayerProcessionBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `opacity` or `tint` is defined.

### opacity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
`opacity` and `opacity_t` interpolate a double smoothly over time.

### opacity_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** {1.0, 1.0, 1.0, 1.0}
`tint` and `tint_t` interpolate a color smoothly over time.

### tint_t
- **Type:** [[Color (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### rotation
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
`rotation` and `rotation_t` interpolate a double smoothly over time.

### rotation_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
`scale` and `scale_t` interpolate a double smoothly over time.

### scale_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** {0.0, 0.0}
`shift` and `shift_t` interpolate a vector smoothly over time using `shift_rate` and `shift_rate_t` for a 0-1 rate curve.

Vector value.

### shift_t
- **Type:** [[Vector (type)]]
- **Optional**
Vector tangent.

### shift_rate
- **Type:** [[double (type)]]
- **Optional**
Rate 0-1 value.

### shift_rate_t
- **Type:** [[double (type)]]
- **Optional**
Rate tangent.

### frame
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`
the frame of the pod animation played. Used only when 'animation_driven_by_curve' is enabled.
