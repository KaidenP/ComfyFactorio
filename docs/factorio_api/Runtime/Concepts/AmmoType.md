---
title: AmmoType
tags: [factorio-api, runtime, concept]
---
# AmmoType

## Fields

### action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### target_type
- **Type:** [[TargetType]]

### clamp_position
- **Type:** [[boolean]]
- **Optional**
When `true`, the gun will be able to shoot even when the target is out of range. Only applies when `target_type` is `position`. The gun will fire at the maximum range in the direction of the target position. Defaults to `false`.

### energy_consumption
- **Type:** [[double]]
- **Optional**
Energy consumption of a single shot, if applicable. Defaults to `0`.

### range_modifier
- **Type:** [[double]]
- **Optional**

### cooldown_modifier
- **Type:** [[double]]
- **Optional**

### consumption_modifier
- **Type:** [[float]]
- **Optional**

### target_filter
- **Type:** array<[[string]]>
- **Optional**
The entity prototype filter names.
