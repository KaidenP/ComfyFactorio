---
title: LuaSpaceLocationPrototype
tags: [factorio-api, runtime, class]
---
# LuaSpaceLocationPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a space location, such as a planet.

## Attributes

### gravity_pull
- **Type:** [[double]]

### origin
- **Type:** [[MapPosition]]

### distance
- **Type:** [[double]]

### orientation
- **Type:** [[RealOrientation]]

### starmap_icon_orientation
- **Type:** [[RealOrientation]]

### position
- **Type:** [[MapPosition]]

### magnitude
- **Type:** [[double]]

### parked_platforms_orientation
- **Type:** [[RealOrientation]]

### parked_platforms_position
- **Type:** [[MapPosition]]

### label_orientation
- **Type:** [[RealOrientation]]

### draw_orbit
- **Type:** [[boolean]]

### fly_condition
- **Type:** [[boolean]]

### solar_power_in_space
- **Type:** [[double]]

### asteroid_spawn_influence
- **Type:** [[double]]

### asteroid_spawn_definitions
- **Type:** array<[[SpaceLocationAsteroidSpawnDefinition]]>
- **Optional**

### factoriopedia_alternative
- **Type:** [[LuaSpaceLocationPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### map_seed_offset
- **Type:** [[uint32]]
- **Optional**

### map_gen_settings
- **Type:** [[MapGenSettings]]
- **Optional**

### entities_require_heating
- **Type:** [[boolean]]
- **Optional**

### pollutant_type
- **Type:** [[LuaAirbornePollutantPrototype]]
- **Optional**

### player_effects
- **Type:** array<[[TriggerItem]]>
- **Optional**

### ticks_between_player_effects
- **Type:** [[uint32]]
- **Optional**

### surface_properties
- **Type:** dictionary<[[string]] → [[double]]>
- **Optional**
A mapping of the surface property name to the value.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
