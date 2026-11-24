---
title: LuaRoboportControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaRoboportControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for roboports.

## Attributes

### read_items_mode
- **Type:** [[defines.control_behavior#read_items_mode]]
- **Writable:** [[defines.control_behavior#read_items_mode]]
Selects contents that are to be read from the roboport

### read_logistics
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Legacy field, please use LuaRoboportControlBehavior::read_items_mode instead. `true` if the roboport should report the logistics network content to the circuit network.

### read_robot_stats
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the roboport should report the robot statistics to the circuit network.

### available_logistic_output_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### total_logistic_output_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### available_construction_output_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### total_construction_output_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### roboport_count_output_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
