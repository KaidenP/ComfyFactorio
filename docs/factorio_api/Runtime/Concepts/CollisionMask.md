---
title: CollisionMask
tags: [factorio-api, runtime, concept]
---
# CollisionMask

## Fields

### layers
- **Type:** dictionary<[[string]] → `true`>
Every key in the dictionary is the name of one [[LuaCollisionLayerPrototype|layer]] the object collides with. The value is meaningless and always `true`. An empty table means that no layers are set.

### not_colliding_with_itself
- **Type:** [[boolean]]
- **Optional**
Any two entities that both have this option enabled on their prototype and have an identical collision mask layers list will not collide. Other collision mask options are not included in the identical layer list check. This does mean that two different prototypes with the same collision mask layers and this option enabled will not collide. Defaults to `false`.

### consider_tile_transitions
- **Type:** [[boolean]]
- **Optional**
Uses the prototypes position rather than its collision box when doing collision checks with tile prototypes. Allows the prototype to overlap colliding tiles up until its center point. This is only respected for character movement and cars driven by players. Defaults to `false`.

### colliding_with_tiles_only
- **Type:** [[boolean]]
- **Optional**
Any prototype with this collision option will only be checked for collision with other prototype's collision masks if they are a tile. Defaults to `false`.

## Examples

```
-- Most common collision mask of buildings:
collision_mask = {layers = {item = true, meltable = true, object = true, player = true, water_tile = true, is_object = true, is_lower_object = true}}
```
