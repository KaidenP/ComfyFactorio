---
title: LuaAsteroidCollectorControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaAsteroidCollectorControlBehavior

> **Extends:** [[LuaGenericOnOffControlBehavior]]

Control behavior for asteroid collectors.

## Attributes

### set_filter
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this asteroid collector has filters set from circuit network

### read_content
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if this asteroid collector reads its content and sends it to a circuit network

### include_hands
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if read contents should include content of hands (items that were captured but are not yet in the asteroid collector's main inventory).

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
