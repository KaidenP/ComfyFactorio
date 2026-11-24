---
title: ArtilleryTurretPrototype
tags: [factorio-api, prototype]
---
# ArtilleryTurretPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `artillery-turret`

An [artillery turret](https://wiki.factorio.com/Artillery_turret).

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
Must be > 0. The amount of ammo that inserters automatically insert into this artillery turret.

### turret_rotation_speed
- **Type:** [[double (type)]]

### manual_range_modifier
- **Type:** [[double (type)]]
Must be positive.

### alert_when_attacking
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### disable_automatic_firing
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### base_picture_secondary_draw_order
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### base_picture_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`

### base_picture
- **Type:** [[Animation4Way]]
- **Optional**

### cannon_base_shift
- **Type:** [[Vector3D (type)]]

### cannon_base_pictures
- **Type:** [[RotatedSprite]]
- **Optional**

### cannon_barrel_pictures
- **Type:** [[RotatedSprite]]
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

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

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

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).
