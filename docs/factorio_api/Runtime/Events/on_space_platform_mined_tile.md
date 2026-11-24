---
title: on_space_platform_mined_tile
tags: [factorio-api, runtime, event]
---
# on_space_platform_mined_tile

Called after a platform mines tiles.

## Data

### platform
- **Type:** [[LuaSpacePlatform]]
The platform.

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
