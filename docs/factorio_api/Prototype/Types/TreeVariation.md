---
title: TreeVariation
tags: [factorio-api, prototype, type]
---
# TreeVariation

Tree has number of "dying" stages, which is deduced from frame count of `shadow` if shadow is defined, otherwise from frame count of `trunk`. The frame count of `leaves` has to be one less than the deduced number of stages, as the last stage is always assumed to be leafless.

## Properties

### trunk
- **Type:** [[Animation]]
If `shadow` is not specified, this has to have one more frame than `leaves`.

### leaves
- **Type:** [[Animation]]

### leaf_generation
- **Type:** [[CreateParticleTriggerEffectItem]]

### branch_generation
- **Type:** [[CreateParticleTriggerEffectItem]]

### shadow
- **Type:** [[Animation]]
- **Optional**
Shadow must have 1 more `frame_count` than `leaves`.

### disable_shadow_distortion_beginning_at_frame
- **Type:** [[uint32 (type)]]
- **Optional**
Only loaded if `shadow` is present. Defaults to `shadow.frame_count - 1`.

### normal
- **Type:** [[Animation]]
- **Optional**
Normal must have the same frame_count as `leaves`.

### overlay
- **Type:** [[Animation]]
- **Optional**
Overlay must have the same frame_count as `leaves`. Won't be tinted by the tree color unless `apply_runtime_tint` is set to `true` in the sprite definition. See [here](https://forums.factorio.com/viewtopic.php?p=547758#p547758).

### underwater
- **Type:** [[Animation]]
- **Optional**

### underwater_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `1`

### leaves_when_mined_manually
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `40`

### leaves_when_mined_automatically
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`

### leaves_when_damaged
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `200`
This value is multiplied with the percent of health lost.

### leaves_when_destroyed
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `40`

### branches_when_mined_manually
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `15`

### branches_when_mined_automatically
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `8`

### branches_when_damaged
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
This value is multiplied with the percent of health lost.

### branches_when_destroyed
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `15`

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
