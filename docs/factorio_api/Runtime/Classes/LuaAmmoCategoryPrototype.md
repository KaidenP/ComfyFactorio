---
title: LuaAmmoCategoryPrototype
tags: [factorio-api, runtime, class]
---
# LuaAmmoCategoryPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a ammo category.

## Attributes

### bonus_gui_order
- **Type:** [[string]]

### factoriopedia_alternative
- **Type:** [[LuaAmmoCategoryPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
