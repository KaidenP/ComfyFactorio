---
title: LuaTilePrototype
tags: [factorio-api, runtime, class]
---
# LuaTilePrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a tile.

## Attributes

### collision_mask
- **Type:** [[TileCollisionMask]]
The collision mask this tile uses

### layer
- **Type:** [[uint32]]

### autoplace_specification
- **Type:** [[AutoplaceSpecification]]
- **Optional**
Autoplace specification for this prototype, if any.

### walking_speed_modifier
- **Type:** [[float]]

### vehicle_friction_modifier
- **Type:** [[float]]

### map_color
- **Type:** [[Color]]

### decorative_removal_probability
- **Type:** [[float]]
The probability that decorative entities will be removed from on top of this tile when this tile is generated.

### automatic_neighbors
- **Type:** [[boolean]]

### allowed_neighbors
- **Type:** dictionary<[[string]] → [[LuaTilePrototype]]>

### needs_correction
- **Type:** [[boolean]]
If this tile needs correction logic applied when it's generated in the world.

### mineable_properties
- **Type:** table

### fluid
- **Type:** [[LuaFluidPrototype]]
- **Optional**
The fluid offshore pump produces on this tile, if any.

### next_direction
- **Type:** [[LuaTilePrototype]]
- **Optional**
The next direction of this tile, if any. Used when a tile has multiple directions (such as hazard concrete)

### items_to_place_this
- **Type:** array<[[ItemToPlace]]>
- **Optional**
Items that when placed will produce this tile, if any. Construction bots will choose the first item in the list to build this tile.

### can_be_part_of_blueprint
- **Type:** [[boolean]]
False if this tile is not allowed in blueprints regardless of the ability to build it.

### absorptions_per_second
- **Type:** dictionary<[[string]] → [[double]]>
A table of pollution emissions per second this tile will absorb, indexed by the name of each absorbed pollution type.

### is_foundation
- **Type:** [[boolean]]
True if this tile can be used as a foundation for other tiles, false otherwise. Foundation tiles can be [[LuaTile#hidden_tile|hidden]].

### allows_being_covered
- **Type:** [[boolean]]
True if this tile can be [[LuaTile#hidden_tile|hidden]] or replaced by another tile through player actions.

### check_collision_with_entities
- **Type:** [[boolean]]
True if building this tile should check for colliding entities above and prevent building if such are found. Also during mining tiles above this tile checks for entities colliding with this tile and prevents mining if such are found.

### destroys_dropped_items
- **Type:** [[boolean]]

### max_health
- **Type:** [[float]]

### weight
- **Type:** [[Weight]]

### default_cover_tile
- **Type:** [[LuaTilePrototype]]
- **Optional**

### frozen_variant
- **Type:** [[LuaTilePrototype]]
- **Optional**

### thawed_variant
- **Type:** [[LuaTilePrototype]]
- **Optional**

### trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### default_destroyed_dropped_item_trigger
- **Type:** array<[[TriggerItem]]>
- **Optional**

### scorch_mark_color
- **Type:** [[Color]]
- **Optional**

### bound_decoratives
- **Type:** array<[[LuaDecorativePrototype]]>
- **Optional**

### ambient_sounds_group
- **Type:** [[LuaTilePrototype]]
- **Optional**

### factoriopedia_alternative
- **Type:** [[LuaTilePrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
