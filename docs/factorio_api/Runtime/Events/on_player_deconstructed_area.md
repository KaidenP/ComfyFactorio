---
title: on_player_deconstructed_area
tags: [factorio-api, runtime, event]
---
# on_player_deconstructed_area

Called when a player selects an area with a deconstruction planner.

## Data

### player_index
- **Type:** [[uint32]]
The player doing the selection.

### surface
- **Type:** [[LuaSurface]]
The surface selected.

### area
- **Type:** [[BoundingBox]]
The area selected.

### position
- **Type:** [[MapPosition]]
The position where the player started the selection.

### cursor_position
- **Type:** [[MapPosition]]
The player cursor position.

### item
- **Type:** [[string]]
The item used to select the area.

### stack
- **Type:** [[LuaItemStack]]
- **Optional**
The item stack used to select the area.

### record
- **Type:** [[LuaRecord]]
- **Optional**
The record that was used to select the area.

### quality
- **Type:** [[string]]
The item quality used to select the area.

### alt
- **Type:** [[boolean]]
If normal selection or alt selection was used.

### selection_mode
- **Type:** [[defines.selection_mode]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
