---
title: on_undo_applied
tags: [factorio-api, runtime, event]
---
# on_undo_applied

Called when the player triggers "undo".

## Data

### player_index
- **Type:** [[uint32]]
The player who triggered the undo action.

### actions
- **Type:** array<[[UndoRedoAction]]>
The context of the undo action.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
