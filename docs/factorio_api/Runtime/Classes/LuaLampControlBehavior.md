---
title: LuaLampControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaLampControlBehavior

> **Extends:** [[LuaGenericOnOffControlBehavior]]

Control behavior for lamps.

## Attributes

### use_colors
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the lamp should set the color from the circuit network signals.

### color_mode
- **Type:** [[defines.control_behavior#color_mode]]
- **Writable:** [[defines.control_behavior#color_mode]]

### red_signal
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

### rgb_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**

### color
- **Type:** [[Color]]
- **Optional**
The color the lamp is showing, if any.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
