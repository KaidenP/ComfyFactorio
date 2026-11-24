---
title: on_sector_scanned
tags: [factorio-api, runtime, event]
---
# on_sector_scanned

Called when an entity of type `radar` finishes scanning a sector.

## Filter

- **Type:** [[LuaSectorScannedEventFilter]]

## Data

### radar
- **Type:** [[LuaEntity]]
The radar that did the scanning.

### chunk_position
- **Type:** [[ChunkPosition]]
The chunk scanned.

### area
- **Type:** [[BoundingBox]]
Area of the scanned chunk.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
