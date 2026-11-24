---
title: on_gui_hover
tags: [factorio-api, runtime, event]
---
# on_gui_hover

Called when [[LuaGuiElement]] is hovered by the mouse.

Only fired for events whose [[LuaGuiElement#raise_hover_events|LuaGuiElement::raise_hover_events]] is `true`.

## Data

### element
- **Type:** [[LuaGuiElement]]
The element that is being hovered over.

### player_index
- **Type:** [[uint32]]
The player whose cursor is hovering.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
