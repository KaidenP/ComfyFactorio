---
title: on_player_display_density_scale_changed
tags: [factorio-api, runtime, event]
---
# on_player_display_density_scale_changed

Called when the display density scale changes for a given player. The display density scale is the scale value automatically applied based on the player's display DPI. This is only relevant on platforms that support high-density displays.

## Data

### player_index
- **Type:** [[uint32]]
The player

### old_scale
- **Type:** [[double]]
The old display scale

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
