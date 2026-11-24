---
title: PodDistanceTraveledProcessionLayer
tags: [factorio-api, prototype, type]
---
# PodDistanceTraveledProcessionLayer

## Properties

### type
- **Type:** `"pod-distance-traveled"`

### reference_group
- **Type:** [[ProcessionLayerInheritanceGroupID]]
- **Optional**
The group this layer belongs to, for inheritance.

### contribute_to_distance_traveled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### distance_traveled_contribution
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### frames
- **Type:** array<[[PodDistanceTraveledProcessionBezierControlPoint]]>
