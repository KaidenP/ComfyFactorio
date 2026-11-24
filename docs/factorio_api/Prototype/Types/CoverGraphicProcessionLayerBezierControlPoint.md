---
title: CoverGraphicProcessionLayerBezierControlPoint
tags: [factorio-api, prototype, type]
---
# CoverGraphicProcessionLayerBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `opacity` or `rotation` or `effect_scale_min` or `effect_scale_max` is defined.

### opacity
- **Type:** [[double (type)]]
- **Optional**
`opacity` and `opacity_t` interpolate a double smoothly over time.

### opacity_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### rotation
- **Type:** [[double (type)]]
- **Optional**
`rotation` and `rotation_t` interpolate a double smoothly over time.

### rotation_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### effect_scale_min
- **Type:** [[double (type)]]
- **Optional**
`effect_scale_min` and `effect_scale_min_t` interpolate a double smoothly over time.

### effect_scale_min_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### effect_scale_max
- **Type:** [[double (type)]]
- **Optional**
`effect_scale_max` and `effect_scale_max_t` interpolate a double smoothly over time.

### effect_scale_max_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### alt_effect_scale_min
- **Type:** [[double (type)]]
- **Optional**
`alt_effect_scale_min` and `alt_effect_scale_min_t` interpolate a double smoothly over time.

### alt_effect_scale_min_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### alt_effect_scale_max
- **Type:** [[double (type)]]
- **Optional**
`alt_effect_scale_max` and `alt_effect_scale_max_t` interpolate a double smoothly over time.

### alt_effect_scale_max_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

### effect_shift
- **Type:** [[Vector (type)]]
- **Optional**
`effect_shift` and `effect_shift_t` interpolate a vector smoothly over time using `effect_shift_rate` and `effect_shift_rate_t` for a 0-1 rate curve.

Vector value.

### effect_shift_t
- **Type:** [[Vector (type)]]
- **Optional**
Vector tangent.

### effect_shift_rate
- **Type:** [[double (type)]]
- **Optional**
Rate 0-1 value.

### effect_shift_rate_t
- **Type:** [[double (type)]]
- **Optional**
Rate tangent.

### alt_effect_shift
- **Type:** [[Vector (type)]]
- **Optional**
`alt_effect_shift` and `alt_effect_shift_t` interpolate a vector smoothly over time using `alt_effect_shift_rate` and `alt_effect_shift_rate_t` for a 0-1 rate curve.

Vector value.

### alt_effect_shift_t
- **Type:** [[Vector (type)]]
- **Optional**
Vector tangent.

### alt_effect_shift_rate
- **Type:** [[double (type)]]
- **Optional**
Rate 0-1 value.

### alt_effect_shift_rate_t
- **Type:** [[double (type)]]
- **Optional**
Rate tangent.

### offset
- **Type:** [[Vector (type)]]
- **Optional**
`offset` and `offset_t` interpolate a vector smoothly over time using `offset_rate` and `offset_rate_t` for a 0-1 rate curve.

Vector value.

### offset_t
- **Type:** [[Vector (type)]]
- **Optional**
Vector tangent.

### offset_rate
- **Type:** [[double (type)]]
- **Optional**
Rate 0-1 value.

### offset_rate_t
- **Type:** [[double (type)]]
- **Optional**
Rate tangent.
