---
title: RotatedAnimation
tags: [factorio-api, prototype, type]
---
# RotatedAnimation

> **Parent:** [[AnimationParameters]]

## Properties

### layers
- **Type:** array<[[RotatedAnimation]]>
- **Optional**
If this property is present, all RotatedAnimation definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

If this property is present, all other properties, including those inherited from AnimationParameters, are ignored.

### direction_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

The sequential animation instance is loaded equal to the entities direction within the `direction_count` setting.

Direction count to [[defines.direction]] (animation sequence number):

- `1`: North (1)

- `2`: North (1), South (2)

- `4`: North (1), East (2), South (3), West (4)

- `8`: North (1), Northeast (2), East (3), Southeast (4), South (5), Southwest (6), West (7), Northwest (8)

### filename
- **Type:** [[FileName]]
- **Optional**
- **Overrides parent**
Only loaded, and mandatory if `layers`, `stripes`, and `filenames` are not defined.

The path to the sprite file to use.

### filenames
- **Type:** array<[[FileName]]>
- **Optional**
Only loaded if both `layers` and `stripes` are not defined.

### lines_per_file
- **Type:** [[uint32 (type)]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `filenames` is defined.

### slice
- **Type:** [[uint32 (type)]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `filenames` is defined.

### still_frame
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `layers` is not defined.

### counterclockwise
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `layers` is not defined.

### middle_orientation
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** `0.5`
Only loaded if `layers` is not defined.

### orientation_range
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `layers` is not defined.

Automatically clamped to be between `0` and `1`.

### apply_projection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Used to fix the inconsistency of direction of the entity in 3d when rendered and direction on the screen (where the 45 degree angle for projection is used).

Only loaded if `layers` is not defined.

### stripes
- **Type:** array<[[Stripe]]>
- **Optional**
Only loaded if `layers` is not defined.
