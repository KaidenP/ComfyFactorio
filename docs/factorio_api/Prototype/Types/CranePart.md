---
title: CranePart
tags: [factorio-api, prototype, type]
---
# CranePart

## Properties

### orientation_shift
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Angle in radian, which is internally converted to a [[RealOrientation (type)|RealOrientation]].

### is_contractible_by_cropping
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### should_scale_for_perspective
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### scale_to_fit_model
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### allow_sprite_rotation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### snap_start
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### snap_end
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### snap_end_arm_extent_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### name
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`

### dying_effect
- **Type:** [[CranePartDyingEffect]]
- **Optional**

### relative_position
- **Type:** [[Vector3D (type)]]
- **Optional**

### relative_position_grappler
- **Type:** [[Vector3D (type)]]
- **Optional**

### static_length
- **Type:** [[Vector3D (type)]]
- **Optional**

### extendable_length
- **Type:** [[Vector3D (type)]]
- **Optional**

### static_length_grappler
- **Type:** [[Vector3D (type)]]
- **Optional**

### extendable_length_grappler
- **Type:** [[Vector3D (type)]]
- **Optional**

### sprite
- **Type:** [[Sprite]]
- **Optional**

### rotated_sprite
- **Type:** [[RotatedSprite]]
- **Optional**
Only loaded if `sprite` is not defined.

### sprite_shadow
- **Type:** [[Sprite]]
- **Optional**

### rotated_sprite_shadow
- **Type:** [[RotatedSprite]]
- **Optional**
Only loaded if `sprite_shadow` is not defined.

### sprite_reflection
- **Type:** [[Sprite]]
- **Optional**

### rotated_sprite_reflection
- **Type:** [[RotatedSprite]]
- **Optional**
Only loaded if `sprite_reflection` is not defined.

### layer
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
