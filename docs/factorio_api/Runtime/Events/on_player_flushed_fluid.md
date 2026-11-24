---
title: on_player_flushed_fluid
tags: [factorio-api, runtime, event]
---
# on_player_flushed_fluid

Called after player flushed fluid

## Data

### player_index
- **Type:** [[uint32]]
Index of the player

### fluid
- **Type:** [[string]]
Name of a fluid that was flushed

### amount
- **Type:** [[double]]
Amount of fluid that was removed

### entity
- **Type:** [[LuaEntity]]
Entity from which flush was performed

### only_this_entity
- **Type:** [[boolean]]
True if flush was requested only on this entity

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
