---
title: PodDistanceTraveledProcessionBezierControlPoint
tags: [factorio-api, prototype, type]
---
# PodDistanceTraveledProcessionBezierControlPoint

> **Inline**

One frame in time for a Bezier interpolation.

## Properties

### timestamp
- **Type:** [[MapTick (type)]]
- **Optional**
Mandatory if `distance` is defined.

### distance
- **Type:** [[double (type)]]
- **Optional**
`distance` and `distance_t` interpolate a double smoothly over time.

### distance_t
- **Type:** [[double (type)]]
- **Optional**
Bidirectional tangent at the given timestamp.
