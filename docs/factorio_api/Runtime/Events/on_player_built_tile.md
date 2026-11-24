---
title: on_player_built_tile
tags: [factorio-api, runtime, event]
---
# on_player_built_tile

Called after a player builds tiles.

## Data

### player_index
- **Type:** [[uint32]]

### surface_index
- **Type:** [[uint32]]
The surface the tile(s) were built on.

### tiles
- **Type:** array<[[OldTileAndPosition]]>
The position data.

### tile
- **Type:** [[LuaTilePrototype]]
The tile prototype that was placed.

### item
- **Type:** [[LuaItemPrototype]]
- **Optional**
The item type used to build the tiles

### quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**
The quality of the item used to build the tiles

### inventory
- **Type:** [[LuaInventory]]
- **Optional**
The inventory containing the items used to build the tiles.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
