---
title: ArmorPrototype
tags: [factorio-api, prototype]
---
# ArmorPrototype

> **Parent:** [[ToolPrototype]] · **Type name:** `armor`

Armor to wear on your in-game [[CharacterPrototype|character]] for defense and buffs.

## Properties

### equipment_grid
- **Type:** [[EquipmentGridID]]
- **Optional**
Name of the [[EquipmentGridPrototype]] that this armor has.

### resistances
- **Type:** array<[[Resistance (type)]]>
- **Optional**
What amount of damage the armor takes on what type of damage is incoming.

### inventory_size_bonus
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
By how many slots the inventory of the player is expanded when the armor is worn.

### provides_flight
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Requires:** `space_age`

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**

### drawing_box
- **Type:** [[BoundingBox (type)]]
- **Optional**

### takeoff_sound
- **Type:** [[Sound]]
- **Optional**
Only loaded if `provides_flight` is `true`.

### flight_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Only loaded if `provides_flight` is `true`.

### landing_sound
- **Type:** [[Sound]]
- **Optional**
Only loaded if `provides_flight` is `true`.

### steps_sound
- **Type:** [[Sound]]
- **Optional**

### moving_sound
- **Type:** [[Sound]]
- **Optional**
