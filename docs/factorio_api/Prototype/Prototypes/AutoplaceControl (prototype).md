---
title: AutoplaceControl
tags: [factorio-api, prototype]
---
# AutoplaceControl

*Note: `AutoplaceControl (prototype)`.*

> **Parent:** [[Prototype]] · **Type name:** `autoplace-control` · **Instance limit:** 255

A setting in the map creation GUI. Used by the [[AutoplaceSpecification (type)#control|autoplace system]].

## Properties

### category
- **Type:** `"resource"` | `"terrain"` | `"cliff"` | `"enemy"`
Controls in what tab the autoplace is shown in the map generator GUI.

### richness
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Sets whether this control's richness can be changed. The map generator GUI will only show the richness slider when the `category` is `"resource"`.

If the autoplace control is used to generate ores, you probably want this to be true.

### can_be_disabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether there is an "enable" checkbox for the autoplace control in the map generator GUI. If this is false, the autoplace control cannot be disabled from the GUI.

### related_to_fight_achievements
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this settings being lower than default disables fight related achievements.

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Hides the autoplace control from the map generation screen.
