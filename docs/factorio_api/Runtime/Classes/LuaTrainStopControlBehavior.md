---
title: LuaTrainStopControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaTrainStopControlBehavior

> **Extends:** [[LuaGenericOnOffControlBehavior]]

Control behavior for train stops.

## Attributes

### send_to_train
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the train stop should send the circuit network contents to the train to use.

### read_from_train
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the train stop should send the train contents to the circuit network.

### read_stopped_train
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the train stop should send the stopped train id to the circuit network.

### set_trains_limit
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the trains_limit_signal is used to set a limit of trains incoming for train stop.

### read_trains_count
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the train stop should send amount of incoming trains to the circuit network.

### stopped_train_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The signal that will be sent when using the send-train-id option.

### trains_count_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The signal that will be sent when using the read-trains-count option.

### trains_limit_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The signal to be used by set-trains-limit to limit amount of incoming trains

### set_priority
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the priority_signal is used to set a priority of the train stop.

### priority_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The signal to be used by set-priority change priority of the train stop

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
