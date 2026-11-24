---
title: on_entity_damaged
tags: [factorio-api, runtime, event]
---
# on_entity_damaged

Called when an entity is damaged. This is not called when an entities health is set directly by another mod.

## Filter

- **Type:** [[LuaEntityDamagedEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]

### damage_type
- **Type:** [[LuaDamagePrototype]]

### original_damage_amount
- **Type:** [[float]]
The damage amount before resistances.

### final_damage_amount
- **Type:** [[float]]
The damage amount after resistances.

### final_health
- **Type:** [[float]]
The health of the entity after the damage was applied.

### cause
- **Type:** [[LuaEntity]]
- **Optional**
The entity that originally triggered the events that led to this damage, if available (e.g. the character, turret, etc. that pulled the trigger).

### source
- **Type:** [[LuaEntity]]
- **Optional**
The entity that is directly dealing the damage, if available (e.g. the projectile, flame, sticker, grenade, laser beam, etc.).

### force
- **Type:** [[LuaForce]]
- **Optional**
The force that did the attacking if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
