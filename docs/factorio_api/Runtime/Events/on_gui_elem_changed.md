---
title: on_gui_elem_changed
tags: [factorio-api, runtime, event]
---
# on_gui_elem_changed

Called when [[LuaGuiElement]] element value is changed (related to choose element buttons).

## Data

### element
- **Type:** [[LuaGuiElement]]
The element whose element value changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
