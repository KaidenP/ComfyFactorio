---
title: on_chunk_generated
tags: [factorio-api, runtime, event]
---
# on_chunk_generated

Called when a chunk is generated.

## Data

### area
- **Type:** [[BoundingBox]]
Area of the chunk.

### position
- **Type:** [[ChunkPosition]]
Position of the chunk.

### surface
- **Type:** [[LuaSurface]]
The surface the chunk is on.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
