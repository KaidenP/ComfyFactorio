---
title: on_gui_selection_state_changed
tags: [factorio-api, runtime, event]
---
# on_gui_selection_state_changed

Called when [[LuaGuiElement]] selection state is changed (related to drop-downs and listboxes).

## Data

### element
- **Type:** [[LuaGuiElement]]
The element whose selection state changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
