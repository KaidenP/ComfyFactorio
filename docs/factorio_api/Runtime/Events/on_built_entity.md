---
title: on_built_entity
tags: [factorio-api, runtime, event]
---
# on_built_entity

Called when player builds something.

## Filter

- **Type:** [[LuaPlayerBuiltEntityEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was built.

### player_index
- **Type:** [[uint32]]
The player who did the building.

### consumed_items
- **Type:** [[LuaInventory]]
A temporary inventory containing all items that the game used to build the entity. This inventory is temporary and thus invalidated after the event.

### tags
- **Type:** [[Tags]]
- **Optional**
The tags associated with this entity if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
