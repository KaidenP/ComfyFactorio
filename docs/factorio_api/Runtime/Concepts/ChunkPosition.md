---
title: ChunkPosition
tags: [factorio-api, runtime, concept]
---
# ChunkPosition

Coordinates of a chunk in a [[LuaSurface]] where each integer `x`/`y` represents a different chunk. This uses the same format as [[MapPosition]], meaning it can be specified either with or without explicit keys. A [[MapPosition]] can be translated to a ChunkPosition by dividing the `x`/`y` values by 32.

## Type

table | ([[int32]], [[int32]])
