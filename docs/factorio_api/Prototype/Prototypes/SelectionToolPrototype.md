---
title: SelectionToolPrototype
tags: [factorio-api, prototype]
---
# SelectionToolPrototype

> **Parent:** [[ItemWithLabelPrototype]] · **Type name:** `selection-tool`

Used in the base game as a base for the blueprint item and the deconstruction item.

## Properties

### select
- **Type:** [[SelectionModeData]]

### alt_select
- **Type:** [[SelectionModeData]]

### super_forced_select
- **Type:** [[SelectionModeData]]
- **Optional**

### reverse_select
- **Type:** [[SelectionModeData]]
- **Optional**

### alt_reverse_select
- **Type:** [[SelectionModeData]]
- **Optional**
Settings for how the selection tool alt-reverse-selects things in-game (using SHIFT + Right mouse button).

### always_include_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If tiles should be included in the selection regardless of entities also being in the selection. This is a visual only setting.

### mouse_cursor
- **Type:** [[MouseCursorID]]
- **Optional**
- **Default:** `"selection-tool-cursor"`

### skip_fog_of_war
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### send_pre_selection_events
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, the selection tool will send pre-selection events to mods [[defines.events#on_player_start_selected_area|defines.events.on_player_start_selected_area]], [[defines.events#on_player_change_selected_area|defines.events.on_player_change_selected_area]], and [[defines.events#on_player_cancel_selected_area|defines.events.on_player_cancel_selected_area]]. Off by default because it will incur a performance penalty in multiplayer. It should only be enabled if a mod specifically needs it.
