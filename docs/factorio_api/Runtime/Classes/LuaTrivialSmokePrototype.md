---
title: LuaTrivialSmokePrototype
tags: [factorio-api, runtime, class]
---
# LuaTrivialSmokePrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a trivial smoke.

## Attributes

### color
- **Type:** [[Color]]

### start_scale
- **Type:** [[double]]

### end_scale
- **Type:** [[double]]

### movement_slow_down_factor
- **Type:** [[double]]

### duration
- **Type:** [[uint32]]

### spread_duration
- **Type:** [[uint32]]

### fade_away_duration
- **Type:** [[uint32]]

### fade_in_duration
- **Type:** [[uint32]]

### glow_fade_away_duration
- **Type:** [[uint32]]

### cyclic
- **Type:** [[boolean]]

### affected_by_wind
- **Type:** [[boolean]]

### show_when_smoke_off
- **Type:** [[boolean]]

### glow_animation
- **Type:** [[boolean]]

### render_layer
- **Type:** [[RenderLayer]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
