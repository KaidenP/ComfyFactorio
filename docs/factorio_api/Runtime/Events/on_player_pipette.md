---
title: on_player_pipette
tags: [factorio-api, runtime, event]
---
# on_player_pipette

Called when a player invokes the "smart pipette" over an entity.

## Data

### player_index
- **Type:** [[uint32]]
The player

### item
- **Type:** [[LuaItemPrototype]]
The item put in the cursor

### quality
- **Type:** [[LuaQualityPrototype]]
The item quality put in the cursor

### used_cheat_mode
- **Type:** [[boolean]]
If cheat mode was used to give a free stack of the item.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
