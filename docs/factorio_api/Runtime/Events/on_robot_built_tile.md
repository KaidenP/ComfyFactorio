---
title: on_robot_built_tile
tags: [factorio-api, runtime, event]
---
# on_robot_built_tile

Called after a robot builds tiles.

## Data

### robot
- **Type:** [[LuaEntity]]
The robot.

### tiles
- **Type:** array<[[OldTileAndPosition]]>
The position data.

### tile
- **Type:** [[LuaTilePrototype]]
The tile prototype that was placed.

### item
- **Type:** [[LuaItemPrototype]]
The item type used to build the tiles.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality the item used to build the tiles.

### inventory
- **Type:** [[LuaInventory]]
The inventory containing the stacks used to build the tiles.

### surface_index
- **Type:** [[uint32]]
The surface the tile(s) are build on.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
