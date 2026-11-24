---
title: LuaForce
tags: [factorio-api, runtime, class]
---
# LuaForce

`LuaForce` encapsulates data local to each "force" or "faction" of the game. Default forces are player, enemy and neutral. Players and mods can create additional forces (up to 64 total).

## Attributes

### name
- **Type:** [[string]]
Name of the force.
**Examples:**

```
game.player.print(game.player.force.name) -- => "player"
```

### technologies
- **Type:** LuaCustomTable<[[string]] → [[LuaTechnology]]>
Technologies owned by this force, indexed by `name`.
**Examples:**

```
-- Researches the technology for the player's force
game.player.force.technologies["steel-processing"].researched = true
```

### recipes
- **Type:** LuaCustomTable<[[string]] → [[LuaRecipe]]>
Recipes available to this force, indexed by `name`.
**Examples:**

```
-- Prints the category of the given recipe
game.player.print(game.player.force.recipes["transport-belt"].category)
```

### manual_mining_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
Multiplier of the manual mining speed. Default value is `0`. The actual mining speed will be multiplied by `1 + manual_mining_speed_modifier`.
**Examples:**

```
-- Double the player's mining speed
game.player.force.manual_mining_speed_modifier = 1
```

### manual_crafting_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
Multiplier of the manual crafting speed. Default value is `0`. The actual crafting speed will be multiplied by `1 + manual_crafting_speed_modifier`.
**Examples:**

```
-- Double the player's crafting speed
game.player.force.manual_crafting_speed_modifier = 1
```

### laboratory_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]

### laboratory_productivity_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### worker_robots_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]

### worker_robots_battery_modifier
- **Type:** [[double]]
- **Writable:** [[double]]

### worker_robots_storage_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### current_research
- **Type:** [[LuaTechnology]]
- **Optional**
The currently ongoing technology research, if any.

### research_progress
- **Type:** [[double]]
- **Writable:** [[double]]
Progress of current research, as a number in range `[0, 1]`.

### previous_research
- **Type:** [[LuaTechnology]]
- **Writable:** [[LuaTechnology]]
- **Optional**
The previous research, if any.

### inserter_stack_size_bonus
- **Type:** [[double]]
- **Writable:** [[double]]
The inserter stack size bonus for non stack inserters

### bulk_inserter_capacity_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Number of items that can be transferred by bulk inserters. When writing to this value, it must be >= 0 and <= 254.

### belt_stack_size_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Belt stack size bonus.

### character_trash_slot_count
- **Type:** [[double]]
- **Writable:** [[double]]
Number of character trash slots.

### maximum_following_robot_count
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Maximum number of follower robots.

### following_robots_lifetime_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
Additional lifetime for following robots.

### create_ghost_on_entity_death
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When an entity dies, a ghost will be placed for automatic reconstruction.

### circuit_network_enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### cliff_deconstruction_enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When true, cliffs will be marked for deconstruction when trying to force-build things that collide.

### mining_with_fluid
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### rail_support_on_deep_oil_ocean
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### rail_planner_allow_elevated_rails
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### vehicle_logistics
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When true, cars/tanks that support logistics will be able to use them.

### unlock_logistic_network
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When true, a "connect to logistic network" button will become enabled for entities that can connect to a logistic network.

### unlock_travel_to_space_platforms
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether traveling to space platforms via rockets is unlocked.

### players
- **Type:** array<[[LuaPlayer]]>
Players belonging to this force.

### ai_controllable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Enables some higher-level AI behaviour for this force. When set to `true`, biters belonging to this force will automatically expand into new territories, build new spawners, and form unit groups. By default, this value is `true` for the enemy force and `false` for all others.

Setting this to `false` does not turn off biters' AI. They will still move around and attack players who come close.

It is necessary for a force to be AI controllable in order to be able to create unit groups or build bases from scripts.

### logistic_networks
- **Type:** dictionary<[[string]] → array<[[LuaLogisticNetwork]]>>
List of logistic networks, grouped by surface.

