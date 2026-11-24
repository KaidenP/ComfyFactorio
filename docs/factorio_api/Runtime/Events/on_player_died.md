---
title: on_player_died
tags: [factorio-api, runtime, event]
---
# on_player_died

Called after a player dies.

## Data

### player_index
- **Type:** [[uint32]]

### cause
- **Type:** [[LuaEntity]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
