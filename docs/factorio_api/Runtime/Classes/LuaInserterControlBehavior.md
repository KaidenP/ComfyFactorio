---
title: LuaInserterControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaInserterControlBehavior

> **Extends:** [[LuaGenericOnOffControlBehavior]]

Control behavior for inserters.

## Attributes

### circuit_set_filters
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if filters are set from circuit network

### circuit_read_hand_contents
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the contents of the inserter hand should be sent to the circuit network

### circuit_hand_read_mode
- **Type:** [[defines.control_behavior#hand_read_mode]]
- **Writable:** [[defines.control_behavior#hand_read_mode]]
The hand read mode for the inserter.

### circuit_set_stack_size
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If the hand stack size of the inserter is set through the circuit network or not.

### circuit_stack_control_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The signal used to set the stack size of the inserter.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
