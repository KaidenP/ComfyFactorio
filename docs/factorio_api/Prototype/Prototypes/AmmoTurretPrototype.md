---
title: AmmoTurretPrototype
tags: [factorio-api, prototype]
---
# AmmoTurretPrototype

> **Parent:** [[TurretPrototype]] · **Type name:** `ammo-turret`

A turret that consumes [[AmmoItemPrototype|ammo items]].

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]
- **Optional**

### energy_per_shot
- **Type:** [[Energy]]
- **Optional**

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
Size of the ammo inventory.

### automated_ammo_count
- **Type:** [[ItemCountType (type)]]
The amount of ammo that inserters automatically insert into this turret.

### prepare_with_no_ammo
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
