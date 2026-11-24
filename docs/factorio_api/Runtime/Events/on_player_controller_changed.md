---
title: on_player_controller_changed
tags: [factorio-api, runtime, event]
---
# on_player_controller_changed

Called after a player changes controller types.

## Data

### player_index
- **Type:** [[uint32]]
The player who changed controllers.

### old_type
- **Type:** [[defines.controllers]]
The old controller type.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
