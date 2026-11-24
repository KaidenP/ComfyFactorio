---
title: on_gui_inventory_action
tags: [factorio-api, runtime, event]
---
# on_gui_inventory_action

Called when a player interacts with a custom inventory GUI.

## Data

### player_index
- **Type:** [[uint32]]
The player doing the action.

### element
- **Type:** [[LuaGuiElement]]
The inventory element interacted with.

### slot
- **Type:** [[uint32]]
The slot index that was interacted with.

### action
- **Type:** [[defines.inventory_actions]]
The action performed.

### button
- **Type:** [[defines.mouse_button_type]]
The final mouse button used if any.

### alt
- **Type:** [[boolean]]
If alt was pressed.

### control
- **Type:** [[boolean]]
If control was pressed.

### shift
- **Type:** [[boolean]]
If shift was pressed.

### item
- **Type:** [[LuaItemPrototype]]
- **Optional**
The item clicked on.

### quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**
The item quality clicked on.

### item_number
- **Type:** [[uint32]]
- **Optional**
The item number clicked on (if it had one).

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
