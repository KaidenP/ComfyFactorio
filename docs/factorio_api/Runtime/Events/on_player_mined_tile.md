---
title: on_player_mined_tile
tags: [factorio-api, runtime, event]
---
# on_player_mined_tile

Called after a player mines tiles.

## Data

### player_index
- **Type:** [[uint32]]

### surface_index
- **Type:** [[uint32]]
The surface the tile(s) were mined from.

### tiles
- **Type:** array<[[OldTileAndPosition]]>
The position data.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
