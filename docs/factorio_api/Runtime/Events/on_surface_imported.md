---
title: on_surface_imported
tags: [factorio-api, runtime, event]
---
# on_surface_imported

Called after a surface is imported via the map editor.

## Data

### surface_index
- **Type:** [[uint32]]

### original_name
- **Type:** [[string]]
The original surface name.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
