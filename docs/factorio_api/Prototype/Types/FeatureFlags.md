---
title: FeatureFlags
tags: [factorio-api, prototype, type]
---
# FeatureFlags

> **Abstract**

A dictionary of feature flags and their status. It can be used to adjust prototypes based on whether the feature flags are enabled. It is accessible through the global object named `feature_flags`.

See the [[mod-structure|mod structure]] documentation for more information on what each feature flag affects.

## Properties

### expansion
- **Type:** [[boolean (type)]]

### quality
- **Type:** [[boolean (type)]]

### rail_bridges
- **Type:** [[boolean (type)]]

### space_travel
- **Type:** [[boolean (type)]]

### spoiling
- **Type:** [[boolean (type)]]

### freezing
- **Type:** [[boolean (type)]]

### segmented_units
- **Type:** [[boolean (type)]]

### expansion_shaders
- **Type:** [[boolean (type)]]

## Examples

```
-- sets coal to spoil only when the spoiling feature flag is enabled
if feature_flags["spoiling"] then
  data.raw.item.coal.spoil_ticks = 600
end
```
