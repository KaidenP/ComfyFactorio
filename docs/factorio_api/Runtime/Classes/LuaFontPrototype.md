---
title: LuaFontPrototype
tags: [factorio-api, runtime, class]
---
# LuaFontPrototype

Prototype of a font.

## Attributes

### name
- **Type:** [[string]]
Name of this prototype.

### from
- **Type:** [[string]]

### size
- **Type:** [[int32]]

### spacing
- **Type:** [[float]]

### border
- **Type:** [[boolean]]

### filtered
- **Type:** [[boolean]]

### border_color
- **Type:** [[Color]]
- **Optional**
The border color, if any.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
