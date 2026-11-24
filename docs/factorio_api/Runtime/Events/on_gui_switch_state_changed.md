---
title: on_gui_switch_state_changed
tags: [factorio-api, runtime, event]
---
# on_gui_switch_state_changed

Called when [[LuaGuiElement]] switch state is changed (related to switches).

## Data

### element
- **Type:** [[LuaGuiElement]]
The switch whose switch state changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
