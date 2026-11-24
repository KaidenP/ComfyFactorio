---
title: ArtilleryTriggerDelivery
tags: [factorio-api, prototype, type]
---
# ArtilleryTriggerDelivery

> **Parent:** [[TriggerDeliveryItem]]

## Properties

### type
- **Type:** `"artillery"`

### projectile
- **Type:** [[EntityID (type)]]
Name of a [[ArtilleryProjectilePrototype]].

### starting_speed
- **Type:** [[float (type)]]

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

### trigger_fired_artillery
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
