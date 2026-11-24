---
title: CustomInputPrototype
tags: [factorio-api, prototype]
---
# CustomInputPrototype

> **Parent:** [[Prototype]] · **Type name:** `custom-input`

Used for custom keyboard shortcuts/key bindings in mods. The key associated with the custom input can be changed in the options. This means that `key_sequence` is simply the default key binding.

Custom inputs share the same namespace as custom events and built-in events for subscribing to and raising them.

## Properties

### name
- **Type:** [[string (type)]]
- **Overrides parent**
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

For a list of all names used in vanilla, see [data.raw](https://wiki.factorio.com/Data.raw).

It is also the name for the event that is raised when they key (combination) is pressed and action is `"lua"`, see [Tutorial:Script interfaces](https://wiki.factorio.com/Tutorial:Script_interfaces#Custom_input).

### key_sequence
- **Type:** [[string (type)]]
The default key sequence for this custom input. Use `""` (empty string) for unassigned.

As modifier keys, these names are used: `"CONTROL"`, `"SHIFT"`, `"COMMAND"`, `"ALT"`. Note that `"COMMAND"` is loaded as `"CONTROL"` on Windows and Linux.

`" + "` is used to separate modifier keys from normal keys, like so: `"ALT + G"`. A key binding can contain any amount of individual modifier keys, but only a single normal mouse button or keyboard key (listed below).
Available names for the normal mouse button

- `mouse-button-1` (left)
- `mouse-button-2` (right)
- `mouse-button-3` (middle)
- `mouse-button-4`
- `mouse-button-5`
- `mouse-button-6`
- `mouse-button-7`
- `mouse-button-8`
- `mouse-button-9`
- `mouse-wheel-up`
- `mouse-wheel-down`
- `mouse-wheel-left`
- `mouse-wheel-right`
Available names for the normal keyboard keys

- A
- B
- C
- D
- E
- F
- G
- H
- I
- J
- K
- L
- M
- N
- O
- P
- Q
- R
- S
- T
- U
- V
- W
- X
- Y
- Z
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 0
- RETURN
- ESCAPE
- BACKSPACE
- TAB
- SPACE
- MINUS
- EQUALS
- LEFTBRACKET
- RIGHTBRACKET
- BACKSLASH
- NONUSHASH
- SEMICOLON
- APOSTROPHE
- GRAVE
- COMMA
- PERIOD
- SLASH
- CAPSLOCK
- F1
- F2
- F3
- F4
- F5
- F6
- F7
- F8
- F9
- F10
- F11
- F12
- PRINTSCREEN
- SCROLLLOCK
- PAUSE
- INSERT
- HOME
- PAGEUP
- DELETE
- END
- PAGEDOWN
- RIGHT
- LEFT
- DOWN
- UP
- NUMLOCKCLEAR
- KP_DIVIDE
- KP_MULTIPLY
- KP_MINUS
- KP_PLUS
- KP_ENTER
- KP_1
- KP_2
- KP_3
- KP_4
- KP_5
- KP_6
- KP_7
- KP_8
- KP_9
- KP_0
- KP_PERIOD
- NONUSBACKSLASH
- APPLICATION
- POWER
- KP_EQUALS
- F13
- F14
- F15
- F16
- F17
- F18
- F19
- F20
- F21
- F22
- F23
- F24
- EXECUTE
- HELP
- MENU
- SELECT
- STOP
- AGAIN
- UNDO
- CUT
- COPY
- PASTE
- FIND
- MUTE
- VOLUMEUP
- VOLUMEDOWN
- KP_COMMA
- KP_EQUALSAS400
- INTERNATIONAL1
- INTERNATIONAL2
- INTERNATIONAL3
- INTERNATIONAL4
- INTERNATIONAL5
- INTERNATIONAL6
- INTERNATIONAL7
- INTERNATIONAL8
- INTERNATIONAL9
- LANG1
- LANG2
- LANG3
- LANG4
- LANG5
- LANG6
- LANG7
- LANG8
- LANG9
- ALTERASE
- SYSREQ
- CANCEL
- CLEAR
- PRIOR
- RETURN2
- SEPARATOR
- OUT
- OPER
- CLEARAGAIN
- CRSEL
- EXSEL
- KP_00
- KP_000
- THOUSANDSSEPARATOR
- DECIMALSEPARATOR
- CURRENCYUNIT
- CURRENCYSUBUNIT
- KP_LEFTPAREN
- KP_RIGHTPAREN
- KP_LEFTBRACE
- KP_RIGHTBRACE
- KP_TAB
- KP_BACKSPACE
- KP_A
- KP_B
- KP_C
- KP_D
- KP_E
- KP_F
- KP_XOR
- KP_POWER
- KP_PERCENT
- KP_LESS
- KP_GREATER
- KP_AMPERSAND
- KP_DBLAMPERSAND
- KP_VERTICALBAR
- KP_DBLVERTICALBAR
- KP_COLON
- KP_HASH
- KP_SPACE
- KP_AT
- KP_EXCLAM
- KP_MEMSTORE
- KP_MEMRECALL
- KP_MEMCLEAR
- KP_MEMADD
- KP_MEMSUBTRACT
- KP_MEMMULTIPLY
- KP_MEMDIVIDE
- KP_PLUSMINUS
- KP_CLEAR
- KP_CLEARENTRY
- KP_BINARY
- KP_OCTAL
- KP_DECIMAL
- KP_HEXADECIMAL
- LCTRL
- LSHIFT
- LALT
- LGUI
- RCTRL
- RSHIFT
- RALT
- RGUI
- MODE
- MEDIA_NEXT_TRACK
- MEDIA_PREVIOUS_TRACK
- MEDIA_STOP
- MEDIA_PLAY
- MEDIA_PLAY_PAUSE
- MUTE
- MEDIA_SELECT
- AC_SEARCH
- AC_HOME
- AC_BACK
- AC_FORWARD
- AC_STOP
- AC_REFRESH
- AC_BOOKMARKS
- MEDIA_EJECT
- SLEEP
- MEDIA_REWIND
- MEDIA_FAST_FORWARD

### alternative_key_sequence
- **Type:** [[string (type)]]
- **Optional**
The alternative key binding for this control. See `key_sequence` for the format.

### controller_key_sequence
- **Type:** [[string (type)]]
- **Optional**
The controller (game pad) keybinding for this control. Use `""` (empty string) for unassigned.

As modifier buttons, these names are used: `"controller-righttrigger"`, `"controller-lefttrigger"`.

`" + "` is used to separate modifier buttons from normal buttons, like so: `"controller-righttrigger + controller-a"`. A key binding can contain any amount of individual modifier buttons, but only a single normal button (listed below).
Available names for the normal controller buttons

- controller-a
- controller-b
- controller-x
- controller-y
- controller-back
- controller-guide
- controller-start
- controller-leftstick (pressing left joy stick)
- controller-left-stick (moving left joy stick)
- controller-rightstick (pressing right joy stick)
- controller-right-stick (moving right joy stick)
- controller-leftshoulder
- controller-rightshoulder
- controller-dpup
- controller-dpdown
- controller-dpleft
- controller-dpright
- controller-misc1
- controller-paddle1
- controller-paddle2
- controller-paddle3
- controller-paddle4
- controller-touchpad

### controller_alternative_key_sequence
- **Type:** [[string (type)]]
- **Optional**
The alternative controller (game pad) keybinding for this control. See `controller_key_sequence` for the format.

### linked_game_control
- **Type:** [[LinkedGameControl (type)]]
- **Optional**
- **Default:** `""`
When a custom-input is linked to a game control it won't show up in the control-settings GUI and will fire when the linked control is pressed.
**Examples:**

```
key_sequence = "",
linked_game_control = "clear-cursor"
```

### consuming
- **Type:** [[ConsumingType]]
- **Optional**
- **Default:** `"none"`
Sets whether internal game events associated with the same key sequence should be fired or blocked. If they are fired ("none"), then the custom input event will happen before the internal game event.

### enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If this custom input is enabled. Disabled custom inputs exist but are not used by the game. If disabled, no event is raised when the input is used.

### enabled_while_spectating
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### enabled_while_in_cutscene
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### include_selected_prototype
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, the type and name of the currently selected prototype will be provided as "selected_prototype" in the raised [[CustomInputEvent|Lua event]]. [This also works in GUIs](https://forums.factorio.com/96125), not just the game world.

This will also return an item in the cursor such as copper-wire or rail-planner, if nothing is beneath the cursor.

### item_to_spawn
- **Type:** [[ItemID (type)]]
- **Optional**
The item will be created when this input is pressed and action is set to "spawn-item". The item must have the [[ItemPrototypeFlags (type)#spawnable|spawnable]] flag set.

### action
- **Type:** `"lua"` | `"spawn-item"` | `"toggle-personal-roboport"` | `"toggle-personal-logistic-requests"` | `"toggle-equipment-movement-bonus"`
- **Optional**
- **Default:** `"lua"`
A [[CustomInputEvent|Lua event]] is only raised if the action is "lua".

### block_modifiers
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, when the shortcut is activated, the modifiers used for this shortcut can't be re-used to press something else until unpressed. The example where this is useful is ALT+A to activate spidertron remote, where ALT is consumed, so pressing right mouse button before the ALT is unpressed will not trigger pin creation (ALT + right mouse button), but send the selected unit instead.
