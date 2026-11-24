---
title: ShortcutPrototype
tags: [factorio-api, prototype]
---
# ShortcutPrototype

> **Parent:** [[Prototype]] · **Type name:** `shortcut`

Definition for a shortcut button in the [shortcut bar](https://wiki.factorio.com/Shortcut_bar).

This is **not** a custom keybinding (keyboard shortcut), for that see [[CustomInputPrototype]].

## Properties

### action
- **Type:** `"toggle-alt-mode"` | `"undo"` | `"redo"` | `"paste"` | `"import-string"` | `"toggle-personal-roboport"` | `"toggle-personal-logistic-requests"` | `"toggle-equipment-movement-bonus"` | `"toggle-tall-entity-visibility"` | `"spawn-item"` | `"lua"`
If this is `"lua"`, [[on_lua_shortcut]] is raised when the shortcut is clicked.

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

The base game uses 32px icons for shortcuts.

Only loaded if `icons` is not defined.

### small_icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### small_icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file. Used in the shortcut selection popup.

Only loaded, and mandatory if `small_icons` is not defined.

### small_icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the small icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

The base game uses 24px small icons for shortcuts.

Only loaded if `small_icons` is not defined.

### item_to_spawn
- **Type:** [[ItemID (type)]]
- **Optional**
The item to create when clicking on a shortcut with the action set to `"spawn-item"`. The item must have the [[ItemPrototypeFlags (type)#spawnable|spawnable]] flag set.

### technology_to_unlock
- **Type:** [[TechnologyID (type)]]
- **Optional**
The technology that must be researched before this shortcut can be used. Once a shortcut is unlocked in one save file, it is unlocked for all future save files.

### unavailable_until_unlocked
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the shortcut will not be available until its `technology_to_unlock` is researched, even if it was already researched in a different game.

### toggleable
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Must be enabled for the Factorio API to be able to set the toggled state on the shortcut button, see [[LuaPlayer#set_shortcut_toggled|LuaPlayer::set_shortcut_toggled]].

### associated_control_input
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
Name of a custom input or vanilla control. This is **only** used to show the keybind in the tooltip of the shortcut.

### style
- **Type:** `"default"` | `"blue"` | `"red"` | `"green"`
- **Optional**
- **Default:** `"default"`

### order
- **Type:** [[Order]]
- **Optional**
- **Default:** `""`
- **Overrides parent**
Used to order the shortcuts in the [quick panel](https://wiki.factorio.com/Quick_panel), which replaces the shortcut bar when using a controller (game pad). It [is recommended](https://forums.factorio.com/106661) to order modded shortcuts after the vanilla shortcuts.

## Example

```
{
  type = "shortcut",
  name = "give-deconstruction-planner",
  order = "b[blueprints]-i[deconstruction-planner]",
  action = "spawn-item",
  localised_name = {"shortcut.make-deconstruction-planner"},
  associated_control_input = "give-deconstruction-planner",
  technology_to_unlock = "construction-robotics",
  item_to_spawn = "deconstruction-planner",
  style = "red",
  icon = "__base__/graphics/icons/shortcut-toolbar/mip/new-deconstruction-planner-x56.png",
  icon_size = 56,
  small_icon = "__base__/graphics/icons/shortcut-toolbar/mip/new-deconstruction-planner-x24.png",
  small_icon_size = 24
}
```
