---
title: LuaCustomChartTag
tags: [factorio-api, runtime, class]
---
# LuaCustomChartTag

A custom tag that shows on the map view.

## Attributes

### icon
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
This tag's icon, if it has one. Writing `nil` removes it.

### last_user
- **Type:** [[LuaPlayer]]
- **Writable:** [[PlayerIdentification]]
- **Optional**
The player who last edited this tag.

### position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
The position of this tag.

### text
- **Type:** [[string]]
- **Writable:** [[string]]

### tag_number
- **Type:** [[uint32]]
The unique ID for this tag on this force.

### force
- **Type:** [[LuaForce]]
The force this tag belongs to.

### surface
- **Type:** [[LuaSurface]]
- **Writable:** [[LuaSurface]]
The surface this tag belongs to.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### destroy
Destroys this tag.
