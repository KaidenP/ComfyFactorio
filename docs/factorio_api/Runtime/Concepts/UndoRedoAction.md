---
title: UndoRedoAction
tags: [factorio-api, runtime, concept]
---
# UndoRedoAction

## Fields

### type
- **Type:** `"built-entity"` | `"built-tile"` | `"copy-entity-settings"` | `"removed-entity"` | `"removed-tile"` | `"upgraded-entity"` | `"upgraded-modules"` | `"wire-added"` | `"wire-removed"` | `"rotated-entity"`
The type of action that was undone or redone.

### tags
- **Type:** [[Tags]]
- **Optional**
The tags attached to the undo action, if any.
