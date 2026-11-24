---
title: on_area_cloned
tags: [factorio-api, runtime, event]
---
# on_area_cloned

Called when an area of the map is cloned.

## Data

### source_surface
- **Type:** [[LuaSurface]]

### source_area
- **Type:** [[BoundingBox]]

### destination_surface
- **Type:** [[LuaSurface]]

### destination_area
- **Type:** [[BoundingBox]]

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
