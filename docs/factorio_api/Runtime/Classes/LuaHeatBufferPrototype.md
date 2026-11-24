---
title: LuaHeatBufferPrototype
tags: [factorio-api, runtime, class]
---
# LuaHeatBufferPrototype

Prototype of a heat buffer.

## Attributes

### max_temperature
- **Type:** [[double]]

### default_temperature
- **Type:** [[double]]

### specific_heat
- **Type:** [[double]]

### max_transfer
- **Type:** [[double]]

### min_temperature_gradient
- **Type:** [[double]]

### min_working_temperature
- **Type:** [[double]]

### minimum_glow_temperature
- **Type:** [[double]]

### connections
- **Type:** array<[[HeatConnectionDefinition]]>

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
