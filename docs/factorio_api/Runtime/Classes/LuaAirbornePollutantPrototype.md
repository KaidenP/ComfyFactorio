---
title: LuaAirbornePollutantPrototype
tags: [factorio-api, runtime, class]
---
# LuaAirbornePollutantPrototype

> **Extends:** [[LuaPrototypeBase]]

Airborne pollutant prototype.

## Attributes

### chart_color
- **Type:** [[Color]]

### affects_evolution
- **Type:** [[boolean]]

### damages_trees
- **Type:** [[boolean]]

### localised_name_with_amount_key
- **Type:** [[string]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
