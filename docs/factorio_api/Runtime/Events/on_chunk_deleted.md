---
title: on_chunk_deleted
tags: [factorio-api, runtime, event]
---
# on_chunk_deleted

Called when one or more chunks are deleted using [[LuaSurface#delete_chunk|LuaSurface::delete_chunk]].

## Data

### surface_index
- **Type:** [[uint32]]

### positions
- **Type:** array<[[ChunkPosition]]>
The chunks deleted.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
