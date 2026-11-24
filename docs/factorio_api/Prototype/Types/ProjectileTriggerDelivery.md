---
title: ProjectileTriggerDelivery
tags: [factorio-api, prototype, type]
---
# ProjectileTriggerDelivery

> **Parent:** [[TriggerDeliveryItem]]

## Properties

### type
- **Type:** `"projectile"`

### projectile
- **Type:** [[EntityID (type)]]
Name of a [[ProjectilePrototype]].

### starting_speed
- **Type:** [[float (type)]]
Starting speed in tiles per tick.

### starting_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### direction_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Maximum deviation of the projectile from source orientation, in +/- (`x radians / 2`). Example: `3.14 radians -> +/- (180° / 2)`, meaning up to 90° deviation in either direction of rotation.

### range_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The maximum deviation of the projectile maximum range from `max_range` is `max_range × range_deviation ÷ 2`. This means a deviation of `0.5` will appear as a maximum of `0.25` (25%) deviation of an initial range goal. Post-deviation range may exceed `max_range` or be less than `min_range`.

### max_range
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1000`

### min_range
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### inherit_speed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the projectile will inherit any positive speed component from the source entity's movement toward the target.
