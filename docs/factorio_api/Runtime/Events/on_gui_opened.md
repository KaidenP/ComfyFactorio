---
title: on_gui_opened
tags: [factorio-api, runtime, event]
---
# on_gui_opened

Called when the player opens a GUI.

## Data

### player_index
- **Type:** [[uint32]]
The player opening the GUI.

### gui_type
- **Type:** [[defines.gui_type]]
The type of GUI that was opened.

### tile_position
- **Type:** [[TilePosition]]
- **Optional**
The position of the tile whose GUI was opened.

### equipment
- **Type:** [[LuaEquipment]]
- **Optional**
The equipment whose GUI was opened.

### entity
- **Type:** [[LuaEntity]]
- **Optional**
The entity or entity grid whose GUI was opened.

### item
- **Type:** [[LuaItemStack]]
- **Optional**
The item whose GUI was opened.

### other_player
- **Type:** [[LuaPlayer]]
- **Optional**
The other player whose GUI was opened.

### element
- **Type:** [[LuaGuiElement]]
- **Optional**
The custom GUI element that was opened.

### surface_index
- **Type:** [[uint32]]
- **Optional**
The surface index of the global electric network whose GUI was opened.

### inventory
- **Type:** [[LuaInventory]]
- **Optional**
The script inventory whose GUI was opened.

### record
- **Type:** [[LuaRecord]]
- **Optional**
Blueprint record that was opened.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
