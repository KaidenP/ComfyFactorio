---
title: on_player_kicked
tags: [factorio-api, runtime, event]
---
# on_player_kicked

Called when a player is kicked.

## Data

### player_index
- **Type:** [[uint32]]
The player kicked.

### by_player
- **Type:** [[uint32]]
- **Optional**
The player that did the kicking if any.

### reason
- **Type:** [[string]]
- **Optional**
The reason given if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
