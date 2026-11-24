---
title: on_gui_click
tags: [factorio-api, runtime, event]
---
# on_gui_click

Called when [[LuaGuiElement]] is clicked.

## Data

### element
- **Type:** [[LuaGuiElement]]
The clicked element.

### player_index
- **Type:** [[uint32]]
The player who did the clicking.

### button
- **Type:** [[defines.mouse_button_type]]
The mouse button used if any.

### cursor_display_location
- **Type:** [[GuiLocation]]
The display location of the player's cursor.

### alt
- **Type:** [[boolean]]
If alt was pressed.

### control
- **Type:** [[boolean]]
If control was pressed.

### shift
- **Type:** [[boolean]]
If shift was pressed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
