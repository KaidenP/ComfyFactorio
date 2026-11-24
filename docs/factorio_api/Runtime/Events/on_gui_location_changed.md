---
title: on_gui_location_changed
tags: [factorio-api, runtime, event]
---
# on_gui_location_changed

Called when [[LuaGuiElement]] element location is changed (related to frames in `player.gui.screen`).

## Data

### element
- **Type:** [[LuaGuiElement]]
The element whose location changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
