---
title: LuaActiveTriggerPrototype
tags: [factorio-api, runtime, class]
---
# LuaActiveTriggerPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of an Active Trigger.

## Attributes

### max_jumps
- **Type:** [[uint32]]
The max number of jumps per trigger. default = 5.

### max_range_per_jump
- **Type:** [[double]]
The max length of jumps. default = 5.

### max_range
- **Type:** [[double]]
The max distance jumps are allowed to travel away from the original target. default = infinity.

### jump_delay_ticks
- **Type:** [[uint32]]
The tick delay between each jump. 0 = all jumps instantaneous. default = 0.

### fork_chance
- **Type:** [[double]]
The chance that a new fork will spawn after each jump [0,1]. default = 0.

### max_forks_per_jump
- **Type:** [[uint32]]
The maximum number of forks that can spawn from a single jump. default = 1.

### max_forks
- **Type:** [[uint32]]
maximum number of forks allowed to spawn for the entire chain. default = infinity.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
