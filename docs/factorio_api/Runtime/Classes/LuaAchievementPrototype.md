---
title: LuaAchievementPrototype
tags: [factorio-api, runtime, class]
---
# LuaAchievementPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a achievement.

## Attributes

### allowed_without_fight
- **Type:** [[boolean]]

### objective_condition
- **Type:** [[string]]
- **Optional**

### amount
- **Type:** [[uint32]]
- **Optional**

### limited_to_one_game
- **Type:** [[boolean]]
- **Optional**

### within
- **Type:** [[uint32]]
- **Optional**

### to_build
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### surface
- **Type:** [[string]]
- **Optional**

### count
- **Type:** [[uint32]]
- **Optional**

### more_than_manually
- **Type:** [[boolean]]
- **Optional**

### dont_build
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**

### excluded
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**

### included
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**

### dont_research
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**

### research_with
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**

### last_hour_only
- **Type:** [[boolean]]
- **Optional**

### minimum_energy_produced
- **Type:** [[double]]
- **Optional**

### armor
- **Type:** [[LuaItemPrototype]]
- **Optional**

### alternative_armor
- **Type:** [[LuaItemPrototype]]
- **Optional**

### limit_quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### damage_type
- **Type:** [[LuaDamagePrototype]]
- **Optional**

### damage_dealer
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**

### to_kill
- **Type:** array<[[LuaEntityPrototype]]>
- **Optional**

### personally
- **Type:** [[boolean]]
- **Optional**

### in_vehicle
- **Type:** [[boolean]]
- **Optional**

### type_to_kill
- **Type:** [[string]]
- **Optional**

### not_to_kill
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### type_not_to_kill
- **Type:** [[string]]
- **Optional**

### module
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**

### limit_equip_quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### minimum_damage
- **Type:** [[float]]
- **Optional**

### should_survive
- **Type:** [[boolean]]
- **Optional**

### type_of_dealer
- **Type:** [[string]]
- **Optional**

### item_product
- **Type:** [[LuaItemPrototype]]
- **Optional**

### quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### fluid_product
- **Type:** [[LuaFluidPrototype]]
- **Optional**

### technology
- **Type:** [[LuaTechnologyPrototype]]
- **Optional**

### research_all
- **Type:** [[boolean]]
- **Optional**

### science_pack
- **Type:** [[LuaItemPrototype]]
- **Optional**

### ammo_type
- **Type:** [[LuaItemPrototype]]
- **Optional**

### minimum_distance
- **Type:** [[double]]
- **Optional**

### to_use
- **Type:** [[LuaItemPrototype]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
