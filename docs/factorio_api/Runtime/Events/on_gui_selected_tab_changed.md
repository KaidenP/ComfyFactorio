---
title: on_gui_selected_tab_changed
tags: [factorio-api, runtime, event]
---
# on_gui_selected_tab_changed

Called when [[LuaGuiElement]] selected tab is changed (related to tabbed-panes).

## Data

### element
- **Type:** [[LuaGuiElement]]
The tabbed pane whose selected tab changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
