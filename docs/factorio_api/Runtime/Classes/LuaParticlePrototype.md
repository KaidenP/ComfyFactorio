---
title: LuaParticlePrototype
tags: [factorio-api, runtime, class]
---
# LuaParticlePrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of an optimized particle.

## Attributes

### regular_trigger_effect
- **Type:** [[TriggerEffectItem]]

### ended_in_water_trigger_effect
- **Type:** [[TriggerEffectItem]]

### ended_on_ground_trigger_effect
- **Type:** [[TriggerEffectItem]]

### render_layer
- **Type:** [[RenderLayer]]

### render_layer_when_on_ground
- **Type:** [[RenderLayer]]

### fade_out_time
- **Type:** [[uint32]]

### life_time
- **Type:** [[uint32]]

### regular_trigger_effect_frequency
- **Type:** [[uint32]]

### movement_modifier_when_on_ground
- **Type:** [[float]]

### movement_modifier
- **Type:** [[float]]

### vertical_acceleration
- **Type:** [[float]]

### mining_particle_frame_speed
- **Type:** [[float]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
