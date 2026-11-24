---
title: on_gui_confirmed
tags: [factorio-api, runtime, event]
---
# on_gui_confirmed

Called when a [[LuaGuiElement]] is confirmed, for example by pressing Enter in a textfield.

## Data

### element
- **Type:** [[LuaGuiElement]]
The confirmed element.

### player_index
- **Type:** [[uint32]]
The player who did the confirming.

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
