---
title: TileGhostPrototype
tags: [factorio-api, prototype]
---
# TileGhostPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `tile-ghost`

The entity used for tile ghosts.

## Example

```
{
  type = "tile-ghost",
  name = "tile-ghost",
  flags = {"not-on-map"},
  minable = { mining_time = 0, results={}},
  collision_box = {{-0.5, -0.5}, {0.5, 0.5}},
  selection_priority = 45
}
```
