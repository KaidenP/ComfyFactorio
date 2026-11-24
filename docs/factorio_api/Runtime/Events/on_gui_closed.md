---
title: on_gui_closed
tags: [factorio-api, runtime, event]
---
# on_gui_closed

Called when the player closes the GUI they have open.

This can only be raised when the GUI's player controller is still valid. If a GUI is thus closed due to the player disconnecting, dying, or becoming a spectator in other ways, it won't cause this event to be raised.

It's not advised to open any other GUI during this event because if this is run as a request to open a different GUI the game will force close the new opened GUI without notice to ensure the original requested GUI is opened.

## Data

### player_index
- **Type:** [[uint32]]
The player closing the GUI.

### gui_type
- **Type:** [[defines.gui_type]]
The type of GUI that was closed.

### tile_position
- **Type:** [[TilePosition]]
- **Optional**
The position of the tile whose GUI was closed.

### equipment
- **Type:** [[LuaEquipment]]
- **Optional**
The equipment whose GUI was closed.

### entity
- **Type:** [[LuaEntity]]
- **Optional**
The entity or entity grid whose GUI was closed.

### item
- **Type:** [[LuaItemStack]]
- **Optional**
The item whose GUI was closed.

### other_player
- **Type:** [[LuaPlayer]]
- **Optional**
The other player whose GUI was closed.

### element
- **Type:** [[LuaGuiElement]]
- **Optional**
The custom GUI element that was closed.

### surface_index
- **Type:** [[uint32]]
- **Optional**
The surface index of the global electric network whose GUI was closed.

### inventory
- **Type:** [[LuaInventory]]
- **Optional**
The script inventory whose GUI was closed.

### record
- **Type:** [[LuaRecord]]
- **Optional**
Blueprint record that was closed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
