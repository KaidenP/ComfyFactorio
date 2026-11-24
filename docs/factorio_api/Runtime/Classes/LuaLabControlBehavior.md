---
title: LuaLabControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaLabControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for lab.

## Attributes

### read_contents
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### read_fuel
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if the fuel (content of energy source) should be read.

### read_research_cost
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### read_technology_level
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### technology_level_signal
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]

### set_research
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### research_conditions
- **Type:** array<[[ResearchCondition]]>
- **Writable:** array<[[ResearchCondition]]>

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
