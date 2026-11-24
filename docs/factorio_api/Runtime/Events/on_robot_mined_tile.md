---
title: on_robot_mined_tile
tags: [factorio-api, runtime, event]
---
# on_robot_mined_tile

Called after a robot mines tiles.

## Data

### robot
- **Type:** [[LuaEntity]]
The robot.

### tiles
- **Type:** array<[[OldTileAndPosition]]>
The position data.

### surface_index
- **Type:** [[uint32]]
The surface the tile(s) were mined on.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
