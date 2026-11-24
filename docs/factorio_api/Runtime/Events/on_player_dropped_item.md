---
title: on_player_dropped_item
tags: [factorio-api, runtime, event]
---
# on_player_dropped_item

Called when a player drops an item on the ground.

## Data

### player_index
- **Type:** [[uint32]]

### entity
- **Type:** [[LuaEntity]]
The item-on-ground entity.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
