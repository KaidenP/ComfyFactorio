---
title: on_gui_value_changed
tags: [factorio-api, runtime, event]
---
# on_gui_value_changed

Called when [[LuaGuiElement]] slider value is changed (related to the slider element).

## Data

### element
- **Type:** [[LuaGuiElement]]
The element whose value changed.

### player_index
- **Type:** [[uint32]]
The player who did the change.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
