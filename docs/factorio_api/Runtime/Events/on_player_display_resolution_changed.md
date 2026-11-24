---
title: on_player_display_resolution_changed
tags: [factorio-api, runtime, event]
---
# on_player_display_resolution_changed

Called when the display resolution changes for a given player.

## Data

### player_index
- **Type:** [[uint32]]
The player

### old_resolution
- **Type:** [[DisplayResolution]]
The old display resolution

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
