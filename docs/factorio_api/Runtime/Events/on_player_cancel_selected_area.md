---
title: on_player_cancel_selected_area
tags: [factorio-api, runtime, event]
---
# on_player_cancel_selected_area

Called after a player cancels their attempt to select an area with a selection-tool item that has [[SelectionToolPrototype#send_pre_selection_events|SelectionToolPrototype::send_pre_selection_events]] set to `true`.

Because a player's selection state exists solely on their local client and not in game state, this event and the other area preselection events are provided with "best effort", but are not guaranteed. In some situations, such as after loading an existing save or in a multiplayer game, preselection events may not be received in an order that makes sense for the current game state or may be dropped altogether.

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

### quality
- **Type:** [[string]]
The item quality used to select the area.

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
