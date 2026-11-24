---
title: on_gui_leave
tags: [factorio-api, runtime, event]
---
# on_gui_leave

Called when the player's cursor leaves a [[LuaGuiElement]] that was previously hovered.

Only fired for events whose [[LuaGuiElement#raise_hover_events|LuaGuiElement::raise_hover_events]] is `true`.

## Data

### element
- **Type:** [[LuaGuiElement]]
The element that was being hovered.

### player_index
- **Type:** [[uint32]]
The player whose cursor was hovering.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
