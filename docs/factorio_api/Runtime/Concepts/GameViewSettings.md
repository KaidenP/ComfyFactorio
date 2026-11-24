---
title: GameViewSettings
tags: [factorio-api, runtime, concept]
---
# GameViewSettings

Parameters that affect the look and control of the game. Updating any of the member attributes here will immediately take effect in the game engine.

## Fields

### show_controller_gui
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Show the controller GUI elements. This includes the toolbar, the selected tool slot, the armour slot, and the gun and ammunition slots.

### show_minimap
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Show the chart in the upper right-hand corner of the screen.

### show_research_info
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Show research progress and name in the upper right-hand corner of the screen.

### show_entity_info
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Show overlay icons on entities. Also known as "alt-mode".

### show_alert_gui
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Show the flashing alert icons next to the player's toolbar.

### update_entity_selection
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When `true` (the default), mousing over an entity will select it. Otherwise, moving the mouse won't update entity selection.

### show_rail_block_visualisation
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When `true` (`false` is default), the rails will always show the rail block visualisation.

### show_side_menu
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the buttons row.

### show_pins_gui
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the pins GUI on the right side of the screen.

### show_map_view_options
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the view options when map is opened.

### show_entity_tooltip
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the tooltip that is displayed when selecting an entity.

### show_quickbar
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides quickbar of shortcuts.

### show_shortcut_bar
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the shortcut bar.

### show_crafting_queue
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the crafting queue.

### show_tool_bar
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the tool window with the weapons and armor.

### show_hotkey_suggestions
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the mouse and keyboard/controller button hints in the bottom left corner if they are enabled in the interface settings.

### show_surface_list
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Shows or hides the surface list while in Remote View.

### hide_tall_entities
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Makes tall entities translucent and unselectable.
