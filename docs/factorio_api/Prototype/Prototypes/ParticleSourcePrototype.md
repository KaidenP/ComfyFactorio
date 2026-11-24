---
title: ParticleSourcePrototype
tags: [factorio-api, prototype]
---
# ParticleSourcePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `particle-source`

Creates particles.

## Properties

### time_to_live
- **Type:** [[float (type)]]

### time_before_start
- **Type:** [[float (type)]]

### height
- **Type:** [[float (type)]]

### vertical_speed
- **Type:** [[float (type)]]

### horizontal_speed
- **Type:** [[float (type)]]

### particle
- **Type:** [[ParticleID (type)]]
- **Optional**
Mandatory if `smoke` is not defined.

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**
Mandatory if `particle` is not defined.

### time_to_live_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### time_before_start_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### height_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### vertical_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### horizontal_speed_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
