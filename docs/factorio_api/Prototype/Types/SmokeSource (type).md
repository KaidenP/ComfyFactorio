---
title: SmokeSource
tags: [factorio-api, prototype, type]
---
# SmokeSource

*Note: `SmokeSource (type)`.*

Definition of the smoke of an entity.

## Properties

### name
- **Type:** [[TrivialSmokeID (type)]]

### frequency
- **Type:** [[float (type)]]
Number of smokes generated per entity animation cycle (or per tick for some entities). Can't be negative or infinite.

### offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Offsets animation cycle, to move at which points of the cycle the smoke gets emitted.

### position
- **Type:** [[Vector (type)]]
- **Optional**
Positional offset of smoke source relative to owner entity position. The vector is rotated by orientation of the entity.

If any of `north_position`, `north_east_position`, `east_position`, `south_east_position`, `south_position`, `south_west_position`, `west_position`, `north_west_position` is defined, `position` is used only as default value for directional positions. Orientation of the owner entity will be rounded to 4 or 8 directions and one of the directional positions will be used as the offset instead of `position`.

### has_8_directions
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### north_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position`

### north_east_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated north-east
Only loaded if `has_8_directions` is `true`.

### east_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated east

### south_east_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated south-east
Only loaded if `has_8_directions` is `true`.

### south_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated south

### south_west_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated south-west
Only loaded if `has_8_directions` is `true`.

### west_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated west

### north_west_position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** Value of `position` rotated north-west
Only loaded if `has_8_directions` is `true`.

### deviation
- **Type:** [[Vector (type)]]
- **Optional**

### starting_frame
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### starting_frame_deviation
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### height_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### starting_vertical_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### starting_vertical_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### vertical_speed_slowdown
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.965`
A value between `0` and `1`.
