---
title: LuaSegmentedUnit
tags: [factorio-api, runtime, class]
---
# LuaSegmentedUnit

A surface-level object composed of one [[SegmentedUnitPrototype]] followed by up to 63 [[SegmentPrototype]]s.

This object is not an entity, and can exist on chunks that do not exist. Instead, the individual segments that compose its body will be destroyed as the unit's body crosses into un-generated or void terrain, and will be re-created when the body crosses into generated, non-void terrain.

Use [[LuaSurface#get_segmented_units|LuaSurface::get_segmented_units]] to iterate over all units on a surface, [[LuaTerritory#get_segmented_units|LuaTerritory::get_segmented_units]] to iterate over all units that guard a territory, or [[LuaEntity#segmented_unit|LuaEntity::segmented_unit]] to get the unit that controls any given segment entity.

## Attributes

### prototype
- **Type:** [[LuaEntityPrototype]]
The prototype of the `segmented-unit` entity that defines the traits and behaviors of the unit.

### surface
- **Type:** [[LuaSurface]]
The surface on which the unit is located.

### territory
- **Type:** [[LuaTerritory]]
- **Writable:** [[LuaTerritory]]
- **Optional**
The territory that the unit is protecting.

### segments
- **Type:** array<[[LuaSegment]]>
The segments that compose the unit.

### force
- **Type:** [[LuaForce]]
- **Writable:** [[ForceID]]
The force that the unit belongs to. Changing this also changes the force of all segment entities.

Always returns a [[LuaForce]], but may be assigned to any [[ForceID]] type.

### unit_number
- **Type:** [[uint64]]
A unique number identifying this unit for the lifetime of the save. These are allocated sequentially and not re-used (until overflow). These numbers are allocated from the same pool as [[LuaEntity#unit_number|LuaEntity::unit_number]], so segmented unit numbers are unique among all segmented units and all entities with owners.

### health
- **Type:** [[float]]
- **Writable:** [[float]]
The current health of the unit. Health is automatically clamped to be between `0` and [[LuaSegmentedUnit#max_health|LuaSegmentedUnit::max_health]].

### max_health
- **Type:** [[float]]
The maximum health of the unit.

### health_ratio
- **Type:** [[float]]
- **Writable:** [[float]]
The ratio of [[LuaSegmentedUnit#health|LuaSegmentedUnit::health]] to [[LuaSegmentedUnit#max_health|LuaSegmentedUnit::max_health]]. Values are clamped between `0` (no health) and `1` (full health) inclusive.

### speed
- **Type:** [[double]]
- **Writable:** [[double]]
The current instantaneous speed in tiles per map tick. Must always be greater than or equal to 0; segmented units are currently incapable of naturally moving in reverse.

When setting this value, note that unless the unit's AI is similarly overridden by a script, the unit's speed will continuously accelerate or decelerate to match [[LuaSegmentedUnit#target_speed|LuaSegmentedUnit::target_speed]].

### target_speed
- **Type:** [[double]]
The speed in tiles per tick that the unit is currently attempting to reach, as determined by its AI. Must always be greater than or equal to 0.

### acceleration
- **Type:** [[double]]
The rate at which [[LuaSegmentedUnit#speed|LuaSegmentedUnit::speed]] is changing over time, in tiles per tick per tick.

This value represents unit's most recent change in speed. If its speed is not changing, the acceleration value will be 0. If it is gaining speed, the value will be positive. If it is losing speed, the value will be negative.

### max_body_nodes
- **Type:** [[uint32]]
The maximum length of [[LuaSegmentedUnit#get_body_nodes|LuaSegmentedUnit::get_body_nodes]].

### activity_mode
- **Type:** [[defines.segmented_unit_activity_mode]]
- **Writable:** [[defines.segmented_unit_activity_mode]]
The current activity mode of the unit. Setting this field can cause the segmented unit to "wake up" or force it into a lower activity mode, but not permanently. Segmented units will generally try to update their activity mode so that they are fully active whenever they are potentially being observed by players, minimally active when relevant to gameplay but not likely observed, and asleep when not relevant to gameplay.

Will never be lower than [[LuaSegmentedUnit#minimum_activity_mode|LuaSegmentedUnit::minimum_activity_mode]].

### minimum_activity_mode
- **Type:** [[defines.segmented_unit_activity_mode]]
- **Writable:** [[defines.segmented_unit_activity_mode]]
The lowest-level activity mode that the unit is allowed to be in. Set this field to prevent the segmented unit from falling asleep or entering minimal mode. Set this field to `nil` or [[defines.segmented_unit_activity_mode|asleep]] to reset this to the default and allow the engine to use whatever activity mode is appropriate.

Performance note: it is NOT recommended to force many segmented units to be fully active or minimally active simultaneously, as they can significantly impact performance depending on how they are configured. When using this feature, remember to reset this field to allow irrelevant units to go back to sleep.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### destroy
Destroys the segmented unit.

Takes a table with the following fields:
- **`raise_destroy`** — [[boolean]] *(optional)*: If `true`, [[script_raised_destroy_segmented_unit]] will be called. Defaults to `false`.

**Raises:**
- [[script_raised_destroy_segmented_unit]] *(timeframe: instantly)*: Raised if the `raise_destroy` flag was set and the unit was successfully destroyed.

### die
Immediately kills the unit.

Unlike [[LuaSegmentedUnit#destroy|LuaSegmentedUnit::destroy]], `die` will trigger the [[on_segmented_unit_died]] event and the unit's individual segments will produce a corpse and drop loot if they have any, and if the segment entities exist at the moment of death (are not in non-generated chunks or out-of-map tiles).

**Parameters:**
- **`force`** — [[ForceID]] *(optional)*: The force to attribute the kill to. Defaults to the `"neutral"` force.
- **`cause`** — [[LuaEntity]] *(optional)*: The cause to attribute the kill to.
- **`damage_type`** — [[DamageTypeID]] *(optional)*: The final damage type that caused the unit to die.

**Raises:**
- [[on_post_segmented_unit_died]] *(timeframe: instantly)*
- [[on_segmented_unit_died]] *(timeframe: instantly)*

### damage
Damages the unit.

**Parameters:**
- **`damage`** — [[float]]: The amount of damage to be done.
- **`force`** — [[ForceID]]: The force that is doing the damage.
- **`type`** — [[DamageTypeID]] *(optional)*: The type of damage being done. Defaults to `"impact"`.
- **`source`** — [[LuaEntity]] *(optional)*: The entity that is directly dealing the damage. This is the projectile, flame, sticker, grenade, laster beam, etc. Must be on the same surface as the entity being damaged.
- **`cause`** — [[LuaEntity]] *(optional)*: The entity that originally triggered the events that led to this damage being dealt. This can be the player character, turret, unit, etc. that pulled the trigger. Does not need to be on the same surface as the segmented unit being damaged.

**Returns:**
- [[float]]: The total damage actually applied after resistances.

**Raises:**
- [[on_segmented_unit_damaged]] *(timeframe: instantly)*

### move_forward
Moves the unit forward by a fixed distance according to its natural movement patterns and AI configuration. This movement occurs in addition to the unit's current speed, but affects neither [[LuaSegmentedUnit#speed|LuaSegmentedUnit::speed]] nor [[LuaSegmentedUnit#acceleration|LuaSegmentedUnit::acceleration]].

**Parameters:**
- **`distance`** — [[double]]: The distance in tiles to move the segmented unit forward.

### clone
Clones this unit.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: The destination position of the head segment. The rest of the body nodes will be copied relative to this.
- **`surface`** — [[LuaSurface]] *(optional)*: The destination surface. If different from this unit's surface, then the clone will not copy the original unit's territory.
- **`force`** — [[ForceID]] *(optional)*: The new unit's force.
- **`territory`** — [[LuaTerritory]] *(optional)*: The territory that the clone should guard. Must be on the same surface as the destination surface.

**Returns:**
- [[LuaSegmentedUnit]] *(optional)*: The cloned unit or `nil` if the unit cannot be cloned.

**Raises:**
- [[on_segmented_unit_created]] *(timeframe: instantly)*: Raised if a clone of the segmented unit was successfully created. [[on_segmented_unit_created|cause]] will be set to [[defines.segmented_unit_created_cause|script_cloned]].

### get_body_nodes
Gets the nodes that define the shape of the unit's body from front to back. Segments are moved along the path these nodes create.

The returned array will always contain at least 1 position, but will not contain more than [[LuaSegmentedUnit#max_body_nodes|LuaSegmentedUnit::max_body_nodes]].

The returned table is a copy of the unit's actual body nodes.

**Returns:**
- array<[[MapPosition]]>

### set_body_nodes
Overwrites the segmented unit's body nodes, which are a series of points that make up the general shape of the unit. Segments are moved along the path these nodes create. For best results, adjacent nodes should be approximately 1.0 tile apart from each other.

This array must contain at least 1 position. Positions at indexes greater than [[LuaSegmentedUnit#max_body_nodes|LuaSegmentedUnit::max_body_nodes]] will be ignored.

Segment entities may be created, destroyed, or moved as a result of setting this field's value. Any segment entities that have a [[TriggerEffectWithCooldown (type)|TriggerEffectWithCooldown]]s will reduce that effect's distance cooldown. However, any effects that go off cooldown as a result will not trigger until the next game update.

**Parameters:**
- **`nodes`** — array<[[MapPosition]]>: The new positions that make up the segmented unit's body nodes. Must not be empty.

### get_ai_state
Gets the state of the unit's AI.

This method returns a copy of the internal AI state. Modifying the returned table will not affect the unit's AI.

**Returns:**
- [[SegmentedUnitAIState]]

### set_ai_state
Sets the segmented unit's AI.

**Parameters:**
- **`state`** — [[SegmentedUnitAIState]]: The new AI state. A copy of this table used, so you can read or write to this table after calling this function without being affected by or affecting the unit's AI.
