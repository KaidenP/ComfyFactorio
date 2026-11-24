---
title: LuaCustomInputPrototype
tags: [factorio-api, runtime, class]
---
# LuaCustomInputPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a custom input.

## Attributes

### event_id
- **Type:** [[defines.events]]
Event identifier associated with this custom input.

### key_sequence
- **Type:** [[string]]
The default key sequence for this custom input.

### alternative_key_sequence
- **Type:** [[string]]
- **Optional**
The default alternative key sequence for this custom input, if any

### controller_key_sequence
- **Type:** [[string]]
- **Optional**
The default controller key sequence for this custom input, if any

### controller_alternative_key_sequence
- **Type:** [[string]]
- **Optional**
The default controller alternative key sequence for this custom input, if any

### linked_game_control
- **Type:** [[LinkedGameControl]]
- **Optional**
The linked game control name, if any.

### consuming
- **Type:** `"none"` | `"game-only"`
The consuming type.

### action
- **Type:** [[string]]
The action that happens when this custom input is triggered.

### enabled
- **Type:** [[boolean]]
Whether this custom input is enabled. Disabled custom inputs exist but are not used by the game.

### enabled_while_spectating
- **Type:** [[boolean]]
Whether this custom input is enabled while using the spectator controller.

### enabled_while_in_cutscene
- **Type:** [[boolean]]
Whether this custom input is enabled while using the cutscene controller.

### include_selected_prototype
- **Type:** [[boolean]]
Whether this custom input will include the selected prototype (if any) when triggered.

### item_to_spawn
- **Type:** [[LuaItemPrototype]]
- **Optional**
The item that gets spawned when this custom input is fired, if any.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
