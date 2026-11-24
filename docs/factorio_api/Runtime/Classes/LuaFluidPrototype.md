---
title: LuaFluidPrototype
tags: [factorio-api, runtime, class]
---
# LuaFluidPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a fluid.

## Attributes

### default_temperature
- **Type:** [[double]]
Default temperature of this fluid.

### max_temperature
- **Type:** [[double]]
Maximum temperature this fluid can reach.

### heat_capacity
- **Type:** [[double]]
The amount of energy in Joules required to heat one unit of this fluid by 1°C.

### base_color
- **Type:** [[Color]]

### flow_color
- **Type:** [[Color]]

### visualization_color
- **Type:** [[Color]]

### gas_temperature
- **Type:** [[double]]
The temperature above which this fluid will be shown as gaseous inside tanks and pipes.

### emissions_multiplier
- **Type:** [[double]]
A multiplier on the amount of emissions produced when this fluid is burnt in a generator. A value above `1.0` increases emissions and vice versa. The multiplier can't be negative.

### fuel_value
- **Type:** [[double]]
The amount of energy in Joules one unit of this fluid will produce when burnt in a generator. A value of `0` means this fluid can't be used for energy generation. The value can't be negative.

### factoriopedia_alternative
- **Type:** [[LuaFluidPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### spent_fluid
- **Type:** [[SpentFluidSpecification]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
