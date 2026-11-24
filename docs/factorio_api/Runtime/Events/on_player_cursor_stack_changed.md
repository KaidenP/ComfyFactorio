---
title: on_player_cursor_stack_changed
tags: [factorio-api, runtime, event]
---
# on_player_cursor_stack_changed

Called after a player's [[LuaControl#cursor_stack|cursor stack]] changed in some way.

This is fired in the same tick that the change happens, but not instantly.

## Data

### player_index
- **Type:** [[uint32]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
