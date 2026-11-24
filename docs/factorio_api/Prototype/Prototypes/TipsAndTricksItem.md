---
title: TipsAndTricksItem
tags: [factorio-api, prototype]
---
# TipsAndTricksItem

> **Parent:** [[PrototypeBase]] · **Type name:** `tips-and-tricks-item`

A tips and tricks entry.

## Properties

### image
- **Type:** [[FileName]]
- **Optional**
- **Default:** `""`

### simulation
- **Type:** [[SimulationDefinition (type)]]
- **Optional**

### tag
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
String to add in front of the tips and trick entries name. Can be anything, the base game tends to use [rich text](https://wiki.factorio.com/Rich_text) tags for items, e.g. `[item=wooden-chest]` here.

### category
- **Type:** [[string (type)]]
- **Optional**
- **Default:** the `name` of this prototype
Name of a [[TipsAndTricksItemCategory]], used for the sorting of this tips and tricks entry. Tips and trick entries are sorted first by category and then by their `order` within that category.

### indent
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
The tips and tricks entry is indented by `indent`×6 spaces.

### is_title
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the tip title on the left in the tips and tricks GUI should use the "title_tip_item" style (semi bold font).

### trigger
- **Type:** [[TipTrigger]]
- **Optional**
Condition for when the tip notification should be shown to the player. If the condition is fulfilled, the status of the tip is set to "suggested" or "dependencies-not-met".

### skip_trigger
- **Type:** [[TipTrigger]]
- **Optional**
Condition for never showing the tip notification to the player. If the condition is fulfilled, the tip is considered completed and shown in the tips list.

If the tip notification is already shown, then fulfilling the skip trigger removes the tip notification icon again.

### tutorial
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
Name of a [[TutorialDefinition]].

### starting_status
- **Type:** [[TipStatus]]
- **Optional**
- **Default:** `"locked"`

### dependencies
- **Type:** array<[[string (type)]]>
- **Optional**
- **Default:** none
An array of names of other tips and tricks items. This tips and tricks entry is only shown to the player once they have marked all dependencies as read.

### player_input_method_filter
- **Type:** [[PlayerInputMethodFilter]]
- **Optional**
- **Default:** `"all"`

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### order
- **Type:** [[Order]]
- **Optional**
- **Default:** Value of `name`
- **Overrides parent**
Used to order prototypes in inventory, recipes and GUIs. May not exceed a length of 200 characters.
