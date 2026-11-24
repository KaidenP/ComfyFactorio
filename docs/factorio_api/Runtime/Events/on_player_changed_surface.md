---
title: on_player_changed_surface
tags: [factorio-api, runtime, event]
---
# on_player_changed_surface

Called after a player changes surfaces.

## Data

### player_index
- **Type:** [[uint32]]
The player who changed surfaces.

### surface_index
- **Type:** [[uint32]]
- **Optional**
The surface index the player was on - may be `nil` if the surface no longer exists.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
