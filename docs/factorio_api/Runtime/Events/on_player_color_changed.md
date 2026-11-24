---
title: on_player_color_changed
tags: [factorio-api, runtime, event]
---
# on_player_color_changed

Called after a player's color changes.

## Data

### player_index
- **Type:** [[uint32]]
The player whose color changed.

### old_color
- **Type:** [[Color]]
The old color.

### old_chat_color
- **Type:** [[Color]]
The old chat color.

### by_script
- **Type:** [[boolean]]
If the change was done by script or the player.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
