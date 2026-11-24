---
title: on_player_banned
tags: [factorio-api, runtime, event]
---
# on_player_banned

Called when a player is banned.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player banned.

### player_name
- **Type:** [[string]]
The banned player name.

### by_player
- **Type:** [[uint32]]
- **Optional**
The player that did the banning if any.

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
