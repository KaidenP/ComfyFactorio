---
title: LuaLogisticContainerControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaLogisticContainerControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for logistic chests.

## Attributes

### circuit_condition_enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the circuit condition is in effect.

### circuit_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]
The circuit condition for the logistic container.

### set_requests
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this logistic container has its requests set by a circuit network.

Can only be set to `true` on containers whose [[LuaEntityPrototype#logistic_mode|logistic_mode]] or [[LuaEntity#override_logistic_mode|override_logistic_mode]] is set to `"requester"` or `"buffer"`.

### read_contents
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this logistic container is sending its content to a circuit network.

### read_empty_slots
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### empty_slots_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
