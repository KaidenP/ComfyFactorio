---
title: on_gui_text_changed
tags: [factorio-api, runtime, event]
---
# on_gui_text_changed

Called when [[LuaGuiElement]] text is changed by the player.

## Data

### element
- **Type:** [[LuaGuiElement]]
The edited element.

### player_index
- **Type:** [[uint32]]
The player who did the edit.

### text
- **Type:** [[string]]
The new text in the element.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
