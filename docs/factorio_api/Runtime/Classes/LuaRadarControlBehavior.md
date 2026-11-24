---
title: LuaRadarControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaRadarControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for radars

## Attributes

### mode
- **Type:** [[defines.control_behavior#mode]]
- **Writable:** [[defines.control_behavior#mode]]
Whether this radar is in universe (channel) or surface mode.

### universe_channel
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
The channel that is used in universe mode. Radars on the same force with the same channel in universe mode are connected to each other with hidden radar wires.

If the channel is empty or a [[LuaPrototypeBase#parameter|parameter]], the radar will be disconnected.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
