---
title: on_player_repaired_entity
tags: [factorio-api, runtime, event]
---
# on_player_repaired_entity

Called when a player repairs an entity.

## Filter

- **Type:** [[LuaPlayerRepairedEntityEventFilter]]

## Data

### player_index
- **Type:** [[uint32]]

### entity
- **Type:** [[LuaEntity]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
