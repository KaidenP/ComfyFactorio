---
title: TintProcessionBezierControlPoint
tags: [factorio-api, prototype, type]
---
# TintProcessionBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `opacity` or `tint_upper` or `tint_lower` is defined.

### opacity
- **Type:** [[double (type)]]
- **Optional**
`opacity` and `opacity_t` interpolate a double smoothly over time.

### opacity_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### tint_upper
- **Type:** [[Color (type)]]
- **Optional**
`tint_upper` and `tint_upper_t` interpolate a color smoothly over time.

### tint_upper_t
- **Type:** [[Color (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### tint_lower
- **Type:** [[Color (type)]]
- **Optional**
`tint_lower` and `tint_lower_t` interpolate a color smoothly over time.

### tint_lower_t
- **Type:** [[Color (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.
