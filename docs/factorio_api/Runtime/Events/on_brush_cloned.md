---
title: on_brush_cloned
tags: [factorio-api, runtime, event]
---
# on_brush_cloned

Called when a set of positions on the map is cloned.

## Data

### source_offset
- **Type:** [[TilePosition]]

### destination_offset
- **Type:** [[TilePosition]]

### source_surface
- **Type:** [[LuaSurface]]

### source_positions
- **Type:** array<[[TilePosition]]>

### destination_surface
- **Type:** [[LuaSurface]]

### destination_force
- **Type:** [[LuaForce]]
- **Optional**

### clone_tiles
- **Type:** [[boolean]]

### clone_entities
- **Type:** [[boolean]]

### clone_decoratives
- **Type:** [[boolean]]

### clear_destination_entities
- **Type:** [[boolean]]

### clear_destination_decoratives
- **Type:** [[boolean]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
