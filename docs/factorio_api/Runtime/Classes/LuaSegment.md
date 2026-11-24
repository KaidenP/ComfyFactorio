---
title: LuaSegment
tags: [factorio-api, runtime, class]
---
# LuaSegment

An individual segment of a [[LuaSegmentedUnit]]. If the segment exists in a generated chunk, you can access the entity representation using [[LuaSegment#entity|LuaSegment::entity]].

## Attributes

### prototype
- **Type:** [[LuaEntityPrototype]]
The prototype for the entity representation of the segment.

### unit
- **Type:** [[LuaSegmentedUnit]]
The segmented unit that owns the segment.

### entity
- **Type:** [[LuaEntity]]
- **Optional**
The actual entity representation of the segment if it exists. A segment's entity will be automatically destroyed if the segment moves into chunks that have not yet been fully generated or onto "out-of-map" tiles. Conversely, if a segment moves into a chunk that is fully generated and onto a non-"out-of-map" tile, then its entity will be created if it doesn't exist yet.

### position
- **Type:** [[MapPosition]]
- **Optional**
The position of the segment if one has been assigned. A position may not be assigned if the unit's number of body nodes is fewer than [[LuaSegmentedUnit#max_body_nodes|LuaSegmentedUnit::max_body_nodes]].

This position may be in an un-generated chunk. Use [[LuaSurface#is_chunk_generated|LuaSurface::is_chunk_generated]] to check before attempting to access the chunk.

If [[LuaSegment#entity|LuaSegment::entity]] is non-nil, this returns that entity's [[LuaEntity#position|LuaEntity::position]]. If the entity is `nil`, then reading this field calculates the entity's would-be position if it existed. This can be expensive to compute, so avoid reading this field too often unless it is really necessary.

### orientation
- **Type:** [[RealOrientation]]
- **Optional**
The relative orientation of the segment if one has been assigned. An orientation may not be assigned if the unit's number of body nodes is fewer than [[LuaSegmentedUnit#max_body_nodes|LuaSegmentedUnit::max_body_nodes]].

If [[LuaSegment#entity|LuaSegment::entity]] is non-nil, this returns that entity's [[LuaEntity#orientation|LuaEntity::orientation]]. If the entity is `nil`, then reading this field calculates the entity's would-be position if it existed. This can be expensive to compute, so avoid reading this field too often unless it is really necessary.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
