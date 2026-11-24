---
title: on_rocket_launch_ordered
tags: [factorio-api, runtime, event]
---
# on_rocket_launch_ordered

Called when a rocket silo is ordered to be launched.

## Data

### rocket
- **Type:** [[LuaEntity]]

### rocket_silo
- **Type:** [[LuaEntity]]

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that is riding the rocket, if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
