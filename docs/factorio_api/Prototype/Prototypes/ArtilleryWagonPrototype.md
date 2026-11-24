---
title: ArtilleryWagonPrototype
tags: [factorio-api, prototype]
---
# ArtilleryWagonPrototype

> **Parent:** [[RollingStockPrototype]] · **Type name:** `artillery-wagon`

An [artillery wagon](https://wiki.factorio.com/Artillery_wagon).

## Properties

### gun
- **Type:** [[ItemID (type)]]
Name of a [[GunPrototype]].

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
Must be > 0.

### ammo_stack_limit
- **Type:** [[ItemCountType (type)]]
Must be > 0.

### automated_ammo_count
- **Type:** [[ItemCountType (type)]]
- **Optional**
Must be > 0. The amount of ammo that inserters automatically insert into this artillery wagon.

### turret_rotation_speed
- **Type:** [[double (type)]]

### manual_range_modifier
- **Type:** [[double (type)]]
Must be > 0.

### disable_automatic_firing
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### cannon_base_pictures
- **Type:** [[RollingStockRotatedSlopedGraphics]]
- **Optional**

### cannon_base_height
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### cannon_base_shift_when_vertical
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### cannon_base_shift_when_horizontal
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### cannon_barrel_pictures
- **Type:** [[RollingStockRotatedSlopedGraphics]]
- **Optional**

### rotating_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### turn_after_shooting_cooldown
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### cannon_parking_frame_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### cannon_parking_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be positive.

### cannon_barrel_recoil_shiftings
- **Type:** array<[[Vector3D (type)]]>
- **Optional**

### cannon_barrel_recoil_shiftings_load_correction_matrix
- **Type:** array<[[Vector3D (type)]]>
- **Optional**
Only loaded if `cannon_barrel_recoil_shiftings` is loaded.

### cannon_barrel_light_direction
- **Type:** [[Vector3D (type)]]
- **Optional**
Only loaded if `cannon_barrel_recoil_shiftings` is loaded.
