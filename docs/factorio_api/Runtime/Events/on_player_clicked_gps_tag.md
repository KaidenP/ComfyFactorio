---
title: on_player_clicked_gps_tag
tags: [factorio-api, runtime, event]
---
# on_player_clicked_gps_tag

Called when a player clicks a gps tag

## Data

### player_index
- **Type:** [[uint32]]
Index of the player

### position
- **Type:** [[MapPosition]]
Map position contained in gps tag

### surface
- **Type:** [[string]]
Surface name contained in gps tag, even when such surface does not exists

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