### character_running_speed_modifier
- **Type:** [[double]]
- **Writable:** [[double]]
Modifies the running speed of all characters in this force by the given value as a percentage. Setting the running modifier to `0.5` makes the character run 50% faster. The minimum value of `-1` reduces the movement speed by 100%, resulting in a speed of `0`.

### artillery_range_modifier
- **Type:** [[double]]
- **Writable:** [[double]]

### beacon_distribution_modifier
- **Type:** [[double]]
- **Writable:** [[double]]

### character_build_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### character_item_drop_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### character_reach_distance_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### character_resource_reach_distance_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### character_item_pickup_distance_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### character_loot_pickup_distance_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### character_inventory_slots_bonus
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of additional inventory slots the character main inventory has.

### deconstruction_time_to_live
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The time, in ticks, before a deconstruction order is removed.

### character_health_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### max_successful_attempts_per_tick_per_construction_queue
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### max_failed_attempts_per_tick_per_construction_queue
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### character_logistic_requests
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
`true` if character requester logistics is enabled.

### cargo_landing_pad_limit
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The maximum cargo landing pads that can be built per surface by this force.

### max_cargo_bay_unloading_distance
- **Type:** [[double]]
- **Writable:** [[double]]
Maximum distance between cargo bay from its connected cargo landing pad that allows unloading. Only relevant for cargo bays that have both [[LuaEntityPrototype#allow_unloading|LuaEntityPrototype::allow_unloading]] and [[LuaEntityPrototype#use_unloading_distance_limit|LuaEntityPrototype::use_unloading_distance_limit]] set to `true`.

### rockets_launched
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of rockets launched.

### items_launched
- **Type:** dictionary<[[string]] → [[ItemCountType]]>
All of the items that have been launched in rockets.

### connected_players
- **Type:** array<[[LuaPlayer]]>
The connected players belonging to this force.

This is primarily useful when you want to do some action against all online players of this force.

This does *not* index using player index. See [[LuaPlayer#index|LuaPlayer::index]] on each player instance for the player index.

### mining_drill_productivity_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### train_braking_force_bonus
- **Type:** [[double]]
- **Writable:** [[double]]

### friendly_fire
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If friendly fire is enabled for this force.

### share_chart
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If sharing chart data is enabled for this force.

### index
- **Type:** [[uint32]]
This force's index in [[LuaGameScript#forces|LuaGameScript::forces]] (unique ID). It is assigned when a force is created, and remains so until it is [[on_forces_merged|merged]] (ie. deleted). Indexes of merged forces can be reused.

### research_queue
- **Type:** array<[[TechnologyID]]>
- **Writable:** array<[[TechnologyID]]>
The research queue of this force. The first technology in the array is the currently active one. Reading this attribute gives an array of [[LuaTechnology]].

To write to this, the entire table must be written. Providing an empty table or `nil` will empty the research queue and cancel the current research.

This only allows mods to queue research that this force is able to research in the first place. As an example, an already researched technology or one whose prerequisites are not fulfilled will not be queued, but dropped silently instead.

### research_enabled
- **Type:** [[boolean]]
Whether research is enabled for this force, see [[LuaForce#enable_research|LuaForce::enable_research]] and [[LuaForce#disable_research|LuaForce::disable_research]].

### platforms
- **Type:** dictionary<[[uint32]] → [[LuaSpacePlatform]]>
The space platforms that belong to this force mapped by their index value.

This will include platforms that are pending deletion.

### custom_color
- **Type:** [[Color]]
- **Writable:** [[Color]]
- **Optional**
Custom color for this force. If specified, will take priority over other sources of the force color. Writing `nil` clears custom color. Will return `nil` if it was not specified or if was set to `{0,0,0,0}`.

### color
- **Type:** [[Color]]
Effective color of this force.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_entity_count
Count entities of given type.

This function has O(1) time complexity as entity counts are kept and maintained in the game engine.

**Parameters:**
- **`name`** — [[EntityID]]: Prototype name of the entity.

**Returns:**
- [[uint32]]: Number of entities of given prototype belonging to this force.

### disable_research
Disable research for this force.

### enable_research
Enable research for this force.

### disable_all_prototypes
Disable all recipes and technologies. Only recipes and technologies enabled explicitly will be useable from this point.

### enable_all_prototypes
Enables all recipes and technologies. The opposite of [[LuaForce#disable_all_prototypes|LuaForce::disable_all_prototypes]].

### reset_recipes
Load the original version of all recipes from the prototypes.

### enable_all_recipes
Unlock all recipes.

### enable_all_technologies
Unlock all technologies.

### research_all_technologies
Research all technologies.

**Parameters:**
- **`include_disabled_prototypes`** — [[boolean]] *(optional)*: Whether technologies that are explicitly disabled in the prototype should also be researched. Defaults to `false`.

**Raises:**
- [[on_research_finished]] *(timeframe: instantly)*

### reset_technologies
Load the original versions of technologies from prototypes. Preserves research, enabled and visible_when_disabled state of technologies.

### reset
Reset everything. All technologies are set to not researched, all modifiers are set to default values.

**Raises:**
- [[on_force_reset]] *(timeframe: instantly)*

### reset_technology_effects
Reapplies all possible research effects, including unlocked recipes. Any custom changes are lost. Preserves research state of technologies.

**Raises:**
- [[on_technology_effects_reset]] *(timeframe: instantly)*

### chart
Chart a portion of the map. The chart for the given area is refreshed; it creates chart for any parts of the given area that haven't been charted yet.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`area`** — [[BoundingBox]]: The area on the given surface to chart.

**Examples:**

```
-- Charts a 2048x2048 rectangle centered around the origin.
game.player.force.chart(game.player.surface, {{x = -1024, y = -1024}, {x = 1024, y = 1024}})
```

### clear_chart
Erases chart data for this force.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Which surface to erase chart data for or if not provided all surfaces charts are erased.

### rechart
Force a rechart of the whole chart.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Which surface to rechart or all if not given.

### chart_all
Chart all generated chunks.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Which surface to chart or all if not given.

### copy_from
Copies all of the given changeable values (except charts) from the given force to this force.

**Parameters:**
- **`force`** — [[ForceID]]: The force to copy from.

### copy_chart
Copies the given surface's chart from the given force to this force.

**Parameters:**
- **`source_force`** — [[ForceID]]: The force to copy from
- **`source_surface`** — [[SurfaceIdentification]]: The surface to copy from.
- **`destination_surface`** — [[SurfaceIdentification]]: The surface to copy to.

### is_chunk_charted
Has a chunk been charted?

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`chunk_position`** — [[ChunkPosition]]: Position of the chunk.

**Returns:**
- [[boolean]]

### is_chunk_visible
Is the given chunk currently charted and visible (not covered by fog of war) on the map.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`chunk_position`** — [[ChunkPosition]]

**Returns:**
- [[boolean]]

### is_chunk_requested_for_charting
Has a chunk been requested for charting?

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`chunk_position`** — [[ChunkPosition]]: Position of the chunk.

**Returns:**
- [[boolean]]

### cancel_charting
Cancels pending chart requests for the given surface or all surfaces.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*

### get_ammo_damage_modifier

**Parameters:**
- **`ammo`** — [[string]]: Ammo category

**Returns:**
- [[double]]

### set_ammo_damage_modifier

**Parameters:**
- **`ammo`** — [[string]]: Ammo category
- **`modifier`** — [[double]]

### get_gun_speed_modifier

**Parameters:**
- **`ammo`** — [[string]]: Ammo category

**Returns:**
- [[double]]

### set_gun_speed_modifier

**Parameters:**
- **`ammo`** — [[string]]: Ammo category
- **`modifier`** — [[double]]

### get_turret_attack_modifier

**Parameters:**
- **`turret`** — [[EntityID]]: Turret prototype name

**Returns:**
- [[double]]

### set_turret_attack_modifier

**Parameters:**
- **`turret`** — [[EntityID]]: Turret prototype name
- **`modifier`** — [[double]]

### set_cease_fire
Add `other` force to this force's cease fire list. Forces on the cease fire list won't be targeted for attack.

**Parameters:**
- **`other`** — [[ForceID]]
- **`cease_fire`** — [[boolean]]

**Raises:**
- [[on_force_cease_fire_changed]] *(timeframe: instantly)*

### get_cease_fire
Is `other` force in this force's cease fire list?

**Parameters:**
- **`other`** — [[ForceID]]

**Returns:**
- [[boolean]]

### set_friend
Add `other` force to this force's friends list. Friends have unrestricted access to buildings and turrets won't fire at them.

**Parameters:**
- **`other`** — [[ForceID]]
- **`friend`** — [[boolean]]

**Raises:**
- [[on_force_friends_changed]] *(timeframe: instantly)*

### get_friend
Is `other` force in this force's friends list.

**Parameters:**
- **`other`** — [[ForceID]]

**Returns:**
- [[boolean]]

### is_pathfinder_busy
Is pathfinder busy? When the pathfinder is busy, it won't accept any more pathfinding requests.

**Returns:**
- [[boolean]]

### kill_all_units
Kill all units and flush the pathfinder.

### find_logistic_network_by_position

**Parameters:**
- **`position`** — [[MapPosition]]: Position to find a network for
- **`surface`** — [[SurfaceIdentification]]: Surface to search on

**Returns:**
- [[LuaLogisticNetwork]] *(optional)*: The found network or `nil`.

### set_spawn_position

**Parameters:**
- **`position`** — [[MapPosition]]: The new position on the given surface.
- **`surface`** — [[SurfaceIdentification]]: Surface to set the spawn position for.

### get_spawn_position

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[MapPosition]]

### set_surface_hidden

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]: Surface to set hidden for.
- **`hidden`** — [[boolean]]: Whether to hide the surface or not.

### get_surface_hidden

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[boolean]]

### unchart_chunk

**Parameters:**
- **`chunk_position`** — [[ChunkPosition]]: The chunk position to unchart.
- **`surface`** — [[SurfaceIdentification]]: Surface to unchart on.

### get_item_launched
Gets the count of a given item launched in rockets.

**Parameters:**
- **`item`** — [[ItemID]]: The item to get

**Returns:**
- [[uint32]]: The count of the item that has been launched.

### set_item_launched
Sets the count of a given item launched in rockets.

**Parameters:**
- **`item`** — [[ItemID]]: The item to set
- **`count`** — [[uint32]]: The count to set

### print
Print text to the chat console of all players on this force.

By default, messages that are identical to a message sent in the last 60 ticks are not printed again.

**Parameters:**
- **`message`** — [[LocalisedString]]
- **`print_settings`** — [[PrintSettings]] *(optional)*

### add_chart_tag
Adds a custom chart tag to the given surface and returns the new tag or `nil` if the given position isn't valid for a chart tag.

The chunk must be charted for a tag to be valid at that location.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]: Which surface to add the tag to.
- **`tag`** — [[ChartTagSpec]]: The tag to add.

**Returns:**
- [[LuaCustomChartTag]] *(optional)*

**Raises:**
- [[on_chart_tag_added]] *(timeframe: instantly)*: Raised if the chart tag was successfully added.

### find_chart_tags
Finds all custom chart tags within a given area on the given surface. If no area is given all custom chart tags on the surface are returned.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`area`** — [[BoundingBox]] *(optional)*

**Returns:**
- array<[[LuaCustomChartTag]]>

### reset_evolution
Resets evolution for this force to zero.

### play_sound
Play a sound for every player in this force.

The sound is not played if its location is not [[LuaForce#chart|charted]] for this force.

**Parameters:**
- **`sound_specification`** — [[PlaySoundSpecification]]: The sound to play.

### play_music
Play a music track for every player in this force.

**Parameters:**
- **`music_specification`** — [[PlayMusicSpecification]]: The track to play.

### get_hand_crafting_disabled_for_recipe
Gets if the given recipe is explicitly disabled from being hand crafted.

**Parameters:**
- **`recipe`** — [[RecipeID]]

**Returns:**
- [[boolean]]

### set_hand_crafting_disabled_for_recipe
Sets if the given recipe can be hand-crafted. This is used to explicitly disable hand crafting a recipe - it won't allow hand-crafting otherwise not hand-craftable recipes.

**Parameters:**
- **`recipe`** — [[RecipeID]]
- **`hand_crafting_disabled`** — [[boolean]]

### add_research
Add this technology to the back of the research queue.

**Parameters:**
- **`technology`** — [[TechnologyID]]

**Returns:**
- [[boolean]]: Whether the technology was successfully added.

**Raises:**
- [[on_research_started]] *(timeframe: instantly)*: Raised if the technology was successfully added.

### cancel_current_research
Stop the research currently in progress. This will remove any dependent technologies from the research queue.

### get_linked_inventory
Gets the linked inventory for the given prototype and link ID if it exists or `nil`.

**Parameters:**
- **`prototype`** — [[EntityID]]
- **`link_id`** — [[uint32]]

**Returns:**
- [[LuaInventory]] *(optional)*

### is_friend
Is this force a friend? This differs from `get_friend` in that it is always true for neutral force. This is equivalent to checking the `friend` ForceCondition.

**Parameters:**
- **`other`** — [[ForceID]]

**Returns:**
- [[boolean]]

### is_enemy
Is this force an enemy? This differs from `get_cease_fire` in that it is always false for neutral force. This is equivalent to checking the `enemy` ForceCondition.

**Parameters:**
- **`other`** — [[ForceID]]

**Returns:**
- [[boolean]]

### lock_space_location
Locks the planet to not be accessible to this force.

**Parameters:**
- **`name`** — [[SpaceLocationID]]: Name of the planet.

### unlock_space_location
Unlocks the planet to be accessible to this force.

**Parameters:**
- **`name`** — [[SpaceLocationID]]: Name of the planet.

### is_space_location_unlocked
Is the specified planet unlocked for this force?

**Parameters:**
- **`name`** — [[SpaceLocationID]]: Name of the planet.

### is_visible
Is the given unlockable ID visible either through computed technologies or script set state.

**Parameters:**
- **`unlockable`** — [[UnlockableID]]

**Returns:**
- [[boolean]]

### set_script_visible
Sets the given unlockable ID state. When set to explicitly hidden or visible the value overrides the state computed through technologies.

**Parameters:**
- **`unlockable`** — [[UnlockableID]]
- **`value`** — [[boolean]] *(optional)*

### get_script_visible
Gets the unlockable script state for the given ID.

**Parameters:**
- **`unlockable`** — [[UnlockableID]]

**Returns:**
- [[boolean]] *(optional)*

### lock_quality
Locks the quality to not be accessible to this force.

**Parameters:**
- **`quality`** — [[QualityID]]: Name of the quality.

### unlock_quality
Unlocks the quality to be accessible to this force.

**Parameters:**
- **`quality`** — [[QualityID]]: Name of the quality.

### is_quality_unlocked
Is the specified quality unlocked for this force?

**Parameters:**
- **`quality`** — [[QualityID]]: Name of the quality.

### lock_space_platforms
Locks the space platforms, which disables the space platforms button

### unlock_space_platforms
Unlocks the space platforms, which enables the space platforms button

### is_space_platforms_unlocked
Are the space platforms unlocked? This basically just controls the availability of the space platforms button.

**Returns:**
- [[boolean]]

### create_space_platform
Creates a new space platform on this force.

Takes a table with the following fields:
- **`name`** — [[string]] *(optional)*: The platform name. If not provided, a random name will be used.
- **`planet`** — [[SpaceLocationID]]: The planet that the platform will orbit.
- **`starter_pack`** — [[ItemWithQualityID]]: The starter pack required to build the platform.

**Returns:**
- [[LuaSpacePlatform]] *(optional)*

### get_space_platforms
Gets the built space platforms at the given space location for this force.

Note, this does not include platforms that have not yet been built.

**Parameters:**
- **`location`** — [[SpaceLocationID]]

**Returns:**
- array<[[LuaSpacePlatform]]>

### get_evolution_factor
Fetches the evolution factor of this force on the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

**Returns:**
- [[double]]

### get_evolution_factor_by_pollution
Fetches the pollution part of the evolution factor of this force on the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

**Returns:**
- [[double]]

### get_evolution_factor_by_time
Fetches the time part of the evolution factor of this force on the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

**Returns:**
- [[double]]

### get_evolution_factor_by_killing_spawners
Fetches the spawner kill part of the evolution factor of this force on the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

**Returns:**
- [[double]]

### set_evolution_factor
Sets the evolution factor of this force on the given surface.

**Parameters:**
- **`factor`** — [[double]]
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

### set_evolution_factor_by_pollution
Sets the pollution part of the evolution factor of this force on the given surface.

**Parameters:**
- **`factor`** — [[double]]
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

### set_evolution_factor_by_time
Sets the time part of the evolution factor of this force on the given surface.

**Parameters:**
- **`factor`** — [[double]]
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

### set_evolution_factor_by_killing_spawners
Sets the spawner kill part of the evolution factor of this force on the given surface.

**Parameters:**
- **`factor`** — [[double]]
- **`surface`** — [[SurfaceIdentification]] *(optional)*: Defaults to "nauvis".

### get_item_production_statistics
The item production statistics for this force for the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[LuaFlowStatistics]]

### get_fluid_production_statistics
The fluid production statistics for this force for the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[LuaFlowStatistics]]

### get_kill_count_statistics
The kill counter statistics for this force for the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[LuaFlowStatistics]]

### get_entity_build_count_statistics
The entity build statistics for this force (built and mined) for the given surface.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]

**Returns:**
- [[LuaFlowStatistics]]

### get_logistic_groups
Gets the names of the current logistic groups.

**Parameters:**
- **`type`** — [[defines.logistic_group_type]] *(optional)*: Defaults to `defines.logistic_group_type.with_trash`.

**Returns:**
- array<[[string]]>

### get_logistic_group
Gets the information about the given logistic group.

**Parameters:**
- **`name`** — [[string]]
- **`type`** — [[defines.logistic_group_type]] *(optional)*: Defaults to `defines.logistic_group_type.with_trash`.

**Returns:**
- [[LogisticGroup]] *(optional)*

### create_logistic_group
Creates the given group if it doesn't already exist.

**Parameters:**
- **`name`** — [[string]]
- **`type`** — [[defines.logistic_group_type]] *(optional)*: Defaults to `defines.logistic_group_type.with_trash`.

### delete_logistic_group
Deletes the given logistic group if it exists.

**Parameters:**
- **`name`** — [[string]]
- **`type`** — [[defines.logistic_group_type]] *(optional)*: Defaults to `defines.logistic_group_type.with_trash`.

### get_chunk_chart
Gets the raw chart data for a given chunk as a binary string.

The pixel data is returned in RGB565 format (2 bytes per pixel).

Returns `nil` if the chunk has not been charted for this force.

**Parameters:**
- **`surface`** — [[SurfaceIdentification]]
- **`chunk_position`** — [[ChunkPosition]]

**Returns:**
- [[string]] *(optional)*: The raw pixel data.

### script_trigger_research
Trigger the "scripted" [[ResearchTrigger|research trigger]] of a technology, researching it. Does nothing if the technology does not have a "scripted" research trigger.

**Parameters:**
- **`technology`** — [[TechnologyID]]

### add_alert
Adds an alert to every connected player on this force.

**Parameters:**
- **`entity`** — [[LuaEntity]]
- **`type`** — [[defines.alert_type]]

### add_custom_alert
Adds a custom alert to every connected player on this force.

**Parameters:**
- **`entity`** — [[LuaEntity]]: If the alert is clicked, the map will open at the position of this entity.
- **`icon`** — [[SignalID]]
- **`message`** — [[LocalisedString]]
- **`show_on_map`** — [[boolean]]

### remove_alert
For every connected player on this force - removes all alerts matching the given filters or if an empty filters table is given all alerts are removed.

**Parameters:**
- **`filter`** — [[AlertFilter]]
