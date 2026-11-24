---
title: LuaRailSignalBaseControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaRailSignalBaseControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for rail signals and rail chain signals.

## Attributes

### red_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### orange_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### green_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### blue_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### close_signal
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this will close the rail signal based off the circuit condition.

### read_signal
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this will read the rail signal state.

### circuit_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]
The circuit condition when controlling the signal through the circuit network.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
