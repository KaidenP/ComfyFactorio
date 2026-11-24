---
title: on_player_reverse_selected_area
tags: [factorio-api, runtime, event]
---
# on_player_reverse_selected_area

Called after a player reverse-selects an area with a selection-tool item.

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

### entities
- **Type:** array<[[LuaEntity]]>
The entities selected.

### tiles
- **Type:** array<[[LuaTile]]>
The tiles selected.

### selection_mode
- **Type:** [[defines.selection_mode]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
