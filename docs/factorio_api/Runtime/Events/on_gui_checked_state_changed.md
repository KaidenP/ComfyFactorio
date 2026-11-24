---
title: on_gui_checked_state_changed
tags: [factorio-api, runtime, event]
---
# on_gui_checked_state_changed

Called when [[LuaGuiElement]] checked state is changed (related to checkboxes and radio buttons).

## Data

### element
- **Type:** [[LuaGuiElement]]
The element whose checked state changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
