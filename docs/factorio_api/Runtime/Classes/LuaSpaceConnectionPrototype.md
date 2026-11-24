---
title: LuaSpaceConnectionPrototype
tags: [factorio-api, runtime, class]
---
# LuaSpaceConnectionPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a space connection.

## Attributes

### origin
- **Type:** [[MapPosition]]

### from
- **Type:** [[LuaSpaceLocationPrototype]]

### to
- **Type:** [[LuaSpaceLocationPrototype]]

### length
- **Type:** [[uint32]]

### shape
- **Type:** `"arc"` | `"line"`

### asteroid_spawn_definitions
- **Type:** array<[[SpaceConnectionAsteroidSpawnDefinition]]>
- **Optional**

### factoriopedia_alternative
- **Type:** [[LuaSpaceConnectionPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
