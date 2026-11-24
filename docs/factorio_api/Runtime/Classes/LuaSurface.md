---
title: LuaSurface
tags: [factorio-api, runtime, class]
---
# LuaSurface

A "domain" of the world, such as a planet or space platform. Surfaces are uniquely identified by their name. Every game contains at least the surface "nauvis".

## Attributes

### name
- **Type:** [[string]]
- **Writable:** [[string]]
The name of this surface. Names are unique among surfaces.

The default surface can't be renamed.

### index
- **Type:** [[uint32]]
This surface's index in [[LuaGameScript#surfaces|LuaGameScript::surfaces]] (unique ID). It is assigned when a surface is created, and remains so until it is [[on_surface_deleted|deleted]]. Indexes of deleted surfaces can be reused.

### map_gen_settings
- **Type:** [[MapGenSettings]]
- **Writable:** [[MapGenSettings]]
The generation settings for this surface. These can be modified after surface generation, but note that this will not retroactively update the surface. To manually regenerate it, [[LuaSurface#regenerate_entity|LuaSurface::regenerate_entity]], [[LuaSurface#regenerate_decorative|LuaSurface::regenerate_decorative]], and [[LuaSurface#delete_chunk|LuaSurface::delete_chunk]] can be used.

### generate_with_lab_tiles
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When set to true, new chunks will be generated with lab tiles, instead of using the surface's map generation settings.

### always_day
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When set to true, the sun will always shine.

### daytime
- **Type:** [[double]]
- **Writable:** [[double]]
Current time of day, as a number in range `[0, 1)`.

### darkness
- **Type:** [[float]]
Amount of darkness at the current time, as a number in range `[0, 1]`.

### wind_speed
- **Type:** [[double]]
- **Writable:** [[double]]
Current wind speed in tiles per tick.

### wind_orientation
- **Type:** [[RealOrientation]]
- **Writable:** [[RealOrientation]]
Current wind direction.

### wind_orientation_change
- **Type:** [[double]]
- **Writable:** [[double]]
Change in wind orientation per tick.

### peaceful_mode
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Is peaceful mode enabled on this surface?

### no_enemies_mode
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Is no-enemies mode enabled on this surface?

### freeze_daytime
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
True if daytime is currently frozen.

### ticks_per_day
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of ticks per day for this surface.

### dusk
- **Type:** [[double]]
- **Writable:** [[double]]
The daytime when dusk starts.

### dawn
- **Type:** [[double]]
- **Writable:** [[double]]
The daytime when dawn starts.

### evening
- **Type:** [[double]]
- **Writable:** [[double]]
The daytime when evening starts.

### morning
- **Type:** [[double]]
- **Writable:** [[double]]
The daytime when morning starts.

### daytime_parameters
- **Type:** table
- **Writable:** table
Parameters of daytime. Equivalent as reading [[LuaSurface#dusk|dusk]], [[LuaSurface#evening|evening]], [[LuaSurface#morning|morning]] and [[LuaSurface#dawn|dawn]] at the same time.

In order for a write to take place, a new table needs to be written in one go: changing individual members of the returned table has no effect as those are value copies.

### solar_power_multiplier
- **Type:** [[double]]
- **Writable:** [[double]]
The multiplier of solar power on this surface. Cannot be less than 0.

### min_brightness
- **Type:** [[double]]
- **Writable:** [[double]]
The minimal brightness during the night. Defaults to `0.15`. This has an effect on both rendering and game mechanics such as biter spawns and solar power.

### brightness_visual_weights
- **Type:** [[ColorModifier]]
- **Writable:** [[ColorModifier]]
Defines how surface daytime brightness influences each color channel of the current color lookup table (LUT).

The LUT is multiplied by `((1 - weight) + brightness * weight)` and result is clamped to range `[0, 1]`.

Default is `{0, 0, 0}`, which means no influence.
**Examples:**

```
-- Makes night on the surface pitch black, LuaSurface::min_brightness is set to default value 0.15.
game.surfaces[1].brightness_visual_weights = { 1 / 0.85, 1 / 0.85, 1 / 0.85 }
```

### show_clouds
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If clouds are shown on this surface. If false, clouds are never shown. If true the player must also have clouds enabled in graphics settings for them to be shown.

By default, clouds are shown on all surfaces.

### has_global_electric_network
- **Type:** [[boolean]]
Whether this surface currently has a global electric network.

### platform
- **Type:** [[LuaSpacePlatform]]
- **Optional**

### planet
- **Type:** [[LuaPlanet]]
- **Optional**
The planet associated with this surface, if there is one.

Use [[LuaPlanet#associate_surface|LuaPlanet::associate_surface]] to create a new association with a planet.

### deletable
- **Type:** [[boolean]]
If this surface can be deleted.

### global_effect
- **Type:** [[Effect]]
- **Writable:** [[Effect]]
- **Optional**
Surface-wide effects applied to entities with effect receivers. `nil` if this surface is not using surface-wide effect source.

### pollutant_type
- **Type:** [[LuaAirbornePollutantPrototype]]
- **Optional**
The type of pollutant enabled on the surface, or `nil` if no pollutant is enabled.

### override_pollution_type
- **Type:** [[Pollutant]]
- **Writable:** [[Pollutant]]
- **Optional**
If set, this pollution type will be used over any other planet or platform values.

If set to an empty table, pollution is disabled. If set to `nil`, the override is 'unset'.

Reading will be `nil` if unset or a table with the current override (`nil` if overridden to disabled).

### localised_name
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
- **Optional**
Localised name of this surface. When set, will replace the internal surface name in places where a player sees surface name.

Value may be ignored if a surface has a SpacePlatform or Planet object attached to it, which take the precedence.

### ignore_surface_conditions
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If surface condition checks should not be performed on this surface.

### pollution_statistics
- **Type:** [[LuaFlowStatistics]]
The pollution statistics for this surface.

### global_electric_network_statistics
- **Type:** [[LuaFlowStatistics]]
- **Optional**
The global electric network statistics for this surface.

If this global network is disabled or this surface is removed, the flow statistics obtained from it will also become invalid. However if the surface index of a deleted surface is reused, the related flow statistics may become valid again.

### global_electric_network
- **Type:** [[LuaElectricSubNetwork]]
- **Optional**
Global electric network for this surface.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_pollution
Get the pollution for a given position.

Pollution is stored per chunk, so this will return the same value for all positions in one chunk.

**Parameters:**
- **`position`** — [[MapPosition]]: The position to poll the chunk's pollution

**Returns:**
- [[double]]

**Examples:**

```
game.surfaces[1].get_pollution({1,2})
```

### set_pollution
Set the pollution for a given position.

Pollution changes by this are not included in pollution statistics and do not affect evolution factors (as opposed to [[LuaSurface#pollute|LuaSurface::pollute]]).

**Parameters:**
- **`position`** — [[MapPosition]]: The position to set the chunk's pollution
- **`amount`** — [[double]]: New amount of pollution to be set on the chunk. Must be >= 0.

### can_place_entity
Check for collisions with terrain or other entities.

Takes a table with the following fields:
- **`name`** — [[EntityID]]: Name of the entity prototype to check.
- **`position`** — [[MapPosition]]: Where the entity would be placed.
- **`direction`** — [[defines.direction]] *(optional)*: Direction of the placed entity. Defaults to `north`.
- **`force`** — [[ForceID]] *(optional)*: The force that would place the entity. Defaults to the `"neutral"` force.
- **`build_check_type`** — [[defines.build_check_type]] *(optional)*: Which type of check should be carried out. Defaults to `ghost_revive`.
- **`forced`** — [[boolean]] *(optional)*: If `true`, entities that can be marked for deconstruction are ignored. Only used if `build_check_type` is either `manual_ghost`, `script_ghost` or `blueprint_ghost`. Defaults to `false`.
- **`inner_name`** — [[string]] *(optional)*: The prototype name of the entity contained in the ghost. Only used if `name` is `entity-ghost`.

**Returns:**
- [[boolean]]

### can_fast_replace
If there exists an entity at the given location that can be fast-replaced with the given entity parameters.

Takes a table with the following fields:
- **`name`** — [[EntityID]]: Name of the entity to check.
- **`position`** — [[MapPosition]]: Where the entity would be placed.
- **`direction`** — [[defines.direction]] *(optional)*: Direction the entity would be placed. Defaults to `north`.
- **`force`** — [[ForceID]] *(optional)*: The force that would place the entity. Defaults to the `"neutral"` force.

**Returns:**
- [[boolean]]

### find_entity
Find an entity of the given name at the given position. This checks both the exact position and the bounding box of the entity.

**Parameters:**
- **`entity`** — [[EntityWithQualityID]]: Name of the entity to look for.
- **`position`** — [[MapPosition]]: Coordinates to look at.

**Returns:**
- [[LuaEntity]] *(optional)*: `nil` if no such entity is found.

**Examples:**

```
game.player.selected.surface.find_entity('filter-inserter', {0,0})
```

### find_entities
Find entities in a given area.

If no area is given all entities on the surface are returned.

**Parameters:**
- **`area`** — [[BoundingBox]] *(optional)*

**Returns:**
- array<[[LuaEntity]]>

**Examples:**

```
-- Will evaluate to a list of all entities within given area.
game.surfaces["nauvis"].find_entities({{-10, -10}, {10, 10}})
```

### find_entities_filtered
Find all entities of the given type or name in the given area.

If no filters (`name`, `type`, `force`, etc.) are given, this returns all entities in the search area. If multiple filters are specified, only entities matching all given filters are returned.

- If no `area` or `position` are given, the entire surface is searched.

- If `position` is given, this returns the entities colliding with that position (i.e the given position is within the entity's collision box).

- If `position` and `radius` are given, this returns the entities within the radius of the position. Looks for the center of entities.

- If `area` is specified, this returns the entities colliding with that area.

**Parameters:**
- **`filter`** — [[EntitySearchFilters]]

**Returns:**
- array<[[LuaEntity]]>

**Examples:**

```
game.surfaces[1].find_entities_filtered{area = {{-10, -10}, {10, 10}}, type = "resource"} -- gets all resources in the rectangle
game.surfaces[1].find_entities_filtered{area = {{-10, -10}, {10, 10}}, name = "iron-ore"} -- gets all iron ores in the rectangle
game.surfaces[1].find_entities_filtered{area = {{-10, -10}, {10, 10}}, name = {"iron-ore", "copper-ore"}} -- gets all iron ore and copper ore in the rectangle
game.surfaces[1].find_entities_filtered{area = {{-10, -10}, {10, 10}}, force = "player"}  -- gets player owned entities in the rectangle
game.surfaces[1].find_entities_filtered{area = {{-10, -10}, {10, 10}}, limit = 5}  -- gets the first 5 entities in the rectangle
game.surfaces[1].find_entities_filtered{position = {0, 0}, radius = 10}  -- gets all entities within 10 tiles of the position [0,0].
```

### find_tiles_filtered
Find all tiles of the given name in the given area.

If no filters are given, this returns all tiles in the search area.

If no `area` or `position` and `radius` is given, the entire surface is searched. If `position` and `radius` are given, only tiles within the radius of the position are included.

**Parameters:**
- **`filter`** — [[TileSearchFilters]]

**Returns:**
- array<[[LuaTile]]>

### count_entities_filtered
Count entities of given type or name in a given area. Works just like [[LuaSurface#find_entities_filtered|LuaSurface::find_entities_filtered]], except this only returns the count. As it doesn't construct all the wrapper objects, this is more efficient if one is only interested in the number of entities.

- If no `area` or `position` are given, the entire surface is searched.

- If `position` is given, this returns the entities colliding with that position (i.e the given position is within the entity's collision box).

- If `position` and `radius` are given, this returns entities in the radius of the position.

- If `area` is specified, this returns entities colliding with that area.

**Parameters:**
- **`filter`** — [[EntitySearchFilters]]

**Returns:**
- [[uint32]]

### count_tiles_filtered
Count tiles of a given name in a given area. Works just like [[LuaSurface#find_tiles_filtered|LuaSurface::find_tiles_filtered]], except this only returns the count. As it doesn't construct all the wrapper objects, this is more efficient if one is only interested in the number of tiles.

If no `area` or `position` and `radius` is given, the entire surface is searched. If `position` and `radius` are given, only tiles within the radius of the position are included.

**Parameters:**
- **`filter`** — [[TileSearchFilters]]

**Returns:**
- [[uint32]]

### find_non_colliding_position
Find a non-colliding position within a given radius.

Special care needs to be taken when using a radius of `0`. The game will not stop searching until it finds a suitable position, so it is important to make sure such a position exists. One particular case where it would not be able to find a solution is running it before any chunks have been generated.

**Parameters:**
- **`name`** — [[EntityID]]: Prototype name of the entity to find a position for. (The bounding box for the collision checking is taken from this prototype.)
- **`center`** — [[MapPosition]]: Center of the search area.
- **`radius`** — [[double]]: Max distance from `center` to search in. A radius of `0` means an infinitely-large search area.
- **`precision`** — [[double]]: The step length from the given position as it searches, in tiles. Minimum value is `0.01`.
- **`force_to_tile_center`** — [[boolean]] *(optional)*: Will only check tile centers. This can be useful when your intent is to place a building at the resulting position, as they must generally be placed at tile centers. Defaults to `false`.

**Returns:**
- [[MapPosition]] *(optional)*: The non-colliding position. May be `nil` if no suitable position was found.

### find_non_colliding_position_in_box
Find a non-colliding position within a given rectangle.

**Parameters:**
- **`name`** — [[EntityID]]: Prototype name of the entity to find a position for. (The bounding box for the collision checking is taken from this prototype.)
- **`search_space`** — [[BoundingBox]]: The rectangle to search inside.
- **`precision`** — [[double]]: The step length from the given position as it searches, in tiles. Minimum value is 0.01.
- **`force_to_tile_center`** — [[boolean]] *(optional)*: Will only check tile centers. This can be useful when your intent is to place a building at the resulting position, as they must generally be placed at tile centers. Defaults to `false`.

**Returns:**
- [[MapPosition]] *(optional)*: The non-colliding position. May be `nil` if no suitable position was found.

### spill_item_stack
Spill items on the ground centered at a given location.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: Center of the spillage
- **`stack`** — [[ItemStackIdentification]]: Stack of items to spill
- **`enable_looted`** — [[boolean]] *(optional)*: When true, each created item will be flagged with the [[LuaEntity#to_be_looted|LuaEntity::to_be_looted]] flag. Defaults to `false`.
- **`force`** — [[ForceID]] *(optional)*: When provided (and not `nil`) the items will be marked for deconstruction by this force.
- **`allow_belts`** — [[boolean]] *(optional)*: Whether items can be spilled onto belts. Defaults to `true`.
- **`max_radius`** — [[double]] *(optional)*: Max radius from the specified `position` to spill items.
- **`use_start_position_on_failure`** — [[boolean]] *(optional)*: Allow spilling items at `position` if no non-colliding position is found. Note: Setting to false might cause some items not to be spilled. Defaults to `true`.
- **`drop_full_stack`** — [[boolean]] *(optional)*: If item on ground should be made out of an entire provided stack. Defaults to `false`.

**Returns:**
- array<[[LuaEntity]]>: The created item-on-ground entities.

### spill_inventory
Spill inventory on the ground centered at a given location.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: Center of the spillage
- **`inventory`** — [[LuaInventory]]: Inventory to spill
- **`enable_looted`** — [[boolean]] *(optional)*: When true, each created item will be flagged with the [[LuaEntity#to_be_looted|LuaEntity::to_be_looted]] flag. Defaults to `false`.
- **`force`** — [[ForceID]] *(optional)*: When provided (and not `nil`) the items will be marked for deconstruction by this force.
- **`allow_belts`** — [[boolean]] *(optional)*: Whether items can be spilled onto belts. Defaults to `true`.
- **`max_radius`** — [[double]] *(optional)*: Max radius from the specified `position` to spill items.
- **`use_start_position_on_failure`** — [[boolean]] *(optional)*: Allow spilling items at `position` if no non-colliding position is found. Note: Setting to false might cause some items not to be spilled. Defaults to `true`.
- **`drop_full_stack`** — [[boolean]] *(optional)*: If item on ground should be made out of an entire provided stack. Defaults to `false`.

**Returns:**
- array<[[LuaEntity]]>: The created item-on-ground entities.

### find_enemy_units
Find enemy units (entities with type "unit") of a given force within an area.

This is more efficient than [[LuaSurface#find_entities|LuaSurface::find_entities]].

**Parameters:**
- **`center`** — [[MapPosition]]: Center of the search area
- **`radius`** — [[double]]: Radius of the circular search area
- **`force`** — [[ForceID]] *(optional)*: Force to find enemies of. If not given, uses the player force.

**Returns:**
- array<[[LuaEntity]]>

**Examples:**

```
-- Find all units who would be interested to attack the player, within 100-tile area.
local enemies = game.player.surface.find_enemy_units(game.player.position, 100)
```

### find_units
Find units (entities with type "unit") of a given force and force condition within a given area.

This is more efficient than [[LuaSurface#find_entities|LuaSurface::find_entities]].

Takes a table with the following fields:
- **`area`** — [[BoundingBox]]: Box to find units within.
- **`force`** — [[ForceID]]: Force performing the search.
- **`condition`** — [[ForceCondition]]: Only forces which meet the condition will be included in the search.

**Returns:**
- array<[[LuaEntity]]>

**Examples:**

```
-- Find friendly units to "player" force
local friendly_units = game.player.surface.find_units({area = {{-10, -10},{10, 10}}, force = "player", condition = "friend")
```

```
-- Find units of "player" force
local units = game.player.surface.find_units({area = {{-10, -10},{10, 10}}, force = "player", condition = "same"})
```

### find_nearest_enemy
Find the enemy military target ([military entity](https://wiki.factorio.com/Military_units_and_structures)) closest to the given position.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: Center of the search area.
- **`max_distance`** — [[double]]: Radius of the circular search area.
- **`force`** — [[ForceID]] *(optional)*: The force the result will be an enemy of. Uses the player force if not specified.

**Returns:**
- [[LuaEntity]] *(optional)*: The nearest enemy military target or `nil` if no enemy could be found within the given area.

### find_nearest_enemy_entity_with_owner
Find the enemy entity-with-owner closest to the given position.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: Center of the search area.
- **`max_distance`** — [[double]]: Radius of the circular search area.
- **`force`** — [[ForceID]] *(optional)*: The force the result will be an enemy of. Uses the player force if not specified.

**Returns:**
- [[LuaEntity]]: The nearest enemy entity-with-owner or `nil` if no enemy could be found within the given area.

### set_multi_command
Give a command to multiple units. This will automatically select suitable units for the task.

Takes a table with the following fields:
- **`command`** — [[Command]]
- **`unit_count`** — [[uint32]]: Number of units to give the command to.
- **`force`** — [[ForceID]] *(optional)*: Force of the units this command is to be given to. If not specified, uses the enemy force.
- **`unit_search_distance`** — [[uint32]] *(optional)*: Radius to search for units. The search area is centered on the destination of the command. If not specified uses default value of 150.

**Returns:**
- [[uint32]]: Number of units actually sent. May be less than `count` if not enough units were available.

### create_entity
Create an entity on this surface.

Takes a table with the following fields:
- **`name`** — [[EntityID]]: The entity prototype name to create.
- **`position`** — [[MapPosition]]: Where to create the entity.
- **`direction`** — [[defines.direction]] *(optional)*: Desired orientation of the entity after creation.
- **`mirror`** — [[boolean]] *(optional)*: Whether this entity is mirrored. Defaults to `false`.
- **`quality`** — [[QualityID]] *(optional)*: Quality of the entity to be created. Defaults to `normal`.
- **`force`** — [[ForceID]] *(optional)*: Force of the entity, default is enemy.
- **`target`** — [[LuaEntity]] | [[MapPosition]] *(optional)*: Entity with health for the new entity to target.
- **`source`** — [[LuaEntity]] | [[MapPosition]] *(optional)*: Source entity. Used for beams, projectiles, and highlight-boxes.
- **`cause`** — [[LuaEntity]] | [[ForceID]] *(optional)*: Cause entity / force. The entity or force that triggered the chain of events that led to this entity being created. Used for beams, projectiles, stickers, etc. so that the damage receiver can know which entity or force to retaliate against. Defaults to the value of `source`.
- **`snap_to_grid`** — [[boolean]] *(optional)*: If false the exact position given is used to instead of snapping to the normal entity grid. This only applies if the entity normally snaps to the grid.
- **`fast_replace`** — [[boolean]] *(optional)*: If true, building will attempt to simulate fast-replace building. Defaults to `false`.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. Defaults to putting it into the appropriate undo item automatically if not specified.
- **`player`** — [[PlayerIdentification]] *(optional)*: If given set the last_user to this player. If fast_replace is true simulate fast replace using this player. Also the player whose undo queue this action should be added to.
- **`character`** — [[LuaEntity]] *(optional)*: If fast_replace is true simulate fast replace using this character.
- **`spill`** — [[boolean]] *(optional)*: If false while fast_replace is true and player is nil any items from fast-replacing will be deleted instead of dropped on the ground. Defaults to `true`.
- **`raise_built`** — [[boolean]] *(optional)*: If true; [[defines.events#script_raised_built|defines.events.script_raised_built]] will be fired on successful entity creation. Defaults to `false`.
- **`create_build_effect_smoke`** — [[boolean]] *(optional)*: If false, the building effect smoke will not be shown around the new entity. Defaults to `true`.
- **`spawn_decorations`** — [[boolean]] *(optional)*: If true, entity types that have [[LuaEntityPrototype#spawn_decorations|spawn_decoration]] property will apply triggers defined in the property. Defaults to `false`.
- **`move_stuck_players`** — [[boolean]] *(optional)*: If true, any characters that are in the way of the entity are teleported out of the way.
- **`item`** — [[LuaItemStack]] *(optional)*: If provided, the entity will attempt to pull stored values from this item (for example; creating a spidertron from a previously named and mined spidertron)
- **`preserve_ghosts_and_corpses`** — [[boolean]] *(optional)*: If true, colliding ghosts and corpses will not be removed by the creation of some entity types. Defaults to `false`.
- **`register_plant`** — [[boolean]] *(optional)*: If true, plants created will register in any in-range agricultural towers.
- **`burner_fuel_inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*: Used by entities with a burner energy source.

Other attributes may be specified depending on the type of entity:

**Variant `accumulator`:**
  - **`control_behavior`** — [[AccumulatorBlueprintControlBehavior]] *(optional)*

**Variant `agricultural-tower`:**
  - **`control_behavior`** — [[AgriculturalTowerBlueprintControlBehavior]] *(optional)*

**Variant `ammo-turret`:**
  - **`priority-list`** — array<[[SlotFilter]]> *(optional)*
  - **`ignore-unprioritised`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`control_behavior`** — [[TurretBlueprintControlBehavior]] *(optional)*

**Variant `arithmetic-combinator`:**
  - **`player_description`** — [[string]] *(optional)*
  - **`control_behavior`** — [[ArithmeticCombinatorBlueprintControlBehavior]] *(optional)*

**Variant `artillery-flare`:**
  - **`movement`** — [[Vector]]
  - **`height`** — [[float]]
  - **`vertical_speed`** — [[float]]
  - **`frame_speed`** — [[float]]

**Variant `artillery-projectile`:**
  - **`speed`** — [[double]] *(optional)*: Defaults to 1.

**Variant `artillery-turret`:**
  - **`artillery_auto_targeting`** — [[boolean]] *(optional)*
  - **`control_behavior`** — [[ArtilleryTurretBlueprintControlBehavior]] *(optional)*

**Variant `artillery-wagon`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*: The orientation of this rolling stock.
  - **`color`** — [[Color]] *(optional)*: The color of this rolling stock, if it supports colors.
  - **`copy_color_from_train_stop`** — [[boolean]] *(optional)*
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, rolling stock will not connect to other rolling stocks nearby.
  - **`artillery_auto_targeting`** — [[boolean]] *(optional)*

**Variant `assembling-machine`:**
  - **`recipe`** — [[string]] *(optional)*
  - **`recipe_quality`** — [[string]] *(optional)*
  - **`control_behavior`** — [[AssemblingMachineBlueprintControlBehavior]] *(optional)*

**Variant `asteroid`:**
  - **`velocity`** — [[Vector]] *(optional)*

**Variant `asteroid-collector`:**
  - **`result-inventory`** — [[BlueprintInventory]] *(optional)*
  - **`chunk-filter`** — array<[[SlotFilter]]> *(optional)*
  - **`control_behavior`** — [[AsteroidCollectorBlueprintControlBehavior]] *(optional)*

**Variant `beam`:**
  - **`target_position`** — [[MapPosition]] *(optional)*: Absolute target position that can be used instead of target entity (entity has precedence if both entity and position are defined).
  - **`source_position`** — [[MapPosition]] *(optional)*: Absolute source position that can be used instead of source entity (entity has precedence if both entity and position are defined).
  - **`max_length`** — [[uint32]] *(optional)*: If set, beam will be destroyed when distance between source and target is greater than this value.
  - **`duration`** — [[uint32]] *(optional)*: If set, beam will be destroyed after this value of ticks.
  - **`source_offset`** — [[Vector]] *(optional)*: Source position will be offset by this value when rendering the beam.

**Variant `boiler`:**
  - **`control_behavior`** — [[BoilerBlueprintControlBehavior]] *(optional)*

**Variant `car`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`trunk_inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*
  - **`ammo_inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*
  - **`driver_is_main_gunner`** — [[boolean]] *(optional)*
  - **`selected_gun_index`** — [[ItemStackIndex]] *(optional)*
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*

**Variant `cargo-landing-pad`:**
  - **`bar`** — [[uint32]] *(optional)*
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`control_behavior`** — [[CargoLandingPadBlueprintControlBehavior]] *(optional)*

**Variant `cargo-wagon`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*: The orientation of this rolling stock.
  - **`color`** — [[Color]] *(optional)*: The color of this rolling stock, if it supports colors.
  - **`copy_color_from_train_stop`** — [[boolean]] *(optional)*
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, rolling stock will not connect to other rolling stocks nearby.
  - **`inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*

**Variant `character-corpse`:**
  - **`inventory_size`** — [[uint32]] *(optional)*
  - **`player_index`** — [[uint32]] *(optional)*
  - **`color`** — [[Color]] *(optional)*

**Variant `cliff`:**
  - **`cliff_orientation`** — [[CliffOrientation]] *(optional)*: If not specified, `direction` will be used instead.

**Variant `constant-combinator`:**
  - **`player_description`** — [[string]] *(optional)*
  - **`control_behavior`** — [[ConstantCombinatorBlueprintControlBehavior]] *(optional)*

**Variant `container`:**
  - **`filters`** — array<[[BlueprintItemFilter]]> *(optional)*
  - **`bar`** — [[ItemStackIndex]] *(optional)*: Inventory index where the red limiting bar should be set.
  - **`control_behavior`** — [[ContainerBlueprintControlBehavior]] *(optional)*

**Variant `decider-combinator`:**
  - **`player_description`** — [[string]] *(optional)*
  - **`control_behavior`** — [[DeciderCombinatorBlueprintControlBehavior]] *(optional)*

**Variant `deconstructible-tile-proxy`:**
  - **`proxy_type`** — `"cover"` | `"foundation"` *(optional)*

**Variant `display-panel`:**
  - **`text`** — [[LocalisedString]] *(optional)*
  - **`icon`** — [[SignalID]] *(optional)*
  - **`always_show`** — [[boolean]] *(optional)*
  - **`show_in_chart`** — [[boolean]] *(optional)*
  - **`control_behavior`** — [[DisplayPanelBlueprintControlBehavior]] *(optional)*

**Variant `electric-energy-interface`:**
  - **`power_production`** — [[double]] *(optional)*
  - **`power_usage`** — [[double]] *(optional)*
  - **`buffer_size`** — [[double]] *(optional)*

**Variant `electric-pole`:**
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, created electric pole will not auto connect to neighbour electric poles.

**Variant `electric-turret`:**
  - **`priority-list`** — array<[[SlotFilter]]> *(optional)*
  - **`ignore-unprioritised`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`control_behavior`** — [[TurretBlueprintControlBehavior]] *(optional)*

**Variant `entity-ghost`:**
  - **`inner_name`** — [[string]]: The prototype name of the entity contained in the ghost.
  - **`tags`** — [[Tags]] *(optional)*: The [[LuaEntity#tags|LuaEntity::tags]] associated with this entity ghost.

**Variant `fire`:**
  - **`initial_ground_flame_count`** — [[uint8]] *(optional)*: With how many small flames should the fire on ground be created. Defaults to the initial flame count of the prototype.

**Variant `fluid-turret`:**
  - **`priority-list`** — array<[[SlotFilter]]> *(optional)*
  - **`ignore-unprioritised`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`control_behavior`** — [[TurretBlueprintControlBehavior]] *(optional)*

**Variant `fluid-wagon`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*: The orientation of this rolling stock.
  - **`color`** — [[Color]] *(optional)*: The color of this rolling stock, if it supports colors.
  - **`copy_color_from_train_stop`** — [[boolean]] *(optional)*
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, rolling stock will not connect to other rolling stocks nearby.

**Variant `furnace`:**
  - **`control_behavior`** — [[FurnaceBlueprintControlBehavior]] *(optional)*

**Variant `heat-interface`:**
  - **`temperature`** — [[double]] *(optional)*
  - **`mode`** — [[HeatSettingMode]] *(optional)*

**Variant `heat-pipe`:**
  - **`control_behavior`** — [[HeatPipeBlueprintControlBehavior]] *(optional)*

**Variant `highlight-box`:**
  - **`bounding_box`** — [[BoundingBox]] *(optional)*: The bounding box defining the highlight box using absolute map coordinates. If specified, the general `position` parameter still needs to be present, but will be ignored. If not specified, the game falls back to the `source` parameter first, then the `target` parameter second. One of these three parameters need to be specified.
  - **`box_type`** — [[CursorBoxRenderType]] *(optional)*: Specifies the graphical appearance (color) of the highlight box. Defaults to `"electricity"`.
  - **`render_player_index`** — [[uint32]] *(optional)*: The player to render the highlight box for. If not provided, it will be rendered for all players.
  - **`blink_interval`** — [[uint32]] *(optional)*: The blink interval for this highlight box. Makes it be shown every `blink_interval` ticks. Defaults to `0` (constantly shown).
  - **`time_to_live`** — [[uint32]] *(optional)*: The amount of time in ticks that the highlight box will exist for. Defaults to existing forever.

**Variant `infinity-cargo-wagon`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*: The orientation of this rolling stock.
  - **`color`** — [[Color]] *(optional)*: The color of this rolling stock, if it supports colors.
  - **`copy_color_from_train_stop`** — [[boolean]] *(optional)*
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, rolling stock will not connect to other rolling stocks nearby.
  - **`inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*
  - **`infinity_settings`** — [[BlueprintInfinityInventorySettings]] *(optional)*

**Variant `infinity-container`:**
  - **`filters`** — array<[[BlueprintItemFilter]]> *(optional)*
  - **`bar`** — [[ItemStackIndex]] *(optional)*
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`infinity_settings`** — [[BlueprintInfinityInventorySettings]] *(optional)*
  - **`saved_request_from_buffers`** — [[boolean]] *(optional)*
  - **`saved_set_requests`** — [[boolean]] *(optional)*
  - **`saved_request_filters`** — [[LogisticSections]] *(optional)*
  - **`saved_storage_filters`** — [[LogisticSections]] *(optional)*
  - **`override_logistic_mode`** — [[LogisticMode]] *(optional)*
  - **`control_behavior`** — [[LogisticContainerBlueprintControlBehavior]] *(optional)*

**Variant `infinity-pipe`:**
  - **`infinity_settings`** — [[InfinityPipeFilter]] *(optional)*

**Variant `inserter`:**
  - **`filters`** — array<[[BlueprintItemFilter]]> *(optional)*
  - **`filter_mode`** — `"blacklist"` | `"whitelist"` *(optional)*
  - **`use_filters`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`drop_position`** — [[Vector]] *(optional)*: Used only if [[InserterPrototype#allow_custom_vectors|InserterPrototype::allow_custom_vectors]] is true.
  - **`pickup_position`** — [[Vector]] *(optional)*: Used only if [[InserterPrototype#allow_custom_vectors|InserterPrototype::allow_custom_vectors]] is true.
  - **`override_stack_size`** — [[uint8]] *(optional)*
  - **`spoil_priority`** — [[BlueprintSpoilPriority]] *(optional)*
  - **`control_behavior`** — [[InserterBlueprintControlBehavior]] *(optional)*

**Variant `item-entity`:**
  - **`stack`** — [[string]] | [[ItemStackDefinition]]: The stack of items to create. Either the name of an item, which will create a full stack, or a detailed item stack definition.

**Variant `item-request-proxy`:**
  - **`target`** — [[LuaEntity]]: The target items are to be delivered to.
  - **`modules`** — array<[[BlueprintInsertPlan]]> *(optional)*: Specification of items to be delivered to the target entity by the logistic network. While this is called "modules", any item can be specified.
  - **`removal_plan`** — array<[[BlueprintInsertPlan]]> *(optional)*: Specification of items to be removed from the target entity by the logistic network.

**Variant `lab`:**
  - **`control_behavior`** — [[LabBlueprintControlBehavior]] *(optional)*

**Variant `lamp`:**
  - **`color`** — [[Color]] *(optional)*: Defaults to white.
  - **`always_on`** — [[boolean]] *(optional)*: Defaults to false.
  - **`control_behavior`** — [[LampBlueprintControlBehavior]] *(optional)*

**Variant `land-mine`:**
  - **`control_behavior`** — [[LandMineBlueprintControlBehavior]] *(optional)*

**Variant `lane-splitter`:**
  - **`filter`** — [[ItemFilter]] *(optional)*
  - **`input_priority`** — [[SplitterPriority]] *(optional)*
  - **`output_priority`** — [[SplitterPriority]] *(optional)*

**Variant `linked-belt`:**
  - **`type`** — [[BeltConnectionType]] *(optional)*

**Variant `linked-container`:**
  - **`link_id`** — [[uint32]] *(optional)*

**Variant `loader`:**
  - **`type`** — [[BeltConnectionType]] *(optional)*: Defaults to `"input"`.
  - **`filters`** — array<[[SlotFilter]]> *(optional)*
  - **`filter_mode`** — [[PrototypeFilterMode]] *(optional)*
  - **`belt_stack_size_override`** — [[uint8]] *(optional)*
  - **`control_behavior`** — [[LoaderBlueprintControlBehavior]] *(optional)*

**Variant `loader-1x1`:**
  - **`type`** — [[BeltConnectionType]] *(optional)*: Defaults to `"input"`.
  - **`filters`** — array<[[SlotFilter]]> *(optional)*
  - **`filter_mode`** — [[PrototypeFilterMode]] *(optional)*
  - **`belt_stack_size_override`** — [[uint8]] *(optional)*
  - **`control_behavior`** — [[LoaderBlueprintControlBehavior]] *(optional)*

**Variant `locomotive`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`orientation`** — [[RealOrientation]] *(optional)*: The orientation of this rolling stock.
  - **`color`** — [[Color]] *(optional)*: The color of this rolling stock, if it supports colors.
  - **`copy_color_from_train_stop`** — [[boolean]] *(optional)*
  - **`auto_connect`** — [[boolean]] *(optional)*: True by default. If set to false, rolling stock will not connect to other rolling stocks nearby.
  - **`snap_to_train_stop`** — [[boolean]] *(optional)*: Whether the locomotive should snap to an adjacent train stop. Defaults to true.

**Variant `logistic-container`:**
  - **`filters`** — array<[[BlueprintItemFilter]]> *(optional)*
  - **`bar`** — [[ItemStackIndex]] *(optional)*
  - **`request_filters`** — array<[[SlotFilter]]> *(optional)*
  - **`control_behavior`** — [[LogisticContainerBlueprintControlBehavior]] *(optional)*

**Variant `mining-drill`:**
  - **`filter`** — [[BlueprintMiningDrillFilter]] *(optional)*
  - **`control_behavior`** — [[MiningDrillBlueprintControlBehavior]] *(optional)*

**Variant `offshore-pump`:**
  - **`control_behavior`** — [[GenericOnOffBlueprintControlBehavior]] *(optional)*

**Variant `particle`:**
  - **`movement`** — [[Vector]]
  - **`height`** — [[float]]
  - **`vertical_speed`** — [[float]]
  - **`frame_speed`** — [[float]]

**Variant `pipe`:**
  - **`control_behavior`** — [[SingleFluidBoxBlueprintControlBehavior]] *(optional)*

**Variant `pipe-to-ground`:**
  - **`control_behavior`** — [[SingleFluidBoxBlueprintControlBehavior]] *(optional)*

**Variant `plant`:**
  - **`tick_grown`** — [[MapTick]] *(optional)*: The tick the plant will be fully grown. If not specified, the plants normal growth time is used.

**Variant `power-switch`:**
  - **`switch_state`** — [[boolean]] *(optional)*
  - **`control_behavior`** — [[GenericOnOffBlueprintControlBehavior]] *(optional)*

**Variant `programmable-speaker`:**
  - **`parameters`** — [[ProgrammableSpeakerParameters]] *(optional)*
  - **`alert_parameters`** — [[ProgrammableSpeakerAlertParameters]] *(optional)*
  - **`control_behavior`** — [[ProgrammableSpeakerBlueprintControlBehavior]] *(optional)*

**Variant `projectile`:**
  - **`speed`** — [[double]] *(optional)*: Defaults to 0.
  - **`max_range`** — [[double]] *(optional)*: Defaults to 1000.
  - **`base_damage_modifiers`** — [[TriggerModifierData]] *(optional)*
  - **`bonus_damage_modifiers`** — [[TriggerModifierData]] *(optional)*

**Variant `proxy-container`:**
  - **`control_behavior`** — [[ProxyContainerBlueprintControlBehavior]] *(optional)*

**Variant `pump`:**
  - **`fluid_filter`** — [[string]] *(optional)*
  - **`control_behavior`** — [[PumpBlueprintControlBehavior]] *(optional)*

**Variant `radar`:**
  - **`control_behavior`** — [[RadarBlueprintControlBehavior]] *(optional)*

**Variant `rail-chain-signal`:**
  - **`rail_layer`** — [[defines.rail_layer]] *(optional)*: Defaults to [[defines.rail_layer#ground|defines.rail_layer.ground]].
  - **`control_behavior`** — [[RailSignalBaseBlueprintControlBehavior]] *(optional)*

**Variant `rail-signal`:**
  - **`rail_layer`** — [[defines.rail_layer]] *(optional)*: Defaults to [[defines.rail_layer#ground|defines.rail_layer.ground]].
  - **`control_behavior`** — [[RailSignalBaseBlueprintControlBehavior]] *(optional)*

**Variant `reactor`:**
  - **`control_behavior`** — [[ReactorBlueprintControlBehavior]] *(optional)*

**Variant `resource`:**
  - **`amount`** — [[uint32]] *(optional)*
  - **`enable_tree_removal`** — [[boolean]] *(optional)*: If colliding trees are removed normally for this resource entity based off the prototype tree removal values. Default is true.
  - **`enable_cliff_removal`** — [[boolean]] *(optional)*: If colliding cliffs are removed. Default is true.
  - **`snap_to_tile_center`** — [[boolean]] *(optional)*: If true, the resource entity will be placed to center of a tile as map generator would place it, otherwise standard non-resource grid alignment rules will apply. Default is true.

**Variant `roboport`:**
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`control_behavior`** — [[RoboportBlueprintControlBehavior]] *(optional)*

**Variant `rocket-silo`:**
  - **`recipe`** — [[string]] *(optional)*
  - **`recipe_quality`** — [[string]] *(optional)*
  - **`use_transitional_requests`** — [[boolean]] *(optional)*
  - **`launch_to_orbit_automatically`** — [[boolean]] *(optional)*
  - **`control_behavior`** — [[RocketSiloBlueprintControlBehavior]] *(optional)*

**Variant `selector-combinator`:**
  - **`player_description`** — [[string]] *(optional)*
  - **`control_behavior`** — [[SelectorCombinatorParameters]] *(optional)*

**Variant `simple-entity-with-force`:**
  - **`render_player_index`** — [[uint32]] *(optional)*
  - **`color`** — [[Color]] *(optional)*
  - **`variation`** — [[uint8]] *(optional)*

**Variant `simple-entity-with-owner`:**
  - **`render_player_index`** — [[uint32]] *(optional)*
  - **`color`** — [[Color]] *(optional)*
  - **`variation`** — [[uint8]] *(optional)*

**Variant `space-platform-hub`:**
  - **`bar`** — [[ItemStackIndex]] *(optional)*
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`request_missing_construction_materials`** — [[boolean]] *(optional)*
  - **`control_behavior`** — [[SpacePlatformHubBlueprintControlBehavior]] *(optional)*
  - **`providing_to_other_platforms`** — [[boolean]] *(optional)*

**Variant `speech-bubble`:**
  - **`text`** — [[LocalisedString]]
  - **`lifetime`** — [[uint32]] *(optional)*

**Variant `spider-vehicle`:**
  - **`enable_logistics_while_moving`** — [[boolean]] *(optional)*
  - **`grid`** — array<[[BlueprintEquipment]]> *(optional)*
  - **`trunk_inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*
  - **`ammo_inventory`** — [[BlueprintInventoryWithFilters]] *(optional)*
  - **`driver_is_main_gunner`** — [[boolean]] *(optional)*
  - **`automatic_targeting_parameters`** — [[VehicleAutomaticTargetingParameters]] *(optional)*
  - **`selected_gun_index`** — [[ItemStackIndex]] *(optional)*
  - **`request_filters`** — [[BlueprintLogisticSections]] *(optional)*
  - **`color`** — [[Color]] *(optional)*
  - **`label`** — [[string]] *(optional)*

**Variant `splitter`:**
  - **`filter`** — [[ItemFilter]] *(optional)*
  - **`input_priority`** — [[SplitterPriority]] *(optional)*
  - **`output_priority`** — [[SplitterPriority]] *(optional)*
  - **`control_behavior`** — [[SplitterBlueprintControlBehavior]] *(optional)*

**Variant `storage-tank`:**
  - **`control_behavior`** — [[SingleFluidBoxBlueprintControlBehavior]] *(optional)*

**Variant `stream`:**
  - **`target_position`** — [[MapPosition]] *(optional)*: Absolute target position that can be used instead of target entity (entity has precedence if both entity and position are defined).
  - **`source_position`** — [[MapPosition]] *(optional)*: Absolute source position that can be used instead of source entity (entity has precedence if both entity and position are defined).

**Variant `tile-ghost`:**
  - **`inner_name`** — [[string]]: The prototype name of the tile contained in the ghost.

**Variant `train-stop`:**
  - **`color`** — [[Color]] *(optional)*
  - **`station`** — [[string]] *(optional)*
  - **`manual_trains_limit`** — [[uint32]] *(optional)*
  - **`priority`** — [[uint8]] *(optional)*
  - **`control_behavior`** — [[TrainStopBlueprintControlBehavior]] *(optional)*

**Variant `transport-belt`:**
  - **`control_behavior`** — [[TransportBeltBlueprintControlBehavior]] *(optional)*

**Variant `turret`:**
  - **`priority-list`** — array<[[SlotFilter]]> *(optional)*
  - **`ignore-unprioritised`** — [[boolean]] *(optional)*: Defaults to `false`.
  - **`control_behavior`** — [[TurretBlueprintControlBehavior]] *(optional)*

**Variant `underground-belt`:**
  - **`type`** — [[BeltConnectionType]] *(optional)*: Defaults to `"input"`.

**Variant `valve`:**
  - **`valve_threshold_override`** — [[float]] *(optional)*

**Variant `wall`:**
  - **`control_behavior`** — [[WallBlueprintControlBehavior]] *(optional)*

**Returns:**
- [[LuaEntity]] *(optional)*: The created entity or `nil` if the creation failed.

**Raises:**
- [[script_raised_built]] *(timeframe: instantly)*: Raised if the `raise_built` flag was set and the entity was successfully created.

**Examples:**

```
local asm = game.surfaces[1].create_entity{name = "assembling-machine-1", position = {15, 3}, force = game.forces.player, recipe = "iron-stick"}
```

```
-- Creates a filter inserter with circuit conditions and a filter
game.surfaces[1].create_entity{
  name = "filter-inserter", position = {20, 15}, force = game.player.force,
  conditions =
  {
    red = {name = "wood", count = 3, operator = ">"},
    green = {name = "iron-ore", count = 1, operator = "<"},
    logistics = {name = "wood", count = 3, operator = "="}
  },
  filters = {{index = 1, name = "iron-ore"}}
}
```

```
-- Creates a requester chest already set to request 128 iron plates.
game.surfaces[1].create_entity{
  name = "requester-chest", position = {game.player.position.x+3, game.player.position.y},
  force = game.player.force, request_filters = {{index = 1, name = "iron-plate", count = 128}}
}
```

```
game.surfaces[1].create_entity{name = "big-biter", position = {15, 3}, force = game.forces.player} -- Friendly biter
game.surfaces[1].create_entity{name = "medium-biter", position = {15, 3}, force = game.forces.enemy} -- Enemy biter
```

```
-- Creates a basic inserter at the player's location facing north
game.surfaces[1].create_entity{name = "inserter", position = game.player.position, direction = defines.direction.north}
```

### create_segmented_unit
Create a segmented unit on the surface. This differs from creating an entity with type `"segmented-unit"` in that this method can create the entity in non-generated chunks and with any arbitrary body shape and pre-assigned to a territory.

Takes a table with the following fields:
- **`name`** — [[EntityID]]: The segmented-unit prototype name to create. Must be of type `"segmented-unit"`.
- **`quality`** — [[QualityID]] *(optional)*: Quality of the entity to be created. Defaults to `normal`.
- **`force`** — [[ForceID]] *(optional)*: Force of the segmented unit. Defaults to `enemy`.
- **`territory`** — [[LuaTerritory]] *(optional)*: The territory that the segmented unit is assigned to. If `nil`, the segmented unit will patrol around its spawn location. Must be located on this same surface.

These attributes provide different methods of specifying the unit's spawn location:

**Variant `body-nodes`:**
  - **`body_nodes`** — array<[[MapPosition]]>: The body nodes that define the shape of the body. The array must contain at least one value and should have no more than [[SegmentEngineSpecification (type)#max_body_nodes|SegmentEngineSpecification::max_body_nodes]]. The nodes should be about 1 tile apart from each other, but it is not strictly required.

**Variant `position-and-direction`:**
  - **`position`** — [[MapPosition]]: The head position.
  - **`direction`** — [[defines.direction]] *(optional)*: The initial orientation of the head. Defaults to `defines.direction.north`.
  - **`extended`** — [[boolean]] *(optional)*: If `true`, will create the segmented unit so that the entire body is stretches in a straight line behind the head. If `false`, then only the head segment will be created and the remainder of the body segments will be created over time as the head moves forward. Defaults to `false`.

**Returns:**
- [[LuaSegmentedUnit]] *(optional)*: The created segmented unit or `nil` if the creation failed or the unit was destroyed during creation.

**Raises:**
- [[on_segmented_unit_created]] *(timeframe: instantly)*: Raised if the segmented unit was successfully created. [[on_segmented_unit_created|cause]] will be set to [[defines.segmented_unit_created_cause|script_created]].

### create_territory
Create a territory on the surface.

Takes a table with the following fields:
- **`chunks`** — array<[[ChunkPosition]]>: The chunks to assign to the new territory. Must contain at least one generated chunk. Any chunks already assigned to existing territories will be removed from those territories. Any territories left with no generated chunks will be deleted from the surface as a result.
- **`patrol_path`** — array<[[MapPosition]]> *(optional)*: The path that patrolling units will follow. If `nil` or empty, one will be generated for the new territory based on `chunks`.

**Returns:**
- [[LuaTerritory]] *(optional)*: The created territory or `nil` if the creation failed or the territory was destroyed during creation.

**Raises:**
- [[on_territory_created]] *(timeframe: instantly)*: Raised if the territory was successfully created.

### create_trivial_smoke

Takes a table with the following fields:
- **`name`** — [[TrivialSmokeID]]: The smoke prototype name to create.
- **`position`** — [[MapPosition]]: Where to create the smoke.

### create_particle
Creates a particle at the given location

Takes a table with the following fields:
- **`name`** — [[ParticleID]]: The particle name.
- **`position`** — [[MapPosition]]: Where to create the particle.
- **`movement`** — [[Vector]]
- **`height`** — [[float]]
- **`vertical_speed`** — [[float]]
- **`frame_speed`** — [[float]]

### create_unit_group
Create a new unit group at a given position.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: Initial position of the new unit group.
- **`force`** — [[ForceID]] *(optional)*: Force of the new unit group. Defaults to `"enemy"`.

**Returns:**
- [[LuaCommandable]]

**Raises:**
- [[on_unit_group_created]] *(timeframe: instantly)*

### build_enemy_base
Send a group to build a new base.

The specified force must be AI-controlled; i.e. `force.ai_controllable` must be `true`.

**Parameters:**
- **`position`** — [[MapPosition]]: Location of the new base.
- **`unit_count`** — [[uint32]]: Number of biters to send for the base-building task.
- **`force`** — [[ForceID]] *(optional)*: Force the new base will belong to. Defaults to enemy.

### get_tile
Get the tile at a given position. An alternative call signature for this method is passing it a single [[TilePosition]].

Non-integer values will result in them being rounded down.

**Parameters:**
- **`x`** — [[int32]]
- **`y`** — [[int32]]

**Returns:**
- [[LuaTile]]

### set_tiles
Set tiles at specified locations. Can automatically correct the edges around modified tiles.

Placing a [[LuaTilePrototype#mineable_properties|mineable]] tile on top of a non-mineable or [[LuaTilePrototype#is_foundation|foundation]] one will turn the latter into the [[LuaTile#hidden_tile|LuaTile::hidden_tile]] for that tile. Placing a mineable non-foundation tile on a mineable non-foundation one or a mineable foundation tile on a mineable foundation one will not modify the hidden tile. This restriction can however be circumvented by using [[LuaSurface#set_hidden_tile|LuaSurface::set_hidden_tile]]. Placing a non-foundation tile on top of a foundation one when there already exists a hidden tile will push hidden tile to [[LuaTile#double_hidden_tile|double hidden]], and foundation tile will turn into hidden. Placing a mineable foundation tile over a mineable non-foundation tile with hidden mineable foundation tile, the hidden tile will be replaced by previously double hidden tile and double hidden tile will be erased. Placing a non-mineable tile will erase hidden and double hidden tiles.

It is recommended to call this method once for all the tiles you want to change rather than calling it individually for every tile. As the tile correction is used after every step, calling it one by one could cause the tile correction logic to redo some of the changes. Also, many small API calls are generally more performance intensive than one big one.

**Parameters:**
- **`tiles`** — array<[[Tile]]>
- **`correct_tiles`** — [[boolean]] *(optional)*: If `false`, the correction logic is not applied to the changed tiles. Defaults to `true`.
- **`remove_colliding_entities`** — [[boolean]] | `"abort_on_collision"` *(optional)*: Defaults to `true`.
- **`remove_colliding_decoratives`** — [[boolean]] *(optional)*: Defaults to `true`.
- **`raise_event`** — [[boolean]] *(optional)*: Defaults to `false`.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player whose undo queue to add these actions to.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. Defaults to putting it into the appropriate undo item automatically if not specified.

**Raises:**
- [[script_raised_set_tiles]] *(timeframe: instantly)*: Raised if the `raise_event` flag was set.

### pollute
Spawn pollution at the given position.

**Parameters:**
- **`source`** — [[MapPosition]]: Where to spawn the pollution.
- **`amount`** — [[double]]: How much pollution to add.
- **`prototype`** — [[EntityID]] *(optional)*: The entity prototype to attribute the pollution change to in statistics. If not defined, the pollution change will not show up in statistics.

### get_chunks
Get an iterator going over every chunk on this surface.

Chunks may or may not be generated; use [[LuaSurface#is_chunk_generated|LuaSurface::is_chunk_generated]] to check a chunk's state before accessing it.

**Returns:**
- [[LuaChunkIterator]]

### is_chunk_generated
Is a given chunk generated?

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk's position.

**Returns:**
- [[boolean]]

### request_to_generate_chunks
Request that the game's map generator generate chunks at the given position for the given radius on this surface. If the radius is `0`, then only the chunk at the given position is generated.

**Parameters:**
- **`position`** — [[MapPosition]]: Where to generate the new chunks.
- **`radius`** — [[uint32]] *(optional)*: The chunk radius from `position` to generate new chunks in. Defaults to `0`.

### force_generate_chunk_requests
Blocks and generates all chunks that have been requested using all available threads.

### set_chunk_generated_status
Set generated status of a chunk. Useful when copying chunks.

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk's position.
- **`status`** — [[defines.chunk_generated_status]]: The chunk's new status.

### get_territories
Get all territories on the surface.

**Returns:**
- array<[[LuaTerritory]]>

### get_territory_for_chunk
Get the territory that the given chunk is assigned to. If the chunk is not part of any territory or the territory for the chunk has not yet been generated, then this returns `nil`.

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk's position. The chunk at this position does not need to exist.

**Returns:**
- [[LuaTerritory]] *(optional)*

### set_territory_for_chunks
Removes the given chunks from their current territories and adds them to the given territory if provided.

This does not affect the [[LuaTerritory#get_patrol_path|LuaTerritory::get_patrol_path]]. It is your responsibility to update the patrol path if needed.

It's recommended that territory chunks are connected to each other, but this is not required.

Territories that do not contain at least one generated chunk as a result of calling this method will be automatically deleted.

**Parameters:**
- **`chunk_positions`** — array<[[ChunkPosition]]>: The chunk positions. The chunks at these positions do not need to exist in order to be assigned to a territory.
- **`territory`** — [[LuaTerritory]] *(optional)*: The territory to associate the chunks with. If not `nil`, the territory must belong to this same surface or else an error will be produced. If `nil`, then the chunks get removed from the territory it is currently associated with and will prevent the map generator from automatically re-generate a new territory for the chunk in the future.

**Raises:**
- [[on_territory_destroyed]] *(timeframe: instantly)*: Raised for each territory that is destroyed as a result of calling this method.

### clear_territory_for_chunks
Removes the chunk from the territory it is associated with (if any) and allows the map generator to potentially generate a new territory for the chunk in the future. To prevent the game from generating a new territory for the chunk, use [[LuaSurface#set_chunk_territory|LuaSurface::set_chunk_territory]] to set the chunk's territory to `nil`.

Territories that do not contain at least one generated chunk as a result of calling this method will be automatically deleted.

**Parameters:**
- **`chunk_positions`** — array<[[ChunkPosition]]>: The chunk positions. The chunks at these positions does not need to exist.

### get_segmented_units
Get all segmented units that exist on the surface.

**Returns:**
- array<[[LuaSegmentedUnit]]>

### find_logistic_network_by_position
Find the logistic network that covers a given position.

**Parameters:**
- **`position`** — [[MapPosition]]
- **`force`** — [[ForceID]]: Force the logistic network should belong to.

**Returns:**
- [[LuaLogisticNetwork]] *(optional)*: The found network or `nil` if no such network was found.

### find_closest_logistic_network_by_position
Find the logistic network with a cell closest to a given position.

**Parameters:**
- **`position`** — [[MapPosition]]
- **`force`** — [[ForceID]]: Force the logistic network should belong to.

**Returns:**
- [[LuaLogisticNetwork]] *(optional)*: The found network or `nil` if no such network was found.

### find_logistic_networks_by_construction_area
Finds all of the logistics networks whose construction area intersects with the given position.

**Parameters:**
- **`position`** — [[MapPosition]]
- **`force`** — [[ForceID]]: Force the logistic networks should belong to.

**Returns:**
- array<[[LuaLogisticNetwork]]>

### deconstruct_area
Place a deconstruction request.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]]: The area to mark for deconstruction.
- **`force`** — [[ForceID]]: The force whose bots should perform the deconstruction.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`item`** — [[LuaItemStack]] *(optional)*: The deconstruction item to use if any.
- **`super_forced`** — [[boolean]] *(optional)*: If the deconstruction is super-forced. Defaults to `false`.

**Raises:**
- [[on_marked_for_deconstruction]] *(timeframe: instantly)*: Raised for every entity that has been successfully marked for deconstruction.

### cancel_deconstruct_area
Cancel a deconstruction order.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]]: The area to cancel deconstruction orders in.
- **`force`** — [[ForceID]]: The force whose deconstruction orders to cancel.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to, if any. Also the player whose undo queue this action should be added to.
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped. Defaults to `false`.
- **`item`** — [[LuaItemStack]] *(optional)*: The deconstruction item to use if any.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. Defaults to putting it into the appropriate undo item automatically if not specified.
- **`super_forced`** — [[boolean]] *(optional)*: If the cancel deconstruction is super-forced. Defaults to `false`.

**Raises:**
- [[on_cancelled_deconstruction]] *(timeframe: instantly)*: Raised for every entity whose deconstruction has been successfully cancelled.

### upgrade_area
Place an upgrade request.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]]: The area to mark for upgrade.
- **`force`** — [[ForceID]]: The force whose bots should perform the upgrade.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped.
- **`item`** — [[LuaItemStack]]: The upgrade item to use.

**Raises:**
- [[on_marked_for_upgrade]] *(timeframe: instantly)*: Raised for every entity that has been successfully marked for upgrade.

### cancel_upgrade_area
Cancel a upgrade order.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]]: The area to cancel upgrade orders in.
- **`force`** — [[ForceID]]: The force whose upgrade orders to cancel.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.
- **`skip_fog_of_war`** — [[boolean]] *(optional)*: If chunks covered by fog-of-war are skipped.
- **`item`** — [[LuaItemStack]]: The upgrade item to use.

**Raises:**
- [[on_cancelled_upgrade]] *(timeframe: instantly)*: Raised for every entity whose upgrade has been successfully cancelled.

### get_hidden_tile
The hidden tile name.

**Parameters:**
- **`position`** — [[TilePosition]]: The tile position.

**Returns:**
- [[string]] *(optional)*: `nil` if there isn't one for the given position.

### get_double_hidden_tile
The double hidden tile name or `nil` if there isn't one for the given position.

**Parameters:**
- **`position`** — [[TilePosition]]: The tile position.

**Returns:**
- [[string]]

### set_hidden_tile
Set the hidden tile for the specified position. While during normal gameplay only [[LuaTilePrototype#mineable_properties|non-mineable]] or [[LuaTilePrototype#is_foundation|foundation]] tiles can become hidden, this method allows any kind of tile to be set as the hidden one.

**Parameters:**
- **`position`** — [[TilePosition]]: The tile position.
- **`tile`** — [[TileID]] *(optional)*: The new hidden tile or `nil` to clear the hidden tile.

### set_double_hidden_tile
Set double hidden tile for the specified position. During normal gameplay, only [[LuaTilePrototype#mineable_properties|non-mineable]] tiles can become double hidden.

Does nothing if hidden tile at specified position does not exist.

**Parameters:**
- **`position`** — [[TilePosition]]: The tile position.
- **`tile`** — [[TileID]] *(optional)*: The new double hidden tile or `nil` to clear the double hidden tile.

### get_connected_tiles
Gets all tiles of the given types that are connected horizontally or vertically to the given tile position including the given tile position.

This won't find tiles in non-generated chunks.

**Parameters:**
- **`position`** — [[TilePosition]]: The tile position to start at.
- **`tiles`** — array<[[TileID]]>: The tiles to search for.
- **`include_diagonal`** — [[boolean]] *(optional)*: Include tiles that are connected diagonally.
- **`area`** — [[BoundingBox]] *(optional)*: The area to find connected tiles in. If provided the start position must be in this area.

**Returns:**
- array<[[TilePosition]]>: The resulting set of tiles.

### delete_chunk

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk position to delete

**Raises:**
- [[on_chunk_deleted]] *(timeframe: future_tick)*
- [[on_pre_chunk_deleted]] *(timeframe: future_tick)*
- [[on_territory_destroyed]] *(timeframe: future_tick)*: Raised if a territory is automatically destroyed as a result of deleting the chunk.

### regenerate_entity
Regenerate autoplacement of some entities on this surface. This can be used to autoplace newly-added entities.

All specified entity prototypes must be autoplacable. If nothing is given all entities are generated on all chunks.

**Parameters:**
- **`entities`** — [[string]] | array<[[string]]> *(optional)*: Prototype names of entity or entities to autoplace. When `nil` all entities with an autoplace are used.
- **`chunks`** — array<[[ChunkPosition]]> *(optional)*: The chunk positions to regenerate the entities on. If not given all chunks are regenerated. Note chunks with status < entities are ignored.

### regenerate_decorative
Regenerate autoplacement of some decoratives on this surface. This can be used to autoplace newly-added decoratives.

All specified decorative prototypes must be autoplacable. If nothing is given all decoratives are generated on all chunks.

**Parameters:**
- **`decoratives`** — [[string]] | array<[[string]]> *(optional)*: Prototype names of decorative or decoratives to autoplace. When `nil` all decoratives with an autoplace are used.
- **`chunks`** — array<[[ChunkPosition]]> *(optional)*: The chunk positions to regenerate the decoratives on. If not given all chunks are regenerated. Note chunks with status < entities are ignored.

### print
Print text to the chat console of all players on this surface.

By default, messages that are identical to a message sent in the last 60 ticks are not printed again.

**Parameters:**
- **`message`** — [[LocalisedString]]
- **`print_settings`** — [[PrintSettings]] *(optional)*

### destroy_decoratives
Removes all decoratives from the given area. If no area and no position are given, then the entire surface is searched.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]] *(optional)*
- **`position`** — [[TilePosition]] *(optional)*
- **`name`** — [[DecorativeID]] | array<[[DecorativeID]]> *(optional)*
- **`collision_mask`** — [[CollisionLayerID]] | array<[[CollisionLayerID]]> | dictionary<[[CollisionLayerID]] → `true`> *(optional)*
- **`from_layer`** — [[string]] *(optional)*
- **`to_layer`** — [[string]] *(optional)*
- **`exclude_soft`** — [[boolean]] *(optional)*: Soft decoratives can be drawn over rails.
- **`limit`** — [[uint32]] *(optional)*
- **`invert`** — [[boolean]] *(optional)*: If the filters should be inverted.

### create_decoratives
Adds the given decoratives to the surface.

This will merge decoratives of the same type that already exist effectively increasing the "amount" field.

Takes a table with the following fields:
- **`check_collision`** — [[boolean]] *(optional)*: If collision should be checked against entities/tiles.
- **`decoratives`** — array<[[Decorative]]>

### find_decoratives_filtered
Find decoratives of a given name in a given area.

If no filters are given, returns all decoratives in the search area. If multiple filters are specified, returns only decoratives matching every given filter. If no area and no position are given, the entire surface is searched.

Takes a table with the following fields:
- **`area`** — [[BoundingBox]] *(optional)*
- **`position`** — [[TilePosition]] *(optional)*
- **`name`** — [[DecorativeID]] | array<[[DecorativeID]]> *(optional)*
- **`collision_mask`** — [[CollisionLayerID]] | array<[[CollisionLayerID]]> | dictionary<[[CollisionLayerID]] → `true`> *(optional)*
- **`from_layer`** — [[string]] *(optional)*
- **`to_layer`** — [[string]] *(optional)*
- **`exclude_soft`** — [[boolean]] *(optional)*: Soft decoratives can be drawn over rails.
- **`limit`** — [[uint32]] *(optional)*
- **`invert`** — [[boolean]] *(optional)*: If the filters should be inverted.

**Returns:**
- array<[[DecorativeResult]]>

**Examples:**

```
game.surfaces[1].find_decoratives_filtered{area = {{-10, -10}, {10, 10}}, name = "sand-decal"} -- gets all sand-decals in the rectangle
game.surfaces[1].find_decoratives_filtered{area = {{-10, -10}, {10, 10}}, limit = 5}  -- gets the first 5 decoratives in the rectangle
```

### clear_pollution
Clears all pollution on this surface.

### play_sound
Play a sound for every player on this surface.

The sound is not played if its location is not [[LuaForce#chart|charted]] for that player.

**Parameters:**
- **`sound_specification`** — [[PlaySoundSpecification]]: The sound to play.

### play_music
Play a music track for every player on this surface.

**Parameters:**
- **`music_specification`** — [[PlayMusicSpecification]]: The track to play.

### get_resource_counts
Gets the resource amount of all resources on this surface

**Returns:**
- dictionary<[[string]] → [[uint32]]>

### get_random_chunk
Gets a random generated chunk position or nil if no chunks have been generated on this surface.

**Returns:**
- [[ChunkPosition]] *(optional)*

### clone_area
Clones the given area.

Entities are cloned in an order such that they can always be created, eg rails before trains.

Takes a table with the following fields:
- **`source_area`** — [[BoundingBox]]
- **`destination_area`** — [[BoundingBox]]
- **`destination_surface`** — [[SurfaceIdentification]] *(optional)*
- **`destination_force`** — [[ForceID]] *(optional)*
- **`clone_tiles`** — [[boolean]] *(optional)*: If tiles should be cloned
- **`clone_entities`** — [[boolean]] *(optional)*: If entities should be cloned
- **`clone_decoratives`** — [[boolean]] *(optional)*: If decoratives should be cloned
- **`clear_destination_entities`** — [[boolean]] *(optional)*: If the destination entities should be cleared
- **`clear_destination_decoratives`** — [[boolean]] *(optional)*: If the destination decoratives should be cleared
- **`expand_map`** — [[boolean]] *(optional)*: If the destination surface should be expanded when destination_area is outside current bounds. Defaults to `false`.
- **`create_build_effect_smoke`** — [[boolean]] *(optional)*: If true, the building effect smoke will be shown around the new entities. Defaults to `false`.

**Raises:**
- [[on_area_cloned]] *(timeframe: instantly)*: Raised after the individual `on_entity_cloned` events.
- [[on_entity_cloned]] *(timeframe: instantly)*: Raised for every entity that was cloned.

### clone_brush
Clones the given area.

[[defines.events#on_entity_cloned|defines.events.on_entity_cloned]] is raised for each entity, and then [[defines.events#on_area_cloned|defines.events.on_area_cloned]] is raised.

Entities are cloned in an order such that they can always be created, eg rails before trains.

Takes a table with the following fields:
- **`source_offset`** — [[TilePosition]]
- **`destination_offset`** — [[TilePosition]]
- **`source_positions`** — array<[[TilePosition]]>
- **`destination_surface`** — [[SurfaceIdentification]] *(optional)*
- **`destination_force`** — [[LuaForce]] | [[string]] *(optional)*
- **`clone_tiles`** — [[boolean]] *(optional)*: If tiles should be cloned
- **`clone_entities`** — [[boolean]] *(optional)*: If entities should be cloned
- **`clone_decoratives`** — [[boolean]] *(optional)*: If decoratives should be cloned
- **`clear_destination_entities`** — [[boolean]] *(optional)*: If the destination entities should be cleared
- **`clear_destination_decoratives`** — [[boolean]] *(optional)*: If the destination decoratives should be cleared
- **`expand_map`** — [[boolean]] *(optional)*: If the destination surface should be expanded when destination_area is outside current bounds. Defaults to `false`.
- **`manual_collision_mode`** — [[boolean]] *(optional)*: If manual-style collision checks should be done.
- **`create_build_effect_smoke`** — [[boolean]] *(optional)*: If true, the building effect smoke will be shown around the new entities.

### clone_entities
Clones the given entities.

Entities are cloned in an order such that they can always be created, eg rails before trains.

Takes a table with the following fields:
- **`entities`** — array<[[LuaEntity]]>
- **`destination_offset`** — [[Vector]]
- **`destination_surface`** — [[SurfaceIdentification]] *(optional)*
- **`destination_force`** — [[ForceID]] *(optional)*
- **`snap_to_grid`** — [[boolean]] *(optional)*
- **`create_build_effect_smoke`** — [[boolean]] *(optional)*: If true, the building effect smoke will be shown around the new entities.

**Raises:**
- [[on_entity_cloned]] *(timeframe: instantly)*: Raised for every entity that was cloned.

### clear
Clears this surface deleting all entities and chunks on it.

**Parameters:**
- **`ignore_characters`** — [[boolean]] *(optional)*: Whether characters on this surface that are connected to or associated with players should be ignored (not destroyed). Defaults to `false`.

**Raises:**
- [[on_pre_surface_cleared]] *(timeframe: future_tick)*
- [[on_surface_cleared]] *(timeframe: future_tick)*

### request_path
Generates a path with the specified constraints (as an array of [[PathfinderWaypoint|PathfinderWaypoints]]) using the unit pathfinding algorithm. This path can be used to emulate pathing behavior by script for non-unit entities, such as vehicles. If you want to command actual units (such as biters or spitters) to move, use [[LuaCommandable#set_command|LuaCommandable::set_command]] via [[LuaEntity#commandable|LuaEntity::commandable]] instead.

The resulting path is ultimately returned asynchronously via [[on_script_path_request_finished]].

Takes a table with the following fields:
- **`bounding_box`** — [[BoundingBox]]: The dimensions of the object that's supposed to travel the path.
- **`collision_mask`** — [[CollisionMask]]: The collision mask the `bounding_box` collides with.
- **`start`** — [[MapPosition]]: The position from which to start pathfinding.
- **`goal`** — [[MapPosition]]: The position to find a path to.
- **`force`** — [[ForceID]]: The force for which to generate the path, determining which gates can be opened for example.
- **`radius`** — [[double]] *(optional)*: How close the pathfinder needs to get to its `goal` (in tiles). Defaults to `1`.
- **`pathfind_flags`** — [[PathfinderFlags]] *(optional)*: Flags that affect pathfinder behavior.
- **`can_open_gates`** — [[boolean]] *(optional)*: Whether the path request can open gates. Defaults to `false`.
- **`path_resolution_modifier`** — [[int32]] *(optional)*: Defines how coarse the pathfinder's grid is, where smaller values mean a coarser grid. Defaults to `0`, which equals a resolution of `1x1` tiles, centered on tile centers. Values range from `-8` to `8` inclusive, where each integer increment doubles/halves the resolution. So, a resolution of `-8` equals a grid of `256x256` tiles, and a resolution of `8` equals `1/256` of a tile.
- **`max_gap_size`** — [[int32]] *(optional)*: Defines the maximum allowed distance between path waypoints. 0 means that paths must be contiguous (as they are for biters). Values greater than 0 will produce paths with "gaps" that are suitable for spiders. Allowed values are from `0` to `31`. Defaults to `0`.
- **`max_attack_distance`** — [[double]] *(optional)*: Defines the maximum allowed distance between the last traversable path waypoint and an obstacle entity to be destroyed. Only used when finding a discontiguous path, i.e. when `max_gap_size` > 0. This field filters out paths that are blocked by obstacles that are outside the entity's attack range. Allowed values are `0` or greater. Defaults to `max_gap_size`.
- **`entity_to_ignore`** — [[LuaEntity]] *(optional)*: Makes the pathfinder ignore collisions with this entity if it is given.

**Returns:**
- [[uint32]]: A unique handle to identify this call when [[on_script_path_request_finished]] fires.

**Raises:**
- [[on_script_path_request_finished]] *(timeframe: future_tick)*

### get_script_areas
Gets the script areas that match the given name or if no name is given all areas are returned.

**Parameters:**
- **`name`** — [[string]] *(optional)*

**Returns:**
- array<[[ScriptArea]]>

### get_script_area
Gets the first script area by name or id.

**Parameters:**
- **`key`** — [[string]] | [[uint32]] *(optional)*: The name or id of the area to get.

**Returns:**
- [[ScriptArea]] *(optional)*

### edit_script_area
Sets the given script area to the new values.

**Parameters:**
- **`id`** — [[uint32]]: The area to edit.
- **`area`** — [[ScriptArea]]

### add_script_area
Adds the given script area.

**Parameters:**
- **`area`** — [[ScriptArea]]

**Returns:**
- [[uint32]]: The id of the created area.

### remove_script_area
Removes the given script area.

**Parameters:**
- **`id`** — [[uint32]]

**Returns:**
- [[boolean]]: If the area was actually removed. False when it didn't exist.

### get_script_positions
Gets the script positions that match the given name or if no name is given all positions are returned.

**Parameters:**
- **`name`** — [[string]] *(optional)*

**Returns:**
- array<[[ScriptPosition]]>

### get_script_position
Gets the first script position by name or id.

**Parameters:**
- **`key`** — [[string]] | [[uint32]] *(optional)*: The name or id of the position to get.

**Returns:**
- [[ScriptPosition]] *(optional)*

### edit_script_position
Sets the given script position to the new values.

**Parameters:**
- **`id`** — [[uint32]]: The position to edit.
- **`position`** — [[ScriptPosition]]

### add_script_position
Adds the given script position.

**Parameters:**
- **`position`** — [[ScriptPosition]]

**Returns:**
- [[uint32]]: The id of the created position.

### remove_script_position
Removes the given script position.

**Parameters:**
- **`id`** — [[uint32]]

**Returns:**
- [[boolean]]: If the position was actually removed. False when it didn't exist.

### get_map_exchange_string
Gets the map exchange string for the current map generation settings of this surface.

**Returns:**
- [[string]]

### get_starting_area_radius
Gets the starting area radius of this surface.

**Returns:**
- [[double]]

### get_closest
Gets the closest entity in the list to this position.

**Parameters:**
- **`position`** — [[MapPosition]]
- **`entities`** — array<[[LuaEntity]]>: The Entities to check.

**Returns:**
- [[LuaEntity]] *(optional)*

### get_total_pollution
Gets the total amount of pollution on the surface by iterating over all the chunks containing pollution.

**Returns:**
- [[double]]

### entity_prototype_collides
Whether the given entity prototype collides at the given position and direction.

**Parameters:**
- **`prototype`** — [[EntityID]]: The entity prototype to check.
- **`position`** — [[MapPosition]]: The position to check.
- **`use_map_generation_bounding_box`** — [[boolean]]: If the map generation bounding box should be used instead of the collision bounding box.
- **`direction`** — [[defines.direction]] *(optional)*

**Returns:**
- [[boolean]]

### decorative_prototype_collides
Whether the given decorative prototype collides at the given position and direction.

**Parameters:**
- **`prototype`** — [[DecorativeID]]: The decorative prototype to check.
- **`position`** — [[MapPosition]]: The position to check.

**Returns:**
- [[boolean]]

### calculate_tile_properties
Calculate values for a list of tile properties at a list of positions. Requests for unrecognized properties will be ignored, so this can also be used to test whether those properties exist.

**Parameters:**
- **`property_names`** — array<[[string]]>: Names of properties (`"elevation"`, etc) to calculate.
- **`positions`** — array<[[MapPosition]]>: Positions for which to calculate property values.

**Returns:**
- dictionary<[[string]] → array<[[double]]>>: Table of property value lists, keyed by property name.

### get_entities_with_force
Returns all the military targets (entities with force) on this chunk for the given force.

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk's position.
- **`force`** — [[ForceID]]: Entities of this force will be returned.

**Returns:**
- array<[[LuaEntity]]>

### create_entities_from_blueprint_string
This method only works when used in simulations.

Places entities via the given blueprint string. These entities are force-built.

Takes a table with the following fields:
- **`string`** — [[string]]: The blueprint string to import.
- **`position`** — [[MapPosition]]: The position to place the blueprint at.
- **`force`** — [[ForceID]] *(optional)*: The force to place the blueprint for. Defaults to the player force.
- **`direction`** — [[defines.direction]] *(optional)*: The direction to place the blueprint in. Defaults to north.
- **`flip_horizontal`** — [[boolean]] *(optional)*: Whether to flip the blueprint horizontally. Defaults to `false`.
- **`flip_vertical`** — [[boolean]] *(optional)*: Whether to flip the blueprint vertically. Defaults to `false`.
- **`by_player`** — [[PlayerIdentification]] *(optional)*: The player that placed the blueprint. Defaults to `nil`.

**Returns:**
- [[int32]] *(optional)*: If the blueprint string was invalid, `1` is returned. Otherwise, `nil` is returned.

### build_checkerboard
Sets the given area to the checkerboard lab tiles.

**Parameters:**
- **`area`** — [[BoundingBox]]: The tile area.

### get_property
Gets the value of surface property on this surface.

**Parameters:**
- **`property`** — [[SurfacePropertyID]]: Property to read.

**Returns:**
- [[double]]: Value of the property.

### set_property
Sets the value of surface property on this surface.

**Parameters:**
- **`property`** — [[SurfacePropertyID]]: Property to change.
- **`value`** — [[double]]: The wanted value of the property.

### create_global_electric_network
Creates a global electric network for this surface, if one doesn't exist already.

### destroy_global_electric_network
Destroys the global electric network for this surface, if it exists.

### execute_lightning
Creates lightning. If other entities which can be lightning targets are nearby, the final position will be adjusted.

Takes a table with the following fields:
- **`name`** — [[EntityID]]
- **`position`** — [[MapPosition]]

### clear_hidden_tiles
Completely removes hidden and double hidden tiles data on this surface.

### get_default_cover_tile
Gets the cover tile for the given force and tile on this surface if one is set.

**Parameters:**
- **`force`** — [[ForceID]]
- **`tile`** — [[TileID]]

**Returns:**
- [[LuaTilePrototype]] *(optional)*

### set_default_cover_tile
Sets the cover tile for the given force and tile on this surface.

**Parameters:**
- **`force`** — [[ForceID]]
- **`from_tile`** — [[TileID]]
- **`to_tile`** — [[TileID]] | [[nil]]
