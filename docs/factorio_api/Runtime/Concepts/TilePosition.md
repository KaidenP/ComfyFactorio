---
title: TilePosition
tags: [factorio-api, runtime, concept]
---
# TilePosition

Coordinates of a tile on a [[LuaSurface]] where each integer `x`/`y` represents a different tile. This uses the same format as [[MapPosition]], except it rounds any non-integer `x`/`y` down to whole numbers. It can be specified either with or without explicit keys.

## Type

table | ([[int32]], [[int32]])
