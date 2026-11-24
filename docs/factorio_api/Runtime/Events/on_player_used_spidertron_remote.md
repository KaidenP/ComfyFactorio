---
title: on_player_used_spidertron_remote
tags: [factorio-api, runtime, event]
---
# on_player_used_spidertron_remote

Called when a player uses spidertron remote to send all selected units to a given position

## Data

### player_index
- **Type:** [[uint32]]
The player that used the remote.

### position
- **Type:** [[MapPosition]]
Goal position to which spidertron was sent to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
