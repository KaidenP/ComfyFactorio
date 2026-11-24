---
title: SpiderVehiclePrototype
tags: [factorio-api, prototype]
---
# SpiderVehiclePrototype

> **Parent:** [[VehiclePrototype]] · **Type name:** `spider-vehicle`

A [spidertron](https://wiki.factorio.com/Spidertron).

## Properties

### energy_source
- **Type:** [[BurnerEnergySource]] | [[VoidEnergySource]]

### inventory_size
- **Type:** [[ItemStackIndex (type)]]

### graphics_set
- **Type:** [[SpiderVehicleGraphicsSet]]
- **Optional**

### spider_engine
- **Type:** [[SpiderEngineSpecification (type)]]

### height
- **Type:** [[float (type)]]
The height of the spider affects the shooting height and the drawing of the graphics and lights.

### movement_energy_consumption
- **Type:** [[Energy]]

### automatic_weapon_cycling
- **Type:** [[boolean (type)]]

### chain_shooting_cooldown_modifier
- **Type:** [[float (type)]]
This is applied whenever the spider shoots (manual and automatic targeting), `automatic_weapon_cycling` is true and the next gun in line (which is then selected) has ammo. When all of the above is the case, the chain_shooting_cooldown_modifier is a multiplier on the remaining shooting cooldown: `cooldown = (remaining_cooldown × chain_shooting_cooldown_modifier)`.

chain_shooting_cooldown_modifier is intended to be in the range of 0 to 1. This means that setting chain_shooting_cooldown_modifier to 0 reduces the remaining shooting cooldown to 0 while a chain_shooting_cooldown_modifier of 1 does not affect the remaining shooting cooldown at all.

### torso_rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
The orientation of the torso of the spider affects the shooting direction and the drawing of the graphics and lights.

### torso_bob_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Cannot be negative.

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`
If set to 0 then the spider will not have a Logistics tab.

### guns
- **Type:** array<[[ItemID (type)]]>
- **Optional**
The guns this spider vehicle uses.
