---
title: StreamAttackParameters
tags: [factorio-api, prototype, type]
---
# StreamAttackParameters

> **Parent:** [[BaseAttackParameters]]

## Properties

### type
- **Type:** `"stream"`

### fluid_consumption
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** `0.0`

### gun_barrel_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### projectile_creation_parameters
- **Type:** [[CircularProjectileCreationSpecification (type)]]
- **Optional**

### gun_center_shift
- **Type:** [[Vector (type)]] | [[GunShift4Way (type)]]
- **Optional**

### fluids
- **Type:** array<[[StreamFluidProperties]]>
- **Optional**
Controls which fluids can fuel this stream attack and their potential damage bonuses.
