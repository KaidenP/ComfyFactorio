---
title: on_pre_player_mined_item
tags: [factorio-api, runtime, event]
---
# on_pre_player_mined_item

Called when the player completes a mining action, but before the entity is potentially removed from the map. This is called even if the entity does not end up being removed.

## Filter

- **Type:** [[LuaPrePlayerMinedEntityEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity being mined

### player_index
- **Type:** [[uint32]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
