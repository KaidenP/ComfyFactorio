---
title: on_chunk_charted
tags: [factorio-api, runtime, event]
---
# on_chunk_charted

Called when a chunk is charted or re-charted.

## Data

### surface_index
- **Type:** [[uint32]]

### position
- **Type:** [[ChunkPosition]]

### area
- **Type:** [[BoundingBox]]
Area of the chunk.

### force
- **Type:** [[LuaForce]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
