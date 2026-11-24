---
title: PrototypeStrafeSettings
tags: [factorio-api, prototype, type]
---
# PrototypeStrafeSettings

*Note: `PrototypeStrafeSettings (type)`.*

Used by [[UnitPrototype]].

## Properties

### max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `20`
Must be >= `0`.

### ideal_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `10`
Must be between 0 and max_distance inclusive.

### ideal_distance_tolerance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.5`
Must be >= `0`.

### ideal_distance_variance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Must be >= `0`.

### ideal_distance_importance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
Must be between between 0 and 1 inclusive.

### ideal_distance_importance_variance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`
Must be between 0 and ideal_distance_importance inclusive.

### clockwise_chance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
Must be between 0 and 1 inclusive.

### face_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
