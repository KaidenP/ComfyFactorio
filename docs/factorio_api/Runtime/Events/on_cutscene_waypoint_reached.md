---
title: on_cutscene_waypoint_reached
tags: [factorio-api, runtime, event]
---
# on_cutscene_waypoint_reached

Called when a cutscene is playing, each time it reaches a waypoint in that cutscene.

This refers to an index in the table previously passed to set_controller which started the cutscene.

## Data

### player_index
- **Type:** [[uint32]]
The player index of the player viewing the cutscene.

### waypoint_index
- **Type:** [[uint32]]
The index of the waypoint we just completed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
