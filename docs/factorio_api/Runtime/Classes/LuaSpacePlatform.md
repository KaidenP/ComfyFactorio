---
title: LuaSpacePlatform
tags: [factorio-api, runtime, class]
---
# LuaSpacePlatform

A space platform.

## Attributes

### force
- **Type:** [[LuaForce]]
The force of this space platform.

### name
- **Type:** [[string]]
- **Writable:** [[string]]
The name of this space platform.

### index
- **Type:** [[uint32]]
The unique index of this space platform.

### space_location
- **Type:** [[LuaSpaceLocationPrototype]]
- **Writable:** [[SpaceLocationID]]
- **Optional**
The space location this space platform is stopped at or `nil`.

Write operation requires a valid space location and will cancel pending item requests.

### last_visited_space_location
- **Type:** [[LuaSpaceLocationPrototype]]
- **Optional**
The space location this space platform previously went through or stopped at.

### completed_trips
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of trips completed between space locations.

### space_connection
- **Type:** [[LuaSpaceConnectionPrototype]]
- **Writable:** [[SpaceConnectionID]]
- **Optional**
The space connection this space platform is traveling through or `nil`.

Write operation requires a valid space connection and it sets the distance to 0.5.

### distance
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The point on space connection this platform is at or `nil`.

It is represented as a number in range `[0, 1]`, with 0 being [[LuaSpaceConnectionPrototype#from|LuaSpaceConnectionPrototype::from]] and 1 being [[LuaSpaceConnectionPrototype#to|LuaSpaceConnectionPrototype::to]].

### state
- **Type:** [[defines.space_platform_state]]
The current state of this space platform.

### paused
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When `true`, the platform has paused thrust and does not advance its schedule.

### starter_pack
- **Type:** [[ItemIDAndQualityIDPair]]
- **Optional**
The starter pack used to create this space platform.

### surface
- **Type:** [[LuaSurface]]
The surface that belongs to this platform (if it has been created yet).

### hub
- **Type:** [[LuaEntity]]
- **Optional**
The hub on this platform, if it exists. It does not exist if the platform has not had the starter pack applied.

If the hub [[LuaEntity#die|dies]] the platform will be deleted at the end of the tick but is otherwise valid to use until that point.

If the hub is [[LuaEntity#destroy|destroyed]] the platform is not affected.

### schedule
- **Type:** [[PlatformSchedule]]
- **Writable:** [[PlatformSchedule]]
- **Optional**
This platform's current schedule, if any. Set to `nil` to clear.

The schedule can't be changed by modifying the returned table. Instead, changes must be made by assigning a new table to this attribute.

This is a simplified schedule that does **not** include groups and interrupts. See [[LuaSpacePlatform#get_schedule|LuaSpacePlatform::get_schedule]] for full access to the schedule, including interrupts and groups.

### speed
- **Type:** [[double]]
- **Writable:** [[double]]

### scheduled_for_deletion
- **Type:** [[uint32]]
If this platform is scheduled for deletion.

Returns how many ticks are left before the platform will be deleted. 0 if not scheduled for deletion.

### weight
- **Type:** [[Weight]]
The total weight of the platform.

### damaged_tiles
- **Type:** array<table>
The damaged tiles on this platform.

### ejected_items
- **Type:** array<[[EjectedItem]]>
All items that have been thrown overboard.

### hidden
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this platform is hidden from the remote view surface list.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### destroy
Schedules this space platform for deletion.

**Parameters:**
- **`ticks`** — [[MapTick]] *(optional)*: The number of ticks from now when this platform will be deleted.

### cancel_deletion
Cancels deletion of this space platform if it was scheduled for deletion.

### apply_starter_pack
Applies the starter pack for this platform if it hasn't already been applied.

**Parameters:**
- **`silent`** — [[boolean]] *(optional)*: If the platform creation is announced to players on the force. Defaults to `false`.

**Returns:**
- [[LuaEntity]] *(optional)*: The platform hub.

### damage_tile
Damages the given tile if it exists, the chunk is generated, and it is a platform foundation tile.

Takes a table with the following fields:
- **`position`** — [[TilePosition]]
- **`damage`** — [[float]]
- **`cause`** — [[LuaEntity]] *(optional)*

### repair_tile
Repairs the given tile if it's damaged.

**Parameters:**
- **`position`** — [[TilePosition]]
- **`amount`** — [[float]] *(optional)*

### destroy_asteroid_chunks
Destroys all asteroid chunks from the given area. If no area and no position are given, then the entire surface is searched.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]] *(optional)*
- **`position`** — [[MapPosition]] *(optional)*
- **`name`** — [[AsteroidChunkID]] | array<[[AsteroidChunkID]]> *(optional)*
- **`limit`** — [[uint32]] *(optional)*
- **`invert`** — [[boolean]] *(optional)*: If the filters should be inverted.

**Returns:**
- [[uint32]]: The number of destroyed chunks.

### create_asteroid_chunks
Creates the given asteroid chunks on this platform.

**Parameters:**
- **`asteroid_chunks`** — array<[[AsteroidChunk]]>

### find_asteroid_chunks_filtered
Find asteroid chunks of a given name in a given area.

If no filters are given, returns all asteroid chunks in the search area. If multiple filters are specified, returns only asteroid chunks matching every given filter. If no area and no position are given, the entire surface is searched.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]] *(optional)*
- **`position`** — [[MapPosition]] *(optional)*
- **`name`** — [[AsteroidChunkID]] | array<[[AsteroidChunkID]]> *(optional)*
- **`limit`** — [[uint32]] *(optional)*
- **`invert`** — [[boolean]] *(optional)*: If the filters should be inverted.

**Returns:**
- array<[[AsteroidChunk]]>

**Examples:**

```
game.forces.player.platforms[1].find_asteroid_chunks_filtered{area = {{-10, -10}, {10, 10}}, name = "carbonic-asteroid"} -- gets all asteroids with the given name in the rectangle
game.forces.player.platforms[1].find_asteroid_chunks_filtered{area = {{-10, -10}, {10, 10}}, limit = 5}  -- gets the first 5 asteroid chunks in the rectangle
```

### can_leave_current_location
Returns `true` when the space platform isn't waiting on any delivery from the planet.

**Returns:**
- [[boolean]]

### get_schedule
This allows full access to the space platform schedule, including modifying the schedule records, the group and the interrupts.

**Returns:**
- [[LuaSchedule]]

### eject_item
Ejects an item into space on this space platform.

If a LuaItemStack is provided, the actual item is ejected and removed from the source.

**Parameters:**
- **`item`** — [[ItemStackIdentification]]
- **`position`** — [[MapPosition]]
- **`movement`** — [[Vector]]: When inserters drop items into space, the [[InserterPrototype#insert_position|InserterPrototype::insert_position]] rotated to the inserter direction is used.

### clear_ejected_items
Removes all ejected items from this space platform.
