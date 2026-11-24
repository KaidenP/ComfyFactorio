---
title: PodMovementProcessionBezierControlPoint
tags: [factorio-api, prototype, type]
---
# PodMovementProcessionBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `tilt` is defined.

### tilt
- **Type:** [[double (type)]]
- **Optional**
`tilt` and `tilt_t` interpolate a double smoothly over time.

### tilt_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.

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
