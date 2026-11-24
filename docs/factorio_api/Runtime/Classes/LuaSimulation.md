---
title: LuaSimulation
tags: [factorio-api, runtime, class]
---
# LuaSimulation

Functions for use during simulations. This object cannot be saved, and cannot be used outside of a simulation.

The simulation object instance can be obtained from [[LuaGameScript#simulation|LuaGameScript::simulation]].

## Attributes

### camera_player_cursor_position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
- **Optional**

### camera_position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
- **Optional**

### camera_surface_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**

### hide_cursor
- **Writable:** [[boolean]]

### camera_zoom
- **Writable:** [[double]]

### camera_player
- **Writable:** [[PlayerIdentification]]

### camera_player_cursor_direction
- **Writable:** [[defines.direction]]

### camera_alt_info
- **Writable:** [[boolean]]

### camera_show_alerts
- **Writable:** [[boolean]]

### smart_belt_building
- **Writable:** [[boolean]]
- **Optional**

### gui_tooltip_interval
- **Writable:** [[double]]

### active_quickbars
- **Writable:** [[uint8]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### create_test_player

Takes a table with the following fields:
- **`name`** — [[string]]: The name of the new player.

**Returns:**
- [[LuaPlayer]]: The created player.

### get_slot_position

Takes a table with the following fields:
- **`inventory_index`** — [[defines.inventory]]
- **`slot_index`** — [[ItemStackIndex]]: This index is 0-based, unlike other inventory indices.
- **`inventory`** — `"character"` | `"entity"` *(optional)*: Defaults to `"character"`.

**Returns:**
- [[MapPosition]] *(optional)*: Position of the GUI slot on the screen, if successfully found.

### get_widget_position

Takes a table with the following fields:
- **`type`** — [[SimulationWidgetType]]

Other attributes may be specified depending on `type`:

**Variant `check-box`:**
  - **`text`** — [[LocalisedString]]

**Variant `drop-down`:**
  - **`text`** — [[string]] *(optional)*

**Variant `item-group-tab`:**
  - **`group`** — [[ItemGroupID]]

**Variant `label`:**
  - **`text`** — [[string]] *(optional)*

**Variant `logistics-button`:**
  - **`request_index`** — [[LogisticFilterIndex]]

**Variant `logistics-button-space`:**
  - **`request_index`** — [[LogisticFilterIndex]]
  - **`section_index`** — [[LogisticSectionIndex]]

**Variant `quickbar-slot`:**
  - **`filter`** — [[ItemFilter]] *(optional)*: Note: since quickbar slots are also of type ItemFilter, filter is used as a value: it must be equal [[QuickBarSlot#filter|QuickBarSlot::filter]].
  - **`page_index`** — [[uint8]] *(optional)*
  - **`slot_index`** — [[uint8]] *(optional)*

**Variant `recipe-slot`:**
  - **`recipe`** — [[RecipeID]]

**Variant `signal-id-base`:**
  - **`id`** — [[SignalIDBase]]

**Variant `simple-item-slot`:**
  - **`item`** — [[ItemID]]

**Variant `simple-item-with-quality-slot`:**
  - **`filter`** — [[ItemFilter]]

**Variant `simple-slot`:**
  - **`item`** — [[ItemID]]

**Variant `text-button`:**
  - **`text`** — [[string]]

**Variant `text-button-localised-substring`:**
  - **`text`** — [[LocalisedString]]

**Variant `text-button-substring`:**
  - **`text`** — [[string]]

**Variant `textfield`:**
  - **`text`** — [[string]]

**Returns:**
- [[MapPosition]] *(optional)*: Center of the GUI widget on the screen, if successfully found.

### activate_rail_planner
Activate the rail planner at the given position.

Takes a table with the following fields:
- **`position`** — [[MapPosition]] *(optional)*
- **`ghost_mode`** — [[boolean]] *(optional)*: Defaults to `false`.
- **`build_mode`** — [[defines.build_mode]] *(optional)*: Defaults to [[defines.build_mode#normal|normal]].

### deactivate_rail_planner
Deactivate the rail planner.

### move_cursor
Move the cursor towards the given position at the given speed.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]
- **`speed`** — [[double]] *(optional)*: Defaults to `0.2`.

**Returns:**
- [[boolean]]: Whether the cursor will reach the target position with this move.

### mouse_down
Send a left mouse button-down event at its current position.

### mouse_up
Send a left mouse button-up event at its current position.

### mouse_click
Send a left mouse button click event at its current position. This is equivalent to calling [[LuaSimulation#mouse_down|LuaSimulation::mouse_down]], then [[LuaSimulation#mouse_up|LuaSimulation::mouse_up]].

### control_down
Send a control press event at the current cursor position.

Takes a table with the following fields:
- **`control`** — [[string]]: The name of the control input to press.
- **`notify`** — [[boolean]]: Whether to show flying text of the activated control.

### control_up
Send a control release event at the current cursor position.

Takes a table with the following fields:
- **`control`** — [[string]]: The name of the control input to release.

### control_press
Send a control down and up event at the current cursor position. This is equivalent to calling [[LuaSimulation#control_down|LuaSimulation::control_down]], then [[LuaSimulation#control_up|LuaSimulation::control_up]].

Takes a table with the following fields:
- **`control`** — [[string]]: The name of the control input to press and release.
- **`notify`** — [[boolean]]: Whether to show flying text of the activated control.

### write
Write text as if it was typed by a player. Overwrites existing text by selecting it first.

Takes a table with the following fields:
- **`text`** — [[string]] *(optional)*: The text to write. Does nothing if no text is provided.

### scroll_clipboard_forwards
Scroll the clipboard forwards by one entry.

### scroll_clipboard_backwards
Scroll the clipboard backwards by one entry.
