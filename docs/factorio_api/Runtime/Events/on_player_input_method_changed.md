---
title: on_player_input_method_changed
tags: [factorio-api, runtime, event]
---
# on_player_input_method_changed

Called when a player's input method changes. See [[LuaPlayer#input_method|LuaPlayer::input_method]].

## Data

### player_index
- **Type:** [[uint32]]
The player whose input method changed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
