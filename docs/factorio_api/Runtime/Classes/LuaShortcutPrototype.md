---
title: LuaShortcutPrototype
tags: [factorio-api, runtime, class]
---
# LuaShortcutPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a shortcut.

## Attributes

### action
- **Type:** [[string]]

### item_to_spawn
- **Type:** [[LuaItemPrototype]]
- **Optional**
The item to create when this shortcut is used, if any.

### technology_to_unlock
- **Type:** [[LuaTechnologyPrototype]]
- **Optional**
The technology that needs to be researched once (in any save) for this shortcut to be unlocked (in all saves).

### toggleable
- **Type:** [[boolean]]

### associated_control_input
- **Type:** [[string]]
- **Optional**
The control input that is associated with this shortcut, if any.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
