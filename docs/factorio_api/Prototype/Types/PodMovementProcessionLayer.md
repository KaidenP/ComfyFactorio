---
title: PodMovementProcessionLayer
tags: [factorio-api, prototype, type]
---
# PodMovementProcessionLayer

## Properties

### type
- **Type:** `"pod-movement"`

### reference_group
- **Type:** [[ProcessionLayerInheritanceGroupID]]
- **Optional**
The group this layer belongs to, for inheritance.

### inherit_from
- **Type:** [[ProcessionLayerInheritanceGroupID]]
- **Optional**
Adds the final position value from given layer to this one.

### contribute_to_distance_traveled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### distance_traveled_contribution
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### frames
- **Type:** array<[[PodMovementProcessionBezierControlPoint]]>

## Examples

```
{
  type = "pod-movement",
  frames =
  {
    { timestamp = 700 , tilt = 0.0               , tilt_t = 0 },
    { timestamp = 700 , offset = {0, 0 - 500}    , offset_t = {0, -40} },
    { timestamp = 900 , offset = {15, -60 - 500} , offset_t = {-10, -10} },
    { timestamp = 900 , opacity = 1.0 },
    { timestamp = 960 , tilt = 0.05              , tilt_t = -0.03 },
    { timestamp = 1050, tilt = 0.25              , tilt_t = 0 },
    { timestamp = 1050, offset = {40, -70 - 500} , offset_t = {-1, 0} },
    { timestamp = 1050, opacity = 0.0 },
    { timestamp = 700 , offset_rate = 0 },
    { timestamp = 1050, offset_rate = 1.0 }
  }
}
```
