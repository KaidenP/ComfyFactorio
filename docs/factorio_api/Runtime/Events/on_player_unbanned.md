---
title: on_player_unbanned
tags: [factorio-api, runtime, event]
---
# on_player_unbanned

Called when a player is un-banned.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player un-banned.

### player_name
- **Type:** [[string]]
The player name un-banned.

### by_player
- **Type:** [[uint32]]
- **Optional**
The player that did the un-banning if any.

### reason
- **Type:** [[string]]
- **Optional**
The reason the player was banned if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
