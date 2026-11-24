---
title: LuaItem
tags: [factorio-api, runtime, class]
---
# LuaItem

> **Extends:** [[LuaItemCommon]]

A reference to an item with data. In contrast to LuaItemStack, this is binding to a specific item data even if it would move between entities or inventories.

## Attributes

### type
- **Type:** [[string]]
Type of the item prototype

### name
- **Type:** [[string]]
Name of the item prototype

### prototype
- **Type:** [[LuaItemPrototype]]
Item prototype of this item

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of this item.

### item_stack
- **Type:** [[LuaItemStack]]
- **Optional**
Object representing the item stack this item is located in right now. If its not possible to locate the item stack holding this item, a nil will be returned

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
