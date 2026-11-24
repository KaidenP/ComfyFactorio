---
title: PumpWagonConnectionGraphics
tags: [factorio-api, prototype, type]
---
# PumpWagonConnectionGraphics

## Properties

### base_animation_finished_at_progress
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.5`
Value between 0 and 1 (both exclusive). The base animation will play up until the connecting progress reaches the value. Needs to be less than `clamp_animation_starts_at_progress`. The arm (`part_1` and `part_2`) will rotate and extend in the time in between.

### clamp_animation_starts_at_progress
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.75`
Value between 0 and 1 (both exclusive). The clamp animation will play up starting when the connecting progress reaches the value. Needs to be larger than `base_animation_finished_at_progress`. The arm (`part_1` and `part_2`) will rotate and extend in the time in between.

### height_diff_to_wagon
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.15`

### part2_crop_adjustment
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.05`
Adjusts where the sprites will be cropped

### part2_shadow_crop_adjustment
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.05`
Adjusts where the sprites will be cropped

### clamp_y_shift
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.375`

### base
- **Type:** [[BasePumpWagonConnectionAnimations]]
- **Optional**

### part_1
- **Type:** [[RotatedSprite]]
- **Optional**
Rotating top part.

### part_1_shadow
- **Type:** [[RotatedSprite]]
- **Optional**

### part_2
- **Type:** [[RotatedSprite]]
- **Optional**
Rotating arm.

### part_2_shadow
- **Type:** [[RotatedSprite]]
- **Optional**

### suction_clamp
- **Type:** [[Animation]]
- **Optional**

### suction_clamp_shadow
- **Type:** [[Animation]]
- **Optional**

### part1_to_2_shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`

### top_pivot_shift
- **Type:** [[PumpWagonConnectionShift4Way]]
- **Optional**
Relative projected render position of `part_1` to the parent pump position.

### resting_position_shift
- **Type:** [[PumpWagonConnectionShift4Way]]
- **Optional**
Projected render rest position of `suction_clamp` relative to the parent pump position.

### shadow_shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0.8, 1.55}`
