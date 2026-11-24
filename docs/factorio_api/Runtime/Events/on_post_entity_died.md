---
title: on_post_entity_died
tags: [factorio-api, runtime, event]
---
# on_post_entity_died

Called after an entity dies.

## Filter

- **Type:** [[LuaPostEntityDiedEventFilter]]

## Data

### ghost
- **Type:** [[LuaEntity]]
- **Optional**
The ghost created by the entity dying if any.

### force
- **Type:** [[LuaForce]]
- **Optional**
The force that did the killing if any.

### position
- **Type:** [[MapPosition]]
Position where the entity died.

### prototype
- **Type:** [[LuaEntityPrototype]]
The entity prototype of the entity that died.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of the entity that died.

### damage_type
- **Type:** [[LuaDamagePrototype]]
- **Optional**
The damage type if any.

### corpses
- **Type:** array<[[LuaEntity]]>
The corpses created by the entity dying if any.

### surface_index
- **Type:** [[uint32]]
The surface the entity was on.

### unit_number
- **Type:** [[uint32]]
- **Optional**
The unit number the entity had if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
