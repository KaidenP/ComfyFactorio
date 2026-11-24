---
title: on_player_used_capsule
tags: [factorio-api, runtime, event]
---
# on_player_used_capsule

Called when a player uses a capsule that results in some game action.

## Data

### player_index
- **Type:** [[uint32]]
The player.

### item
- **Type:** [[LuaItemPrototype]]
The capsule item used.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of the capsule item used.

### position
- **Type:** [[MapPosition]]
The position the capsule was used.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
