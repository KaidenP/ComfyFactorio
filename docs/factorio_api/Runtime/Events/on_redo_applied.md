---
title: on_redo_applied
tags: [factorio-api, runtime, event]
---
# on_redo_applied

Called when the player triggers "redo".

## Data

### player_index
- **Type:** [[uint32]]
The player who triggered the redo action.

### actions
- **Type:** array<[[UndoRedoAction]]>
The context of the redo action.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
