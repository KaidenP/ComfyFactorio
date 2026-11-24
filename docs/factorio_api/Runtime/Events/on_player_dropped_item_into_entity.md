---
title: on_player_dropped_item_into_entity
tags: [factorio-api, runtime, event]
---
# on_player_dropped_item_into_entity

Called when a player drops a single item into an entity.

## Data

### player_index
- **Type:** [[uint32]]

### entity
- **Type:** [[LuaEntity]]
The entity the item was dropped into.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
