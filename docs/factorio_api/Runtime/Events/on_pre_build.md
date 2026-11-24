---
title: on_pre_build
tags: [factorio-api, runtime, event]
---
# on_pre_build

Called when players uses an item to build something. Called before [[on_built_entity]].

## Data

### player_index
- **Type:** [[uint32]]
The player who did the placing.

### position
- **Type:** [[MapPosition]]
Where the item was placed.

### build_mode
- **Type:** [[defines.build_mode]]
Build mode the item was placed with.

### direction
- **Type:** [[defines.direction]]
The direction the item was facing when placed.

### mirror
- **Type:** [[boolean]]
If the item is mirrored (only crafting machines support this)

### flip_horizontal
- **Type:** [[boolean]]
Whether the blueprint was flipped horizontally. `nil` if not built by a blueprint.

### flip_vertical
- **Type:** [[boolean]]
Whether the blueprint was flipped vertically. `nil` if not built by a blueprint.

### created_by_moving
- **Type:** [[boolean]]
Whether the item was placed while moving.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
