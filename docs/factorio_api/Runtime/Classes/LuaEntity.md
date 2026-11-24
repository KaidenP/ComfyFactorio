---
title: LuaEntity
tags: [factorio-api, runtime, class]
---
# LuaEntity

> **Extends:** [[LuaControl]]

The primary interface for interacting with entities through the Lua API. Entities are everything that exists on the map except for tiles (see [[LuaTile]]).

Most functions on LuaEntity also work when the entity is contained in a ghost.

## Attributes

### rail_length
- **Type:** [[double]]
Length of this rail piece.

### fluids_count
- **Type:** [[uint32]]
Returns count of fluid storages. This includes fluid storages provided by fluidboxes but also covers other fluid storages like fluid turret's internal buffer and fluid wagon's fluid.

### name
- **Type:** [[string]]
Name of the entity prototype. E.g. "inserter" or "fast-inserter".

### ghost_name
- **Type:** [[string]]
Name of the entity or tile contained in this ghost.

### localised_name
- **Type:** [[LocalisedString]]
Localised name of the entity.

### localised_description
- **Type:** [[LocalisedString]]

### ghost_localised_name
- **Type:** [[LocalisedString]]
Localised name of the entity or tile contained in this ghost.

### ghost_localised_description
- **Type:** [[LocalisedString]]

### type
- **Type:** [[string]]
The entity prototype type of this entity.

### ghost_type
- **Type:** [[string]]
The prototype type of the entity or tile contained in this ghost.

### use_filters
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If set to 'true', this inserter will use filtering logic.

This has no effect if the prototype does not support filters.

### active
- **Type:** [[boolean]]
A deactivated entity will stop all of its operations (car will stop moving, inserters will stop working, fish will stop moving, etc).

Reading from this returns `false` if the entity is deactivated in at least one of the following ways: [[LuaEntity#disabled_by_script|by script]], [[LuaEntity#disabled_by_control_behavior|by circuit network]], [[LuaEntity#disabled_by_recipe|by recipe]], [[LuaEntity#frozen|by freezing]], or by being marked for deconstruction.

If this entity is not considered [[LuaEntity#is_updatable|updatable]] then this always returns `false`.

### destructible
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If set to `false`, this entity can't be damaged and won't be attacked automatically. It can however still be mined.

Entities that are indestructible naturally (they have no health, like smoke, resource etc) can't be set to be destructible.

### minable
- **Type:** [[boolean]]
Not minable entities can still be destroyed.

Tells if entity reports as being minable right now. This takes into account `minable_flag` and entity specific conditions (for example rail under rolling stocks is not minable, vehicle with passenger is not minable).

### minable_flag
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Script controlled flag that allows entity to be mined.

### rotatable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When entity is not to be rotatable (inserter, transport belt etc), it can't be rotated by player using the R key.

Entities that are not rotatable naturally (like chest or furnace) can't be set to be rotatable.

### operable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Player can't open gui of this entity and he can't quick insert/input stuff in to the entity when it is not operable.

### protected
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Automated weapons won't target protected entities.

### health
- **Type:** [[float]]
- **Writable:** [[float]]
- **Optional**
The current health of the entity, if any. Health is automatically clamped to be between `0` and max health (inclusive). Entities with a health of `0` can not be attacked.

To get the maximum possible health of this entity, see [[LuaEntity#max_health|LuaEntity::max_health]].

### max_health
- **Type:** [[float]]
Max health of this entity.

### direction
- **Type:** [[defines.direction]]
- **Writable:** [[defines.direction]]
The current direction this entity is facing.

### mirroring
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether the entity is currently mirrored. This state is referred to as `flipped` elsewhere, such as on the [[on_player_flipped_entity]] event.

If an entity is mirrored, it is flipped over the axis that is pointing in the entity's direction. For example if a mirrored entity is facing north, everything that was defined to be facing east in the prototype now faces west.

### supports_direction
- **Type:** [[boolean]]
Whether the entity has direction. When it is false for this entity, it will always return north direction when asked for.

### orientation
- **Type:** [[RealOrientation]]
- **Writable:** [[RealOrientation]]
The smooth orientation of this entity. For turrets this is the orientation of the weapon.

### cliff_orientation
- **Type:** [[CliffOrientation]]
The orientation of this cliff.

### relative_turret_orientation
- **Type:** [[RealOrientation]]
- **Writable:** [[RealOrientation]]
- **Optional**
The relative orientation of the vehicle turret, artillery turret, artillery wagon. `nil` if this entity isn't a vehicle with a vehicle turret or artillery turret/wagon.

Writing does nothing if the vehicle doesn't have a turret.

For the turret orientation of non-artillery turrets, use [[LuaEntity#orientation|LuaEntity::orientation]].

### torso_orientation
- **Type:** [[RealOrientation]]
- **Writable:** [[RealOrientation]]
The torso orientation of this spider vehicle.

### amount
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Count of resource units contained.

### initial_amount
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**
Count of initial resource units contained. `nil` if this is not an infinite resource.

If this is not an infinite resource, writing will produce an error.

### effectivity_modifier
- **Type:** [[float]]
- **Writable:** [[float]]
Multiplies the acceleration the car can create for one unit of energy. Defaults to `1`.

### consumption_modifier
- **Type:** [[float]]
- **Writable:** [[float]]
Multiplies the energy consumption.

### friction_modifier
- **Type:** [[float]]
- **Writable:** [[float]]
Multiplies the car friction rate.
**Examples:**

```
-- This will allow the car to go much faster
game.player.vehicle.friction_modifier = 0.5
```

### driver_is_gunner
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
Whether the driver of this car or spidertron is the gunner. If `false`, the passenger is the gunner. `nil` if this is neither a car or a spidertron.

### vehicle_automatic_targeting_parameters
- **Type:** [[VehicleAutomaticTargetingParameters]]
- **Writable:** [[VehicleAutomaticTargetingParameters]]
Read when this spidertron auto-targets enemies

### speed
- **Type:** [[float]]
- **Writable:** [[float]]
- **Optional**
The current speed if this is a car, rolling stock, projectile or spidertron, or the maximum speed if this is a unit. The speed is in tiles per tick. `nil` if this is not a car, rolling stock, unit, projectile or spidertron.

Only the speed of units, cars, and projectiles are writable.

### effective_speed
- **Type:** [[float]]
- **Optional**
The current speed of this unit in tiles per tick, taking into account any walking speed modifier given by the tile the unit is standing on. `nil` if this is not a unit.

### stack
- **Type:** [[LuaItemStack]]

### prototype
- **Type:** [[LuaEntityPrototype]]
The entity prototype of this entity.

### ghost_prototype
- **Type:** [[LuaEntityPrototype]] | [[LuaTilePrototype]]
The prototype of the entity or tile contained in this ghost.

### drop_position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
Position where the entity puts its stuff.

Mining drills and crafting machines can't have their drop position changed; inserters must have `allow_custom_vectors` set to true on their prototype to allow changing the drop position.

Meaningful only for entities that put stuff somewhere, such as mining drills, crafting machines with a drop target or inserters.

### pickup_position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
Where the inserter will pick up items from.

Inserters must have `allow_custom_vectors` set to true on their prototype to allow changing the pickup position.

### drop_target
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The entity this entity is putting its items to. If there are multiple possible entities at the drop-off point, writing to this attribute allows a mod to choose which one to drop off items to. The entity needs to collide with the tile box under the drop-off position. `nil` if there is no entity to put items to, or if this is not an entity that puts items somewhere.

### pickup_target
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The entity this inserter will attempt to pick up items from. If there are multiple possible entities at the pick-up point, writing to this attribute allows a mod to choose which one to pick up items from. The entity needs to collide with the tile box under the pick-up position. `nil` if there is no entity to pull items from.

### selected_gun_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**
Index of the currently selected weapon slot of this character, car, or spidertron. `nil` if this entity doesn't have guns.

### energy
- **Type:** [[double]]
- **Writable:** [[double]]
Energy stored in the entity's energy buffer (energy stored in electrical devices etc.). Always 0 for entities that don't have the concept of energy stored inside.
**Examples:**

```
game.player.print("Machine energy: " .. game.player.selected.energy .. "J")
game.player.selected.energy = 3000
```

### temperature
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The temperature of this entity's heat energy source or this entity's heat buffer. `nil` if this entity does not use a heat energy source or does not have a heat buffer.

The following entity types have a heat buffer: heat pipe, reactor and heat interface.

### previous_recipe
- **Type:** [[RecipeIDAndQualityIDPair]]
- **Optional**
The previous recipe this furnace was using, if any.

### held_stack
- **Type:** [[LuaItemStack]]
The item stack currently held in an inserter's hand.

### held_stack_position
- **Type:** [[MapPosition]]
Current position of the inserter's "hand".

### train
- **Type:** [[LuaTrain]]
- **Optional**
The train this rolling stock belongs to, if any. `nil` if this is not a rolling stock.

### fluidbox_neighbours
- **Type:** array<array<[[LuaEntity]]>>
A list of neighbours connected to fluidboxes of this entity. Neighbours are grouped by index of fluid box of this entity to which they are connected. For more detailed informations please use [[LuaEntity#get_fluid_box_neighbours|LuaEntity::get_fluid_box_neighbours]].

### underground_belt_neighbour
- **Type:** [[LuaEntity]]
- **Optional**
Neighbour underground belt connected to this underground belt through underground lines.

### wall_neighbours
- **Type:** table
Table of wall-connectable neighbours.

### belt_neighbours
- **Type:** table
The belt connectable neighbours of this belt connectable entity. Only entities that input to or are outputs of this entity. Does not contain the other end of an underground belt, see [[LuaEntity#underground_belt_neighbour|LuaEntity::underground_belt_neighbour]] for that.

### heat_neighbours
- **Type:** array<[[LuaEntity]]>
The entities connected to this entity's heat energy source or this entity's heat buffer.

The following entity types have a heat buffer: heat pipe, reactor and heat interface.

### cliff_neighbours
- **Type:** table
Table of cliff neighbours.

### neighbour_connectable_connections
- **Type:** array<[[NeighbourConnectableConnection]]>
Connections of a [[LuaEntityPrototype#neighbour_connectable|neighbour connectable]] entity. Includes connections that aren't currently connected to another entity.

### backer_name
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The backer name assigned to this entity. Entities that support backer names are labs, locomotives, radars, roboports, and train stops. `nil` if this entity doesn't support backer names.

While train stops get the name of a backer when placed down, players can rename them if they want to. In this case, `backer_name` returns the player-given name of the entity.

### entity_label
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The label on this spider-vehicle entity, if any. `nil` if this is not a spider-vehicle.

### time_to_live
- **Type:** [[uint64]]
- **Writable:** [[uint64]]
The ticks left before a combat robot, highlight box, smoke, or sticker entity is destroyed.

### color
- **Type:** [[Color]]
- **Writable:** [[Color]]
- **Optional**
The color of this character, rolling stock, corpse, character corpse, train stop, simple-entity-with-owner, car, spider-vehicle, or lamp. `nil` if this entity doesn't use custom colors.

Car color is overridden by the color of the current driver/passenger, if there is one.

### signal_state
- **Type:** [[defines.signal_state]]
The state of this rail signal.

### chain_signal_state
- **Type:** [[defines.chain_signal_state]]
The state of this chain signal.

### to_be_looted
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Will this item entity be picked up automatically when the player walks over it?

### crafting_speed
- **Type:** [[double]]
The current crafting speed, including speed bonuses from modules and beacons.

### crafting_progress
- **Type:** [[float]]
- **Writable:** [[float]]
The current crafting progress, as a number in range `[0, 1]`.

### bonus_progress
- **Type:** [[double]]
- **Writable:** [[double]]
The current productivity bonus progress, as a number in range `[0, 1]`.

### result_quality
- **Type:** [[LuaQualityPrototype]]
- **Writable:** [[QualityID]]
- **Optional**
The quality produced when this crafting machine finishes crafting. `nil` when crafting is not in progress.

Note: Writing `nil` is not allowed.

### productivity_bonus
- **Type:** [[double]]
The productivity bonus of this entity.

This includes force based bonuses as well as beacon/module bonuses.

### pollution_bonus
- **Type:** [[double]]
The pollution bonus of this entity.

### speed_bonus
- **Type:** [[double]]
The speed bonus of this entity.

This includes force based bonuses as well as beacon/module bonuses.

### consumption_bonus
- **Type:** [[double]]
The consumption bonus of this entity.

### belt_to_ground_type
- **Type:** [[BeltConnectionType]]
Whether this underground belt goes into or out of the ground.

### loader_type
- **Type:** [[BeltConnectionType]]
- **Writable:** [[BeltConnectionType]]
Whether this loader gets items from or puts item into a container.

### use_transitional_requests
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When true, the rocket silo will automatically request items for space platforms in orbit.

Setting the value will have no effect when the silo doesn't support logistics.

### transitional_request_target
- **Type:** [[LuaSpacePlatform]]
- **Optional**
The space platform in orbit this rocket silo is automatically requesting items for.

### rocket_parts
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Number of rocket parts in this rocket silo.

### send_to_orbit_automatically
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this rocket silo is set to send items to orbit automatically. Only relevant if there is an item prototype with [[LuaItemPrototype#rocket_launch_products|launch products]] with automated [[LuaItemPrototype#send_to_orbit_mode|send_to_orbit_mode]], such as the satellite in vanilla (without Space Age mod).

### logistic_network
- **Type:** [[LuaLogisticNetwork]]
- **Writable:** [[LuaLogisticNetwork]]
The logistic network this entity is a part of, or `nil` if this entity is not a part of any logistic network.

### logistic_cell
- **Type:** [[LuaLogisticCell]]
The logistic cell this entity is a part of. Will be `nil` if this entity is not a part of any logistic cell.

### item_requests
- **Type:** array<[[ItemWithQualityCount]]>
Items this ghost will request when revived or items this item request proxy is requesting.

### insert_plan
- **Type:** array<[[BlueprintInsertPlan]]>
- **Writable:** array<[[BlueprintInsertPlan]]>
The insert plan for this ghost or item request proxy.

### removal_plan
- **Type:** array<[[BlueprintInsertPlan]]>
- **Writable:** array<[[BlueprintInsertPlan]]>
The removal plan for this item request proxy.

### player
- **Type:** [[LuaPlayer]]
- **Optional**
The player connected to this character, if any.

### damage_dealt
- **Type:** [[double]]
- **Writable:** [[double]]
The damage dealt by this turret, artillery turret, or artillery wagon.

### kills
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of units killed by this turret, artillery turret, or artillery wagon.

### ignore_unprioritised_targets
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this turret shoots at targets that are not on its priority list.

### last_user
- **Type:** [[LuaPlayer]]
- **Writable:** [[PlayerIdentification]]
- **Optional**
The last player that changed any setting on this entity. This includes building the entity, changing its color, or configuring its circuit network. `nil` if the last user is not part of the save anymore.

### electric_buffer_size
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The buffer size for the electric energy source. `nil` if the entity doesn't have an electric energy source.

Write access is limited to the ElectricEnergyInterface type.

### electric_drain
- **Type:** [[double]]
- **Optional**
The electric drain for the electric energy source. `nil` if the entity doesn't have an electric energy source.

### electric_emissions_per_joule
- **Type:** dictionary<[[string]] → [[double]]>
- **Optional**
The table of emissions of this energy source in `pollution/Joule`, indexed by pollutant type. `nil` if the entity doesn't have an electric energy source. Multiplying values in the returned table by energy consumption in `Watt` gives `pollution/second`.

### unit_number
- **Type:** [[uint64]]
- **Optional**
A unique number identifying this entity for the lifetime of the save. These are allocated sequentially, and not re-used (until overflow).

Only entities inheriting from [[EntityWithOwnerPrototype]], as well as [[ItemRequestProxyPrototype]] and [[EntityGhostPrototype]] are assigned a unit number. Returns `nil` otherwise.

### ghost_unit_number
- **Type:** [[uint64]]
- **Optional**
The [[LuaEntity#unit_number|unit_number]] of the entity contained in this ghost. It is the same as the unit number of the [[EntityWithOwnerPrototype]] that was destroyed to create this ghost. If it was created by other means, or if the inner entity does not support unit numbers, this property is `nil`.

### bonus_mining_progress
- **Type:** [[double]]
- **Writable:** [[double]]
- **Optional**
The bonus mining progress for this mining drill. Read yields a number in range [0, mining_target.prototype.mineable_properties.mining_time]. `nil` if this isn't a mining drill.

### mining_area
- **Type:** [[BoundingBox]]
Area in which this mining drill looks for resources to mine.

### bounding_box
- **Type:** [[BoundingBox]]
[[LuaEntityPrototype#collision_box|LuaEntityPrototype::collision_box]] around entity's given position and respecting the current entity orientation.

### secondary_bounding_box
- **Type:** [[BoundingBox]]
- **Optional**
The secondary bounding box of this entity or `nil` if it doesn't have one. This only exists for curved rails, and is automatically determined by the game.

### selection_box
- **Type:** [[BoundingBox]]
[[LuaEntityPrototype#selection_box|LuaEntityPrototype::selection_box]] around entity's given position and respecting the current entity orientation.

### secondary_selection_box
- **Type:** [[BoundingBox]]
- **Optional**
The secondary selection box of this entity or `nil` if it doesn't have one. This only exists for curved rails, and is automatically determined by the game.

### mining_target
- **Type:** [[LuaEntity]]
- **Optional**
The mining target, if any.

### filter_slot_count
- **Type:** [[uint32]]
The number of filter slots this inserter, loader, mining drill, asteroid collector or logistic storage container has. 0 if not one of those entities.

### loader_container
- **Type:** [[LuaEntity]]
- **Optional**
The container entity this loader is pointing at/pulling from depending on the [[LuaEntity#loader_type|LuaEntity::loader_type]], if any.

### grid
- **Type:** [[LuaEquipmentGrid]]
- **Optional**
This entity's equipment grid, if any.

### graphics_variation
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
- **Optional**
The graphics variation for this entity. `nil` if this entity doesn't use graphics variations.

### tree_color_index
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
Index of the tree color.

### tree_color_index_max
- **Type:** [[uint8]]
Maximum index of the tree colors.

### tree_stage_index
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
Index of the tree stage.

### tree_stage_index_max
- **Type:** [[uint8]]
Maximum index of the tree stages.

### tree_gray_stage_index
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
Index of the tree gray stage

### tree_gray_stage_index_max
- **Type:** [[uint8]]
Maximum index of the tree gray stages.

### burner
- **Type:** [[LuaBurner]]
- **Optional**
The burner energy source for this entity, if any.

### shooting_target
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The shooting target for this turret, if any. Can't be set to `nil` via script.

### proxy_target
- **Type:** [[LuaEntity]]
- **Optional**
The target entity for this item-request-proxy, if any.

### stickers
- **Type:** array<[[LuaEntity]]>
- **Optional**
The sticker entities attached to this entity, if any.

### sticked_to
- **Type:** [[LuaEntity]]
The entity this sticker is sticked to.

### sticker_vehicle_modifiers
- **Type:** table
- **Optional**
The vehicle modifiers applied to this entity through the attached stickers.

### parameters
- **Type:** [[ProgrammableSpeakerParameters]]
- **Writable:** [[ProgrammableSpeakerParameters]]

### alert_parameters
- **Type:** [[ProgrammableSpeakerAlertParameters]]
- **Writable:** [[ProgrammableSpeakerAlertParameters]]

### electric_network_statistics
- **Type:** [[LuaFlowStatistics]]
The electric network statistics for this electric pole.

If this electric pole becomes invalid, the flow statistics obtained from it will also become invalid. If this electric pole becomes part of a different electric network, the flow statistics will be for the new electric network this pole is part of.

### inserter_target_pickup_count
- **Type:** [[uint32]]
Returns the current target pickup count of the inserter.

This considers the circuit network, manual override and the inserter stack size limit based on technology.

### inserter_stack_size_override
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Sets the stack size limit on this inserter.

Set to `0` to reset.

### products_finished
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The number of products this machine finished crafting in its lifetime.

### spawning_cooldown
- **Type:** [[double]]

### absorbed_pollution
- **Type:** [[double]]

### spawn_shift
- **Type:** [[double]]

### units
- **Type:** array<[[LuaEntity]]>
The units associated with this spawner entity.

### power_switch_state
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
The state of this power switch.

### combinator_description
- **Type:** [[string]]
- **Writable:** [[string]]
The description on this combinator.

### effects
- **Type:** [[Effect]]
- **Optional**
The effects being applied to this entity, if any. For beacons, this is the effect the beacon is broadcasting.

### potential_effects
- **Type:** [[Effect]]
- **Optional**
The effects that will be applied to this entity once all upgrades are resolved. Can only be used when the entity has an effect receiver (AssemblingMachine, Furnace, Lab, MiningDrill, AgriculturalTower).

### beacons_count
- **Type:** [[uint32]]
- **Optional**
Number of beacons affecting this effect receiver. Can only be used when the entity has an effect receiver (AssemblingMachine, Furnace, Lab, MiningDrills)

### override_logistic_mode
- **Type:** [[defines.logistic_mode]]
- **Writable:** [[defines.logistic_mode]]
- **Optional**
The override logistic mode being used by this infinity container if it is overridden.

### saved_request_from_buffers
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
The saved request from buffers value if one exists.

The value exists when the infinity container was switched away from having the request from buffers option, for example by changing the [[LuaEntity#override_logistic_mode|logistic mode]] away from requester.

### saved_set_requests
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
The saved set requests value if one exists.

The value exists when the infinity container was switched away from having the set requests option, for example by changing the [[LuaEntity#override_logistic_mode|logistic mode]] away from requester or buffer.

### saved_request_filters
- **Type:** [[SavedLogisticFilters]]
- **Writable:** [[SavedLogisticFilters]]
- **Optional**
The saved logistic requests if they exist.

They exist when the infinity container was switched away from having the option to set logistic requests, for example by changing the [[LuaEntity#override_logistic_mode|logistic mode]] away from requester or buffer.

### saved_storage_filters
- **Type:** [[SavedLogisticFilters]]
- **Writable:** [[SavedLogisticFilters]]
- **Optional**
The saved storage filters if they exist.

They exist when the infinity container was switched away from having the option to set storage filters, for example by changing the [[LuaEntity#override_logistic_mode|logistic mode]] away from storage.

### infinity_container_filters
- **Type:** array<[[InfinityInventoryFilter]]>
- **Writable:** array<[[InfinityInventoryFilter]]>
The filters for this infinity container.

### remove_unfiltered_items
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether items not included in this infinity container filters should be removed from the container.

### character_corpse_player_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The player index associated with this character corpse.

The index is not guaranteed to be valid so it should always be checked first if a player with that index actually exists.

### character_corpse_tick_of_death
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The tick this character corpse died at.

### character_corpse_death_cause
- **Type:** [[LocalisedString]]
- **Writable:** [[LocalisedString]]
The reason this character corpse character died. `""` if there is no reason.

### associated_player
- **Type:** [[LuaPlayer]]
- **Writable:** [[PlayerIdentification]]
- **Optional**
The player this character is associated with, if any. Set to `nil` to clear.

The player will be automatically disassociated when a controller is set on the character. Also, all characters associated to a player will be logged off when the player logs off in multiplayer.

A character associated with a player is not directly controlled by any player.

### tick_of_last_attack
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The last tick this character entity was attacked.

### tick_of_last_damage
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The last tick this character entity was damaged.

### splitter_filter
- **Type:** [[ItemFilter]]
- **Writable:** [[ItemFilter]]
- **Optional**
The filter for this splitter, if any is set.

### inserter_filter_mode
- **Type:** `"whitelist"` | `"blacklist"`
- **Writable:** `"whitelist"` | `"blacklist"`
- **Optional**
The filter mode for this filter inserter. `nil` if this inserter doesn't use filters.

### loader_filter_mode
- **Type:** [[PrototypeFilterMode]]
- **Writable:** [[PrototypeFilterMode]]
- **Optional**
The filter mode for this loader. `nil` if this loader does not support filters.

### loader_belt_stack_size_override
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
The belt stack size override for this loader. Set to `0` to disable. Writing this value requires [[LoaderPrototype#adjustable_belt_stack_size|LoaderPrototype::adjustable_belt_stack_size]] to be `true`.

### mining_drill_filter_mode
- **Type:** `"whitelist"` | `"blacklist"`
- **Writable:** `"whitelist"` | `"blacklist"`
- **Optional**
The filter mode for this mining drill. `nil` if this mining drill doesn't have filters.

### splitter_input_priority
- **Type:** `"left"` | `"none"` | `"right"`
- **Writable:** `"left"` | `"none"` | `"right"`
The input priority for this splitter.

### splitter_output_priority
- **Type:** `"left"` | `"none"` | `"right"`
- **Writable:** `"left"` | `"none"` | `"right"`
The output priority for this splitter.

### inserter_spoil_priority
- **Type:** [[SpoilPriority]]
- **Writable:** [[SpoilPriority]]
The spoil priority for this inserter.

### armed
- **Type:** [[boolean]]
Whether this land mine is armed.

### recipe_locked
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When locked; the recipe in this assembling machine can't be changed by the player.

### connected_rail
- **Type:** [[LuaEntity]]
- **Optional**
The rail entity this train stop is connected to, if any.

### connected_rail_direction
- **Type:** [[defines.rail_direction]]
Rail direction to which this train stop is binding. This returns a value even when no rails are present.

### trains_in_block
- **Type:** [[uint32]]
The number of trains in this rail block for this rail entity.

### timeout
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The timeout that's left on this landmine in ticks. It describes the time between the landmine being placed and it being armed.

### neighbour_bonus
- **Type:** [[double]]
The current total neighbour bonus of this reactor.

### ai_settings
- **Type:** [[LuaAISettings]]
The AI settings of this unit.

### highlight_box_type
- **Type:** [[CursorBoxRenderType]]
- **Writable:** [[CursorBoxRenderType]]
The highlight box type of this highlight box entity.

### highlight_box_blink_interval
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The blink interval of this highlight box entity. `0` indicates no blink.

### status
- **Type:** [[defines.entity_status]]
- **Optional**
The status of this entity, if any.

This is always the actual status of the entity, even if [[LuaEntity#custom_status|LuaEntity::custom_status]] is set.

### custom_status
- **Type:** [[CustomEntityStatus]]
- **Writable:** [[CustomEntityStatus]]
- **Optional**
A custom status for this entity that will be displayed in the GUI.

### enable_logistics_while_moving
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether equipment grid logistics are enabled while this vehicle is moving.

### render_player
- **Type:** [[LuaPlayer]]
- **Writable:** [[PlayerIdentification]]
- **Optional**
The player that this `simple-entity-with-owner`, `simple-entity-with-force`, or `highlight-box` is visible to. `nil` when this entity is rendered for all players.

### render_to_forces
- **Type:** array<[[LuaForce]]>
- **Writable:** [[ForceSet]]
- **Optional**
The forces that this `simple-entity-with-owner` or `simple-entity-with-force` is visible to. `nil` or an empty array when this entity is rendered for all forces.

### pump_input_rail_targets
- **Type:** array<[[LuaEntity]]>
The rail targets of this pump's input

### pump_output_rail_targets
- **Type:** array<[[LuaEntity]]>
The rail targets of this pump's output

### valve_threshold_override
- **Type:** [[float]]
- **Writable:** [[float]]
- **Optional**
The threshold override of this valve, or `nil` if an override is not defined.

If no override is defined, the threshold is taken from [[LuaEntityPrototype#valve_threshold|LuaEntityPrototype::valve_threshold]].

### electric_network_id
- **Type:** [[uint32]]
- **Optional**
Returns the id of the electric network that this entity is connected to, if any.

### electric_network
- **Type:** [[LuaElectricSubNetwork]]
- **Optional**
Electric network this entity is connected to.

This can be used with electric poles, in which case the network will be the same as the one obtained from copper wire connector.

If this entity has an electric energy source, only a primary network will be provided. To also get other networks for entities in range of multiple networks, use [[LuaEntity#electric_networks|LuaEntity::electric_networks]] instead.

### electric_networks
- **Type:** array<[[LuaElectricSubNetwork]]>
- **Optional**
Electric networks this entity with an electric energy source is connected to.

No array is given if this entity has no electric energy source.

Empty array will be given if this entity is not in range of any networks.

Compared to [[LuaEntity#electric_network|LuaEntity::electric_network]], this does not work with electric poles since they do not have an electric energy source and as such can only belong to one network at a time.

### allow_dispatching_robots
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this entity's personal roboports are allowed to dispatch robots.

### energy_generated_last_tick
- **Type:** [[double]]
How much energy this generator generated in the last tick.

### storage_filter
- **Type:** [[ItemIDAndQualityIDPair]]
- **Writable:** [[ItemWithQualityID]]
- **Optional**
The storage filter for this logistic storage container.

Useable only on logistic containers with the `"storage"` [[LuaEntityPrototype#logistic_mode|logistic_mode]].

### request_from_buffers
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this requester chest is set to also request from buffer chests.

Useable only on entities that have requester slots.

### corpse_expires
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this corpse will ever fade away.

### corpse_immune_to_entity_placement
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If true, corpse won't be destroyed when entities are placed over it. If false, whether corpse will be removed or not depends on value of [[CorpsePrototype#remove_on_entity_placement|CorpsePrototype::remove_on_entity_placement]].

### tags
- **Type:** [[Tags]]
- **Writable:** [[Tags]]
- **Optional**
The tags associated with this entity ghost. `nil` if this is not an entity ghost or when the ghost has no tags.

### time_to_next_effect
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The ticks until the next trigger effect of this smoke-with-trigger.

### autopilot_destination
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
- **Optional**
Destination of this spidertron's autopilot, if any. Writing `nil` clears all destinations.

### autopilot_patrol_size
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
When there are this many waypoints left the spider vehicle will start patrolling along them.

Setting this to 0 will disable patrolling.

### autopilot_destinations
- **Type:** array<[[MapPosition]]>
The queued destination positions of spidertron's autopilot.

### trains_count
- **Type:** [[uint32]]
Amount of trains related to this particular train stop. Includes train stopped at this train stop (until it finds a path to next target) and trains having this train stop as goal or waypoint.

Train may be included multiple times when braking distance covers this train stop multiple times.

Value may be read even when train stop has no control behavior.

This value is equal to LuaEntity::train_reservations_count + LuaEntity::script_reservations_count.

### trains_limit
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Amount of trains above which no new trains will be sent to this train stop. Writing nil will disable the limit (will set a maximum possible value).

When a train stop has a control behavior with wire connected and set_trains_limit enabled, this value will be overwritten by it.

### train_reservations_count
- **Type:** [[uint32]]
Amount of train stop reservations taken by trains.

### script_reservations_count
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Amount of train stop reservations taken by script.

### is_military_target
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Whether this entity is a MilitaryTarget. Can be written to if [[LuaEntityPrototype#allow_run_time_change_of_is_military_target|LuaEntityPrototype::allow_run_time_change_of_is_military_target]] returns `true`.

### is_entity_with_owner
- **Type:** [[boolean]]
If this entity is EntityWithOwner

### is_entity_with_health
- **Type:** [[boolean]]
If this entity is EntityWithHealth

### combat_robot_owner
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The owner of this combat robot, if any.

### link_id
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The link ID this linked container is using.

### follow_target
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The follow target of this spidertron, if any.

### follow_offset
- **Type:** [[Vector]]
- **Writable:** [[Vector]]
- **Optional**
The follow offset of this spidertron, if any entity is being followed. This is randomized each time the follow entity is set.

### linked_belt_type
- **Type:** [[BeltConnectionType]]
- **Writable:** [[BeltConnectionType]]
Type of linked belt. Changing type will also flip direction so the belt is out of the same side.

Can only be changed when linked belt is disconnected (has no neighbour set).

### linked_belt_neighbour
- **Type:** [[LuaEntity]]
- **Optional**
Neighbour to which this linked belt is connected to, if any.

May return entity ghost which contains linked belt to which connection is made.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of this entity.

Not all entities support quality and will give the "normal" quality back if they don't.

### rail_layer
- **Type:** [[defines.rail_layer]]
Gets rail layer of a given signal

### radar_scan_progress
- **Type:** [[float]]
The current radar scan progress, as a number in range `[0, 1]`.

### name_tag
- **Type:** [[string]]
- **Writable:** [[string]]
Name tag of this entity. Returns `nil` if entity has no name tag. When name tag is already used by other entity, the name will be removed from the other entity. Entity name tags can also be set in the entity "extra settings" GUI in the map editor.

### rocket_silo_status
- **Type:** [[defines.rocket_silo_status]]
The status of this rocket silo entity.

### tile_width
- **Type:** [[uint32]]
Specifies the tiling size of the entity, is used to decide, if the center should be in the center of the tile (odd tile size dimension) or on the tile border (even tile size dimension). Uses the current direction of the entity.

### tile_height
- **Type:** [[uint32]]
Specifies the tiling size of the entity, is used to decide, if the center should be in the center of the tile (odd tile size dimension) or on the tile border (even tile size dimension). Uses the current direction of the entity.

### crane_end_position_3d
- **Type:** [[Vector3D]]
Returns current position in 3D for the end of the crane of this entity.

### crane_destination
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
Destination of the crane of this entity. Throws when trying to set the destination out of range.

### crane_destination_3d
- **Type:** [[Vector3D]]
- **Writable:** [[Vector3D]]
Destination of the crane of this entity in 3D. Throws when trying to set the destination out of range.

### crane_grappler_destination
- **Writable:** [[MapPosition]]
Will set destination for the grappler of crane of this entity. The crane grappler will start moving to reach the destination, but the rest of the arm will remain stationary. Throws when trying to set the destination out of range.

### crane_grappler_destination_3d
- **Writable:** [[Vector3D]]
Will set destination in 3D for the grappler of crane of this entity. The crane grappler will start moving to reach the destination, but the rest of the arm will remain stationary. Throws when trying to set the destination out of range.

### owned_plants
- **Type:** array<[[LuaEntity]]>
Plants registered by this agricultural tower. One plant can be registered in multiple agricultural towers.

### copy_color_from_train_stop
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this rolling stock has 'copy color from train stop' enabled.

### is_headed_to_trains_front
- **Type:** [[boolean]]
If the rolling stock is facing train's front.

### draw_data
- **Type:** [[RollingStockDrawData]]
Gives a draw data of the given entity if it supports such data.

### train_stop_priority
- **Type:** [[uint8]]
- **Writable:** [[uint8]]
Priority of this train stop.

### belt_shape
- **Type:** `"straight"` | `"left"` | `"right"`
Gives what is the current shape of a transport-belt.

### gps_tag
- **Type:** [[string]]
Returns a [rich text](https://wiki.factorio.com/Rich_text) string containing this entity's position and surface name as a gps tag. [[LuaGameScript#print|Printing]] it will ping the location of the entity.
**Examples:**

```
-- called on a LuaEntity on the default surface it returns:
entity.gps_tag -- => "[gps=-4,-9]"

-- called on a LuaEntity on "custom-surface" it returns:
different_entity.gps_tag -- => "[gps=1,-5,custom-surface]"
```

### commandable
- **Type:** [[LuaCommandable]]
- **Optional**
Returns a LuaCommandable for this entity or nil if entity is not commandable. Units and SpiderUnits are commandable.

### tick_grown
- **Type:** [[MapTick]]
- **Writable:** [[MapTick]]
The tick when this plant is fully grown.

### always_on
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If the lamp is always on when not driven by control behavior.

### artillery_auto_targeting
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this artillery auto-targets enemies.

### robot_order_queue
- **Type:** array<[[WorkerRobotOrder]]>
Get the current queue of robot orders.

### procession_tick
- **Type:** [[MapTick]]
- **Writable:** [[MapTick]]
how far into the current procession the cargo pod is.

### is_updatable
- **Type:** [[boolean]]
Whether the entity is updatable and considered an UpdatableEntity.

### disabled_by_script
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If the updatable entity is disabled by script.

Note: Some entities (Corpse, FireFlame, Roboport, RollingStock, dying entities) need to remain active and will ignore writes.

If this entity is not considered [[LuaEntity#is_updatable|updatable]] then this always returns `false` and writes will be ignored.

### disabled_by_control_behavior
- **Type:** [[boolean]]
If the updatable entity is disabled by control behavior.

Always returns `false` if this entity is not considered [[LuaEntity#is_updatable|updatable]].

### disabled_by_recipe
- **Type:** [[boolean]]
If the assembling machine is disabled by recipe, e.g. due to [[AssemblingMachinePrototype#disabled_when_recipe_not_researched|AssemblingMachinePrototype::disabled_when_recipe_not_researched]].

Always returns `false` if this entity is not considered [[LuaEntity#is_updatable|updatable]].

### is_freezable
- **Type:** [[boolean]]
Whether the entity is freezable and considered a FreezableEntity.

### frozen
- **Type:** [[boolean]]
Whether the freezable entity is currently frozen.

Always returns `false` if this entity is not considered [[LuaEntity#is_freezable|freezable]].

### cargo_hatches
- **Type:** array<[[LuaCargoHatch]]>
The cargo hatches owned by this entity if any.

### cargo_pod_state
- **Type:** `"awaiting_launch"` | `"ascending"` | `"surface_transition"` | `"descending"` | `"parking"`
The state of this cargo pod entity.

### cargo_pod_destination
- **Type:** [[CargoDestination]]
- **Writable:** [[CargoDestination]]
The destination of this cargo pod entity.

Use [[LuaEntity#force_finish_ascending|force_finish_ascending]] if you want it to only descend from orbit.

### cargo_pod_origin
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
The origin of this cargo pod entity. (Must be a silo, hub or pad)

### attached_cargo_pod
- **Type:** [[LuaEntity]]
- **Optional**
The cargo pod attached to this rocket silo rocket if any.

### rocket
- **Type:** [[LuaEntity]]
- **Optional**
The rocket silo rocket this cargo pod is attached to, or rocket silo rocket attached to this rocket silo - if any.

### item_request_proxy
- **Type:** [[LuaEntity]]
- **Optional**
The first found item request proxy targeting this entity.

### base_damage_modifiers
- **Type:** [[TriggerModifierData]]
- **Writable:** [[TriggerModifierData]]

### bonus_damage_modifiers
- **Type:** [[TriggerModifierData]]
- **Writable:** [[TriggerModifierData]]

### cargo_bay_connection_owner
- **Type:** [[LuaEntity]]
- **Optional**
The space platform hub or cargo landing pad this cargo bay is connected to if any.

### pickup_from_left_lane
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
For inserters taking items from transport belt connectables, this determines whether the inserter is allowed to take items from the left lane.

### pickup_from_right_lane
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
For inserters taking items from transport belt connectables, this determines whether the inserter is allowed to take items from the right lane.

### segmented_unit
- **Type:** [[LuaSegmentedUnit]]
- **Optional**
The segmented unit object that the segment entity is a part of.

### pumped_last_tick
- **Type:** [[double]]
The amount of fluid moved by this offshore pump or normal pump in the last tick.

### created_by_corpse
- **Type:** [[LuaEntity]]
- **Optional**
The corpse that caused this entity ghost to be created, if any.

### priority_targets
- **Type:** array<[[LuaEntityPrototype]]>
The priority targets for this turret (if any).

### request_missing_construction_materials
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this space platform hub will automatically make logistic requests for any missing construction materials.

### providing_to_other_platforms
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
If this space platform hub will provide its contents to other requesting platforms.

### local_effect
- **Type:** [[Effect]]
- **Writable:** [[Effect]]
- **Optional**
Additional effect applied to this entity with effect receiver. `nil` if this entity has no effect receiver.

### proxy_target_entity
- **Type:** [[LuaEntity]]
- **Writable:** [[LuaEntity]]
- **Optional**
Entity of which inventory is exposed by this ProxyContainer

### proxy_target_inventory
- **Type:** [[defines.inventory]]
- **Writable:** [[defines.inventory]]
Inventory index of the inventory that is exposed by this ProxyContainer

### display_panel_text
- **Type:** [[string]]
- **Writable:** [[string]]
Text visible on the display panel. Can be written only when it is not set by control behavior.

### display_panel_icon
- **Type:** [[SignalID]]
- **Writable:** [[SignalID]]
- **Optional**
Icon visible on the display panel. Can be written only when it is not set by control behavior.

### display_panel_always_show
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### display_panel_show_in_chart
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### power_production
- **Type:** [[double]]
- **Writable:** [[double]]
The power production specific to the ElectricEnergyInterface entity type.

### power_usage
- **Type:** [[double]]
- **Writable:** [[double]]
The power usage specific to the ElectricEnergyInterface entity type.

### input_flow_limit
- **Type:** [[double]]
- **Writable:** [[double]]
Max amount of energy this ElectricEnergyInterface will take from electric network in one tick.

### output_flow_limit
- **Type:** [[double]]
- **Writable:** [[double]]
Max amount of energy this ElectricEnergyInterface will provide to electric network in one tick.

### electric_interface_mode
- **Type:** [[defines.electric_interface_mode]]
- **Writable:** [[defines.electric_interface_mode]]
Mode this ElectricEnergyInterface is in. Mode changes how the interface interacts with electric network: if its an electric producer, consumer and what priority it has.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_output_inventory
Gets the entity's output inventory if it has one.

**Returns:**
- [[LuaInventory]] *(optional)*: A reference to the entity's output inventory.

### get_module_inventory
Inventory for storing modules of this entity; `nil` if this entity has no module inventory.

**Returns:**
- [[LuaInventory]] *(optional)*

### get_fuel_inventory
The fuel inventory for this entity or `nil` if this entity doesn't have a fuel inventory.

**Returns:**
- [[LuaInventory]] *(optional)*

### get_burnt_result_inventory
The burnt result inventory for this entity or `nil` if this entity doesn't have a burnt result inventory.

**Returns:**
- [[LuaInventory]] *(optional)*

### damage
Damages the entity.
*Only available on:* `EntityWithHealth`

**Parameters:**
- **`damage`** — [[float]]: The amount of damage to be done.
- **`force`** — [[ForceID]]: The force that will be doing the damage.
- **`type`** — [[DamageTypeID]] *(optional)*: The type of damage to be done, defaults to `"impact"`.
- **`source`** — [[LuaEntity]] *(optional)*: The entity that is directly dealing the damage (e.g. the projectile, flame, sticker, grenade, laser beam, etc.). Needs to be on the same surface as the entity being damaged.
- **`cause`** — [[LuaEntity]] *(optional)*: The entity that originally triggered the events that led to this damage being dealt (e.g. the character, turret, enemy, etc. that pulled the trigger). Does not need to be on the same surface as the entity being damaged.

**Returns:**
- [[float]]: the total damage actually applied after resistances.

**Raises:**
- [[on_entity_damaged]] *(timeframe: instantly)*

### can_be_destroyed
Whether the entity can be destroyed

**Returns:**
- [[boolean]]

### destroy
Destroys the entity.

Not all entities can be destroyed - things such as rails under trains cannot be destroyed until the train is moved or destroyed.

Takes a table with the following fields:
- **`do_cliff_correction`** — [[boolean]] *(optional)*: Whether neighbouring cliffs should be corrected. Defaults to `false`.
- **`raise_destroy`** — [[boolean]] *(optional)*: If `true`, [[script_raised_destroy]] will be called. Defaults to `false`.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player whose undo queue this action should be added to.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. Defaults to putting it into the appropriate undo item automatically if not specified.

**Returns:**
- [[boolean]]: Returns `false` if the entity was valid and destruction failed, `true` in all other cases.

**Raises:**
- [[script_raised_destroy]] *(timeframe: instantly)*: Raised if the `raise_destroy` flag was set and the entity was successfully destroyed.

### die
Immediately kills the entity. Does nothing if the entity doesn't have health.

Unlike [[LuaEntity#destroy|LuaEntity::destroy]], `die` will trigger the [[on_entity_died]] event and the entity will produce a corpse and drop loot if it has any.

**Parameters:**
- **`force`** — [[ForceID]] *(optional)*: The force to attribute the kill to.
- **`cause`** — [[LuaEntity]] *(optional)*: The cause to attribute the kill to.

**Returns:**
- [[boolean]]: Whether the entity was successfully killed.

**Raises:**
- [[on_entity_died]] *(timeframe: instantly)*: Raised if the entity was successfully killed. If `force` is not specified, the event will blame the `"neutral"` force.
- [[on_post_entity_died]] *(timeframe: instantly)*: Raised if the entity was successfully killed.

**Examples:**

```
-- This function can be called with only the `cause` argument and no `force`:
entity.die(nil, killer_entity)
```

### has_flag
Test whether this entity's prototype has a certain flag set.

`entity.has_flag(f)` is a shortcut for `entity.prototype.has_flag(f)`.

**Parameters:**
- **`flag`** — [[EntityPrototypeFlag]]: The flag to test.

**Returns:**
- [[boolean]]: `true` if this entity has the given flag set.

### ghost_has_flag
Same as [[LuaEntity#has_flag|LuaEntity::has_flag]], but targets the inner entity on a entity ghost.
*Only available on:* `EntityGhost`

**Parameters:**
- **`flag`** — [[EntityPrototypeFlag]]: The flag to test.

**Returns:**
- [[boolean]]: `true` if the entity has the given flag set.

### add_market_item
Offer a thing on the market.
*Only available on:* `Market`

**Parameters:**
- **`offer`** — [[Offer]]

**Examples:**

```
-- Adds market offer, 1 copper ore for 10 iron ore
market.add_market_item{price={{name = "iron-ore", count = 10}}, offer={type="give-item", item="copper-ore"}}
```

```
-- Adds market offer, 1 copper ore for 5 iron ore and 5 stone ore
market.add_market_item{price={{name = "iron-ore", count = 5}, {name = "stone", count = 5}}, offer={type="give-item", item="copper-ore"}}
```

### remove_market_item
Remove an offer from a market.

The other offers are moved down to fill the gap created by removing the offer, which decrements the overall size of the offer array.
*Only available on:* `Market`

**Parameters:**
- **`offer`** — [[uint32]]: Index of offer to remove.

**Returns:**
- [[boolean]]: `true` if the offer was successfully removed; `false` when the given index was not valid.

### get_market_items
Get all offers in a market as an array.
*Only available on:* `Market`

**Returns:**
- array<[[Offer]]>

### clear_market_items
Removes all offers from a market.
*Only available on:* `Market`

### order_deconstruction
Sets the entity to be deconstructed by construction robots.

**Parameters:**
- **`force`** — [[ForceID]]: The force whose robots are supposed to do the deconstruction.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to, if any. Also the player whose undo queue this action should be added to.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. An index of `1` adds the action to the latest undo action on the stack. Defaults to putting it into the appropriate undo item automatically if one is not specified.

**Returns:**
- [[boolean]]: if the entity was marked for deconstruction.

**Raises:**
- [[on_marked_for_deconstruction]] *(timeframe: instantly)*: Raised if the entity was successfully marked for deconstruction.

### cancel_deconstruction
Cancels deconstruction if it is scheduled, does nothing otherwise.

**Parameters:**
- **`force`** — [[ForceID]]: The force who did the deconstruction order.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the `last_user` to if any.

**Raises:**
- [[on_cancelled_deconstruction]] *(timeframe: instantly)*: Raised if the entity's deconstruction was successfully cancelled.

### to_be_deconstructed
Is this entity marked for deconstruction?

**Returns:**
- [[boolean]]

### order_upgrade
Sets the entity to be upgraded by construction robots.

Takes a table with the following fields:
- **`target`** — [[EntityWithQualityID]]: The prototype of the entity to upgrade to.
- **`force`** — [[ForceID]]: The force whose robots are supposed to do the upgrade.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player whose undo queue this action should be added to.
- **`undo_index`** — [[uint32]] *(optional)*: The index of the undo item to add this action to. An index of `0` creates a new undo item for it. Defaults to putting it into the appropriate undo item automatically if not specified.

**Returns:**
- [[boolean]]: Whether the entity was marked for upgrade.

**Raises:**
- [[on_marked_for_upgrade]] *(timeframe: instantly)*: Raised if the entity was successfully marked for upgrade.

### cancel_upgrade
Cancels upgrade if it is scheduled, does nothing otherwise.

**Parameters:**
- **`force`** — [[ForceID]]: The force who did the upgrade order.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.

**Returns:**
- [[boolean]]: Whether the cancel was successful.

**Raises:**
- [[on_cancelled_upgrade]] *(timeframe: instantly)*: Raised if the entity was previously marked for upgrade.

### to_be_upgraded
Is this entity marked for upgrade?

**Returns:**
- [[boolean]]

### apply_upgrade
Upgrades this entity in place if it's marked to be upgraded.

**Parameters:**
- **`override_target`** — [[EntityWithQualityID]] *(optional)*: The override upgrade target - used instead of the entities current upgrade target if given. Note, the entity must be fast-replaceable with the override target, or it won't be upgraded.
- **`buffer`** — [[LuaInventory]] *(optional)*: If provided - any items left over from the upgrade are put into this inventory.

**Returns:**
- [[LuaEntity]] *(optional)*: The first upgraded entity - `nil` if this entity is not marked for upgrade.
- [[LuaEntity]] *(optional)*: When upgrading underground belts, the other underground belt end that was also upgraded - `nil` if this entity is not marked for upgrade.

**Raises:**
- [[script_raised_built]] *(timeframe: instantly)*: Raised for the new entity if the entity was actually upgraded.
- [[script_raised_destroy]] *(timeframe: instantly)*: Raised for the old entity if the entity was actually upgraded.

### is_crafting
Returns whether a craft is currently in process. It does not indicate whether progress is currently being made, but whether a crafting process has been started in this machine.
*Only available on:* `CraftingMachine`

**Returns:**
- [[boolean]]

### is_opened
*Only available on:* `Gate`

**Returns:**
- [[boolean]]: `true` if this gate is currently opened.

### is_opening
*Only available on:* `Gate`

**Returns:**
- [[boolean]]: `true` if this gate is currently opening.

### is_closed
*Only available on:* `Gate`

**Returns:**
- [[boolean]]: `true` if this gate is currently closed.

### is_closing
*Only available on:* `Gate`

**Returns:**
- [[boolean]]: `true` if this gate is currently closing

### request_to_open
*Only available on:* `Gate`

**Parameters:**
- **`force`** — [[ForceID]]: The force that requests the gate to be open.
- **`extra_time`** — [[uint32]] *(optional)*: Extra ticks to stay open.

### request_to_close
*Only available on:* `Gate`

**Parameters:**
- **`force`** — [[ForceID]]: The force that requests the gate to be closed.

### get_transport_line
Get a transport line of a belt or belt connectable entity.
*Only available on:* `TransportBeltConnectable`

**Parameters:**
- **`index`** — [[defines.transport_line]]: Index of the requested transport line. Transport lines are 1-indexed.

**Returns:**
- [[LuaTransportLine]]

### get_item_insert_specification
Get an item insert specification onto a belt connectable: for a given map position provides into which line at what position item should be inserted to be closest to the provided position.
*Only available on:* `TransportBeltConnectable`

**Parameters:**
- **`position`** — [[MapPosition]]: Position where the item is to be inserted.
- **`mirrored`** — [[boolean]] *(optional)*: When inserting at position exactly in between lines, mirroring is used to choose line.

**Returns:**
- [[uint32]]: Index of the transport line that is closest to the provided map position.
- [[float]]: Position along the transport line where item should be dropped.

### get_line_item_position
Get a map position related to a position on a transport line.
*Only available on:* `TransportBeltConnectable`

**Parameters:**
- **`index`** — [[defines.transport_line]]: Index of the transport line. Transport lines are 1-indexed.
- **`position`** — [[float]]: Linear position along the transport line. Clamped to the transport line range.

**Returns:**
- [[MapPosition]]

### get_max_transport_line_index
Get the maximum transport line index of a belt or belt connectable entity.
*Only available on:* `TransportBeltConnectable`

**Returns:**
- [[defines.transport_line]]

### launch_rocket
*Only available on:* `RocketSilo`

**Parameters:**
- **`destination`** — [[CargoDestination]] *(optional)*
- **`character`** — [[LuaEntity]] *(optional)*: If provided, must be of `character` type.

**Returns:**
- [[boolean]]: `true` if the rocket was successfully launched. Return value of `false` means the silo is not ready for launch.

**Raises:**
- [[on_rocket_launch_ordered]] *(timeframe: instantly)*: Raised if the rocket launch was successfully initiated.

### revive
Revive a ghost, which turns it from a ghost into a real entity or tile.
*Only available on:* `Ghost`

Takes a table with the following fields:
- **`raise_revive`** — [[boolean]] *(optional)*: If true, and an entity ghost; [[script_raised_revive]] will be called. Else if true, and a tile ghost; [[script_raised_set_tiles]] will be called.
- **`overflow`** — [[LuaInventory]] *(optional)*: Items that would be deleted will be transferred to this inventory. Must be a script inventory or inventory of other entity. Inventory references obtained from proxy container are not allowed.

**Returns:**
- array<[[ItemWithQualityCount]]> *(optional)*: Any items the new real entity collided with or `nil` if the ghost could not be revived.
- [[LuaEntity]] *(optional)*: The revived entity if an entity ghost was successfully revived.
- [[LuaEntity]] *(optional)*: The item request proxy if one was created.

**Raises:**
- [[script_raised_revive]] *(timeframe: instantly)*: Raised if this was an entity ghost and the `raise_revive` flag was set and the entity was successfully revived.
- [[script_raised_set_tiles]] *(timeframe: instantly)*: Raised if this was a tile ghost and the `raise_revive` flag was set and the tile was successfully revived.

### silent_revive
Revives a ghost silently, so the revival makes no sound and no smoke is created.
*Only available on:* `Ghost`

Takes a table with the following fields:
- **`raise_revive`** — [[boolean]] *(optional)*: If true, and an entity ghost; [[script_raised_revive]] will be called. Else if true, and a tile ghost; [[script_raised_set_tiles]] will be called.
- **`overflow`** — [[LuaInventory]] *(optional)*: Items that would be deleted will be transferred to this inventory. Must be a script inventory or inventory of other entity. Inventory references obtained from proxy container are not allowed.

**Returns:**
- array<[[ItemWithQualityCount]]>: Any items the new real entity collided with or `nil` if the ghost could not be revived.
- [[LuaEntity]] *(optional)*: The revived entity if an entity ghost was successfully revived.
- [[LuaEntity]] *(optional)*: The item request proxy if one was created.

**Raises:**
- [[script_raised_revive]] *(timeframe: instantly)*: Raised if this was an entity ghost and the `raise_revive` flag was set and the entity was successfully revived.
- [[script_raised_set_tiles]] *(timeframe: instantly)*: Raised if this was a tile ghost and the `raise_revive` flag was set and the tile was successfully revived.

### get_connected_rail
*Only available on:* `Rail`

Takes a table with the following fields:
- **`rail_direction`** — [[defines.rail_direction]]
- **`rail_connection_direction`** — [[defines.rail_connection_direction]]

**Returns:**
- [[LuaEntity]] *(optional)*: Rail connected in the specified manner to this one, `nil` if unsuccessful.
- [[defines.rail_direction]] *(optional)*: Rail direction of the returned rail which points to origin rail
- [[defines.rail_connection_direction]] *(optional)*: Turn to be taken when going back from returned rail to origin rail

### get_connected_rails
Get the rails that this signal is connected to.
*Only available on:* `RailSignal`, `RailChainSignal`

**Returns:**
- array<[[LuaEntity]]>

### get_rail_segment_signal
Get the rail signal at the start/end of the rail segment this rail is in.

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]: The direction of travel relative to this rail.
- **`in_else_out`** — [[boolean]]: If true, gets the signal at the entrance of the rail segment, otherwise gets the signal at the exit of the rail segment.

**Returns:**
- [[LuaEntity]] *(optional)*: `nil` if the rail segment doesn't start/end with a signal.

### get_rail_segment_stop
Get train stop at the start/end of the rail segment this rail is in.

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]: The direction of travel relative to this rail.

**Returns:**
- [[LuaEntity]] *(optional)*: `nil` if the rail segment doesn't start/end with a train stop.

### get_rail_segment_end
Get the rail at the end of the rail segment this rail is in.

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[LuaEntity]]: The rail entity.
- [[defines.rail_direction]]: A rail direction pointing out of the rail segment from the end rail.

### get_rail_segment_rails
Get all rails of a rail segment this rail is in

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]: Selects end of this rail that points to a rail segment end from which to start returning rails

**Returns:**
- array<[[LuaEntity]]>: Rails of this rail segment

### get_rail_segment_length
Get the length of the rail segment this rail is in.

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Returns:**
- [[double]]

### get_rail_segment_overlaps
Get a rail from each rail segment that overlaps with this rail's rail segment.

A rail segment is a continuous section of rail with no branches, signals, nor train stops.
*Only available on:* `Rail`

**Returns:**
- array<[[LuaEntity]]>

### is_rail_in_same_rail_segment_as
Checks if this rail and other rail both belong to the same rail segment.
*Only available on:* `Rail`

**Parameters:**
- **`other_rail`** — [[LuaEntity]]

**Returns:**
- [[boolean]]

### is_rail_in_same_rail_block_as
Checks if this rail and other rail both belong to the same rail block.
*Only available on:* `Rail`

**Parameters:**
- **`other_rail`** — [[LuaEntity]]

**Returns:**
- [[boolean]]

### get_parent_signals
Returns all parent signals. Parent signals are always RailChainSignal. Parent signals are those signals that are checking state of this signal to determine their own chain state.
*Only available on:* `RailSignal`, `RailChainSignal`

**Returns:**
- array<[[LuaEntity]]>

### get_child_signals
Returns all child signals. Child signals can be either RailSignal or RailChainSignal. Child signals are signals which are checked by this signal to determine a chain state.
*Only available on:* `RailChainSignal`

**Returns:**
- array<[[LuaEntity]]>

### get_inbound_signals
Returns all signals guarding entrance to a rail block this rail belongs to.
*Only available on:* `Rail`

**Returns:**
- array<[[LuaEntity]]>

### get_outbound_signals
Returns all signals guarding exit from a rail block this rail belongs to.
*Only available on:* `Rail`

**Returns:**
- array<[[LuaEntity]]>

### get_filter
Get the filter for a slot in an inserter, loader, mining drill, asteroid collector, or logistic storage container. The entity must allow filters.

**Parameters:**
- **`slot_index`** — [[uint32]]: Index of the slot to get the filter for.

**Returns:**
- [[ItemFilter]] | [[EntityID]] | [[AsteroidChunkID]] *(optional)*: The filter, or `nil` if the given slot has no filter.

### set_filter
Set the filter for a slot in an inserter (ItemFilter), loader (ItemFilter), mining drill (EntityID), asteroid collector (AsteroidChunkID) or logistic storage container (ItemWithQualityID). The entity must allow filters.

**Parameters:**
- **`index`** — [[uint32]]: Index of the slot to set the filter for.
- **`filter`** — [[ItemFilter]] | [[ItemWithQualityID]] | [[EntityID]] | [[AsteroidChunkID]] *(optional)*: The item or entity to filter, or `nil` to clear the filter.

### get_infinity_container_filter
Gets the filter for this infinity container at the given index, or `nil` if the filter index doesn't exist or is empty.
*Only available on:* `InfinityContainer`, `InfinityCargoWagon`

**Parameters:**
- **`index`** — [[uint32]]: The index to get.

**Returns:**
- [[InfinityInventoryFilter]] *(optional)*

### set_infinity_container_filter
Sets the filter for this infinity container at the given index.
*Only available on:* `InfinityContainer`, `InfinityCargoWagon`

**Parameters:**
- **`index`** — [[uint32]]: The index to set.
- **`filter`** — [[InfinityInventoryFilter]] | [[nil]]: The new filter, or `nil` to clear the filter.

### get_infinity_pipe_filter
Gets the filter for this infinity pipe, or `nil` if the filter is empty.
*Only available on:* `InfinityPipe`

**Returns:**
- [[InfinityPipeFilter]] *(optional)*

### set_infinity_pipe_filter
Sets the filter for this infinity pipe.
*Only available on:* `InfinityPipe`

**Parameters:**
- **`filter`** — [[InfinityPipeFilter]] | [[nil]]: The new filter, or `nil` to clear the filter.

### get_heat_setting
Gets the heat setting for this heat interface.
*Only available on:* `HeatInterface`

**Returns:**
- [[HeatSetting]]

### set_heat_setting
Sets the heat setting for this heat interface.
*Only available on:* `HeatInterface`

**Parameters:**
- **`filter`** — [[HeatSetting]]: The new setting.

### get_control_behavior
Gets the control behavior of the entity (if any).

**Returns:**
- [[LuaControlBehavior]] *(optional)*: The control behavior or `nil`.

### get_or_create_control_behavior
Gets (and or creates if needed) the control behavior of the entity.

**Returns:**
- [[LuaControlBehavior]] *(optional)*: The control behavior or `nil`.

### get_circuit_network

**Parameters:**
- **`wire_connector_id`** — [[defines.wire_connector_id]]: Wire connector to get circuit network for.

**Returns:**
- [[LuaCircuitNetwork]] *(optional)*: The circuit network or nil.

### get_signal
Read a single signal from the selected wire connector

**Parameters:**
- **`signal`** — [[SignalID]]: The signal to read.
- **`wire_connector_id`** — [[defines.wire_connector_id]]: Wire connector ID from which to get the signal
- **`extra_wire_connector_id`** — [[defines.wire_connector_id]] *(optional)*: Additional wire connector ID. If specified, signal will be added to the result

**Returns:**
- [[int32]]: The current value of the signal.

### get_signals
Read all signals from the selected wire connector.

**Parameters:**
- **`wire_connector_id`** — [[defines.wire_connector_id]]: Wire connector ID from which to get the signal
- **`extra_wire_connector_id`** — [[defines.wire_connector_id]] *(optional)*: Additional wire connector ID. If specified, signals will be added to the result

**Returns:**
- array<[[Signal]]> *(optional)*: Current values of all signals.

### get_signals_changed
Checks if signals on a circuit connector changed recently.

Returns `true` if signals changed since last tick. If a tick of last check is provided, returns `true` if signals changed since the specified tick. May also return `true` spuriously in other situations when values seen on this connector may be different, caused by addition of wires, removal of wires, circuit network merges, circuit network splits, input network selection changes, etc.

`nil` if entity has no circuit connector with provided identifier.

**Parameters:**
- **`wire_connector_id`** — [[defines.wire_connector_id]]
- **`tick_of_last_check`** — [[MapTick]] *(optional)*: Value of [[LuaGameScript#tick|LuaGameScript::tick]] of the previous check.

**Returns:**
- [[boolean]] *(optional)*

### supports_backer_name
Whether this entity supports a backer name.

**Returns:**
- [[boolean]]

### copy_settings
Copies settings from the given entity onto this entity.

**Parameters:**
- **`entity`** — [[LuaEntity]]
- **`by_player`** — [[PlayerIdentification]] *(optional)*: If provided, the copying is done 'as' this player and [[on_entity_settings_pasted]] is triggered.

**Returns:**
- array<[[ItemWithQualityCount]]>: Any items removed from this entity as a result of copying the settings.

### get_logistic_point
Gets all the `LuaLogisticPoint`s that this entity owns. Optionally returns only the point specified by the index parameter.

**Parameters:**
- **`index`** — [[defines.logistic_member_index]] *(optional)*: If provided, this method only returns the `LuaLogisticPoint` specified by this index, or `nil` if it doesn't exist.

**Returns:**
- [[LuaLogisticPoint]] | array<[[LuaLogisticPoint]]> *(optional)*

### play_note
Plays a note with the given instrument and note.
*Only available on:* `ProgrammableSpeaker`

**Parameters:**
- **`instrument`** — [[uint32]]
- **`note`** — [[uint32]]
- **`stop_playing_sounds`** — [[boolean]] *(optional)*

**Returns:**
- [[boolean]]: Whether the request is valid. The sound may or may not be played depending on polyphony settings.

### connect_rolling_stock
Connects the rolling stock in the given direction.
*Only available on:* `RollingStock`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[boolean]]: Whether any connection was made

### disconnect_rolling_stock
Tries to disconnect this rolling stock in the given direction.
*Only available on:* `RollingStock`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[boolean]]: If anything was disconnected

### update_connections
Reconnect loader, beacon, cliff and mining drill connections to entities that might have been teleported out or in by the script. The game doesn't do this automatically as we don't want to lose performance by checking this in normal games.

### get_recipe
Current recipe being assembled by this machine, if any.
*Only available on:* `CraftingMachine`

**Returns:**
- [[LuaRecipe]] *(optional)*
- [[LuaQualityPrototype]] *(optional)*

### set_recipe
Sets the given recipe in this assembly machine.
*Only available on:* `AssemblingMachine`

**Parameters:**
- **`recipe`** — [[RecipeID]] *(optional)*: The new recipe. Writing `nil` clears the recipe, if any.
- **`quality`** — [[QualityID]] *(optional)*: The quality. If not provided `normal` is used.

**Returns:**
- array<[[ItemWithQualityCount]]>: Any items removed from this entity as a result of setting the recipe.

### rotate
Rotates this entity as if the player rotated it.

Takes a table with the following fields:
- **`reverse`** — [[boolean]] *(optional)*: If `true`, rotate the entity in the counter-clockwise direction.
- **`by_player`** — [[PlayerIdentification]] *(optional)*

**Returns:**
- [[boolean]]: Whether the rotation was successful.

**Raises:**
- [[on_player_rotated_entity]] *(timeframe: instantly)*: Raised if the `by_player` argument was given and the rotation was successful.

### flip
Flips this entity

Takes a table with the following fields:
- **`horizontal`** — [[boolean]]
- **`by_player`** — [[PlayerIdentification]] *(optional)*

**Returns:**
- [[boolean]]: Whether the flip was successful.

**Raises:**
- [[on_player_flipped_entity]] *(timeframe: instantly)*: Raised if the `by_player` argument was given and the flip was successful.

### get_driver
Gets the driver of this vehicle if any.
*Only available on:* `Vehicle`

**Returns:**
- [[LuaEntity]] | [[LuaPlayer]] *(optional)*: `nil` if the vehicle contains no driver. To check if there's a passenger see [[LuaEntity#get_passenger|LuaEntity::get_passenger]].

### set_driver
Sets the driver of this vehicle.

This differs from [[LuaEntity#set_passenger|LuaEntity::set_passenger]] in that the passenger can't drive the vehicle.
*Only available on:* `Vehicle`

**Parameters:**
- **`driver`** — [[LuaEntity]] | [[PlayerIdentification]] | [[nil]]: The new driver. Writing `nil` ejects the current driver, if any.

**Raises:**
- [[on_player_driving_changed_state]] *(timeframe: instantly)*

### get_passenger
Gets the passenger of this car, spidertron, or cargo pod if any.

This differs over [[LuaEntity#get_driver|LuaEntity::get_driver]] in that for cars, the passenger can't drive the car.
*Only available on:* `Car`, `SpiderVehicle`, `CargoPod`

**Returns:**
- [[LuaEntity]] | [[LuaPlayer]] *(optional)*: `nil` if the vehicle contains no passenger. To check if there's a driver see [[LuaEntity#get_driver|LuaEntity::get_driver]].

### set_passenger
Sets the passenger of this car, spidertron, or cargo pod.

This differs from [[LuaEntity#get_driver|LuaEntity::get_driver]] in that the passenger can't drive the car.
*Only available on:* `Car`, `SpiderVehicle`, `CargoPod`

**Parameters:**
- **`passenger`** — [[LuaEntity]] | [[PlayerIdentification]] | [[nil]]: The new passenger. Writing `nil` ejects the current passenger, if any.

**Raises:**
- [[on_player_driving_changed_state]] *(timeframe: instantly)*

### is_connected_to_electric_network
Returns `true` if this entity produces or consumes electricity and is connected to an electric network that has at least one entity that can produce power.

**Returns:**
- [[boolean]]

### get_train_stop_trains
The trains scheduled to stop at this train stop.
*Only available on:* `TrainStop`

**Returns:**
- array<[[LuaTrain]]>

### get_stopped_train
The train currently stopped at this train stop, if any.
*Only available on:* `TrainStop`

**Returns:**
- [[LuaTrain]] *(optional)*

### clone
Clones this entity.

Takes a table with the following fields:
- **`position`** — [[MapPosition]]: The destination position
- **`surface`** — [[LuaSurface]] *(optional)*: The destination surface
- **`force`** — [[ForceID]] *(optional)*
- **`create_build_effect_smoke`** — [[boolean]] *(optional)*: If false, the building effect smoke will not be shown around the new entity.

**Returns:**
- [[LuaEntity]] *(optional)*: The cloned entity or `nil` if this entity can't be cloned/can't be cloned to the given location.

**Raises:**
- [[on_entity_cloned]] *(timeframe: instantly)*: Raised if the entity was successfully cloned.

### get_fluid_count
Get the amount of all or some fluid in this entity.

If information about fluid temperatures is required, [[LuaEntity#get_fluid|LuaEntity::get_fluid]] should be used instead.

**Parameters:**
- **`fluid`** — [[string]] *(optional)*: Prototype name of the fluid to count. If not specified, count all fluids.

**Returns:**
- [[FluidAmount]]

### get_fluid_contents
Get amounts of all fluids in this entity.

If information about fluid temperatures is required, [[LuaEntity#get_fluid|LuaEntity::get_fluid]] should be used instead.

**Returns:**
- dictionary<[[string]] → [[FluidAmount]]>: The amounts, indexed by fluid names.

### clear_fluids
Clears all fluids in this entity but will not clear fluids in any fluid segments fluidboxes may be part of.

**Returns:**
- array<[[Fluid]]>: The fluids removed.

### get_fluid
Gets the fluid in the entity's given fluid storage if one exists.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[Fluid]] *(optional)*: The fluid in this storage. `nil` if fluid storage is empty.

### set_fluid
Sets the fluid in the entity's given fluid storage to the provided fluid if possible.

Fluid filters may block setting the fluid, or less fluid may be set if it's more than the maximum capacity.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`fluid`** — [[Fluid]]

**Returns:**
- [[FluidAmount]]: How much of the given fluid was actually set.

### add_fluid
Adds the given fluid to the entity's given fluid storage if possible.

If the current fluid conflicts or the current filter conflicts the fluid may not be added.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`fluid`** — [[Fluid]]

**Returns:**
- [[FluidAmount]]: The amount of fluid added.

### remove_fluid
Removes the given fluid amount from the entity's given fluid storage if possible.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`amount`** — [[FluidAmount]]

**Returns:**
- [[Fluid]] *(optional)*: The fluid removed.

### clear_fluid
Removes all fluid from the entity's given fluid storage if possible.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[Fluid]] *(optional)*: The fluid cleared.

### get_fluid_filter
Get a fluidbox filter, such as the filter of a pump.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[LuaFluidPrototype]] *(optional)*

### set_fluid_filter
Set a fluidbox filter, such as the filter of a pump.

Some entities cannot have their fluidbox filter set, notably fluid wagons and crafting machines.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`filter`** — [[FluidID]] *(optional)*

**Returns:**
- [[boolean]]: Whether the filter was set.

### get_fluid_capacity
Gets the maximum capacity of the entity's given fluid storage.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[FluidAmount]]

### get_fluid_box_prototype
The prototype of the entity's given fluid storage if one exists. If this is used on a fluidbox of a crafting machine which due to recipe was created by merging multiple prototypes, a table of prototypes that were merged will be returned instead For storages on entities that have fluid storage but no prototype for those storages (fluid wagons, and fluid turrets) this returns `nil`.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[LuaFluidBoxPrototype]] | array<[[LuaFluidBoxPrototype]]> *(optional)*

### get_fluid_box_neighbours
The entities the given fluidbox is connected to.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- array<[[FluidBoxNeighbourRecord]]> *(optional)*

### get_fluid_box_pipe_connections
Get the given connections and associated data of the fluidbox.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- array<[[PipeConnection]]> *(optional)*

### add_fluid_box_linked_connection
Registers a linked fluidbox connection between this entity and other entity. Because entity may have multiple fluidboxes, each with multiple connections that could be linked, a unique value for this and other linked_connection_id may need to be given.

It may happen a linked fluidbox connection is not established immediately due to crafting machines being possible to not have certain fluidboxes exposed at a given point in time, but once they appear (due to recipe changes that would use them) they will be linked. Linked connections are persisted as (this_entity, this_linked_connection_id, other_entity, other_linked_connection_id) so if a pipe connection definition's value of linked_connection_id changes existing connections may not restore correct connections.

Every fluidbox connection that was defined in prototypes as connection_type=="linked" may be linked to at most 1 other fluidbox. When trying to connect already used connection, previous connection will be removed.

Linked connections cannot go to the same entity even if they would be part of other fluidbox.

**Parameters:**
- **`this_linked_connection_id`** — [[uint32]]
- **`other_entity`** — [[LuaEntity]]
- **`other_linked_connection_id`** — [[uint32]]

### remove_fluid_box_linked_connection
Removes linked fluidbox connection record. If connected, other end will be also removed.

**Parameters:**
- **`this_linked_connection_id`** — [[uint32]]

### get_fluid_box_linked_connection
Returns other end of a linked fluidbox connection.

**Parameters:**
- **`this_linked_connection_id`** — [[uint32]]

**Returns:**
- [[LuaEntity]] *(optional)*: Other entity to which a linked fluidbox connection was made
- [[uint32]] *(optional)*: linked_connection_id on other entity

### get_fluid_box_linked_connections
Returns list of all linked fluidbox connections registered for this entity.

**Returns:**
- array<[[FluidBoxConnectionRecord]]>

### has_fluid_segment
Whether the given fluid storage has a fluid segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[boolean]]

### get_fluid_segment_fluid
The fluid within the given storage's fluid segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[Fluid]] *(optional)*

### set_fluid_segment_fluid
Sets the fluid within the given storage's fluid segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`fluid`** — [[Fluid]]

**Returns:**
- [[FluidAmount]]: The amount of fluid set.

### add_fluid_segment_fluid
Adds the given fluid to the given storage's fluid segment if possible.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`fluid`** — [[Fluid]]

**Returns:**
- [[FluidAmount]]: The amount of fluid added.

### clear_fluid_segment_fluid
Clears the given fluid storage's fluid segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[Fluid]] *(optional)*: The fluid cleared.

### remove_fluid_segment_fluid
Removes the given fluid amount from the given storage's fluid segment if possible.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]
- **`amount`** — [[FluidAmount]]

**Returns:**
- [[Fluid]] *(optional)*: The fluid removed.

### get_fluid_segment_filter
Gets the filter of the given fluid storage's segment. The filter is based on the filters set on the fluidboxes of the segment, so it can't be set directly on the segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[LuaFluidPrototype]] *(optional)*

### get_fluid_segment_capacity
Gets the maximum capacity of the given fluid storage's segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[FluidAmount]]

### get_fluid_segment_extent_bounding_box
Gets the current extent bounding box of of the given fluid storage's segment.

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[BoundingBox]]

### get_fluid_segment_id

**Parameters:**
- **`index`** — [[FluidStorageIndex]]

**Returns:**
- [[uint32]]

### insert_fluid
Insert fluid into this entity. Fluidbox is chosen automatically.

**Parameters:**
- **`fluid`** — [[Fluid]]: Fluid to insert.

**Returns:**
- [[FluidAmount]]: Amount of fluid actually inserted.

### extract_fluid
Remove fluid from this entity.

If temperature is given only fluid matching that exact temperature is removed. If minimum and maximum is given fluid within that range is removed.

Takes a table with the following fields:
- **`name`** — [[string]]: Fluid prototype name.
- **`amount`** — [[FluidAmount]]: Amount to remove
- **`minimum_temperature`** — [[double]] *(optional)*
- **`maximum_temperature`** — [[double]] *(optional)*
- **`temperature`** — [[double]] *(optional)*

**Returns:**
- [[FluidAmount]]: Amount of fluid actually removed.

### clear_fluid_inside
Remove all fluids from this entity and connected fluid segments.

### get_beam_source
Get the source of this beam.
*Only available on:* `Beam`

**Returns:**
- [[BeamTarget]] *(optional)*

### set_beam_source
Set the source of this beam.
*Only available on:* `Beam`

**Parameters:**
- **`source`** — [[LuaEntity]] | [[MapPosition]]

### get_beam_target
Get the target of this beam.
*Only available on:* `Beam`

**Returns:**
- [[BeamTarget]] *(optional)*

### set_beam_target
Set the target of this beam.
*Only available on:* `Beam`

**Parameters:**
- **`target`** — [[LuaEntity]] | [[MapPosition]]

### get_radius
The radius of this entity. The radius is defined as half the distance between the top left corner and bottom right corner of the collision box.

**Returns:**
- [[double]]

### get_health_ratio
The health ratio of this entity between 1 and 0 (for full health and no health respectively).

**Returns:**
- [[float]] *(optional)*: `nil` if this entity doesn't have health.

### create_build_effect_smoke
Creates the same smoke that is created when you place a building by hand.

You can play the building sound to go with it by using [[LuaSurface#play_sound|LuaSurface::play_sound]], eg: `entity.surface.play_sound{path="entity-build/"..entity.prototype.name, position=entity.position}`

### release_from_spawner
Release the unit from the spawner which spawned it. This allows the spawner to continue spawning additional units.
*Only available on:* `Unit`, `SpiderUnit`

### toggle_equipment_movement_bonus
Toggle this entity's equipment movement bonus. Does nothing if the entity does not have an equipment grid.

This property can also be read and written on the equipment grid of this entity.

### can_shoot
Whether this character can shoot the given entity or position.
*Only available on:* `Character`

**Parameters:**
- **`target`** — [[LuaEntity]]
- **`position`** — [[MapPosition]]

**Returns:**
- [[boolean]]

### start_fading_out
Only works if the entity is a speech-bubble, with an "effect" defined in its wrapper_flow_style. Starts animating the opacity of the speech bubble towards zero, and destroys the entity when it hits zero.
*Only available on:* `SpeechBubble`

### get_upgrade_target
Returns the new entity prototype and its quality.

**Returns:**
- [[LuaEntityPrototype]] *(optional)*: `nil` if this entity is not marked for upgrade.
- [[LuaQualityPrototype]] *(optional)*: `nil` if this entity is not marked for upgrade.

### get_damage_to_be_taken
Returns the amount of damage to be taken by this entity.

**Returns:**
- [[float]] *(optional)*: `nil` if this entity does not have health.

### deplete
Depletes and destroys this resource entity.
*Only available on:* `ResourceEntity`

**Raises:**
- [[on_resource_depleted]] *(timeframe: instantly)*

### mine
Mines this entity.

'Standard' operation is to keep calling `LuaEntity.mine` with an inventory until all items are transferred and the items dealt with.

The result of mining the entity (the item(s) it produces when mined) will be dropped on the ground if they don't fit into the provided inventory. If no inventory is provided, the items will be destroyed.

Takes a table with the following fields:
- **`inventory`** — [[LuaInventory]] *(optional)*: If provided the item(s) will be transferred into this inventory. If provided, this must be an inventory created with [[LuaGameScript#create_inventory|LuaGameScript::create_inventory]] or be a basic inventory owned by some entity.
- **`force`** — [[boolean]] *(optional)*: If true, when the item(s) don't fit into the given inventory the entity is force mined. If false, the mining operation fails when there isn't enough room to transfer all of the items into the inventory. Defaults to false. This is ignored and acts as `true` if no inventory is provided.
- **`raise_destroyed`** — [[boolean]] *(optional)*: If true, [[script_raised_destroy]] will be raised. Defaults to `true`.
- **`ignore_minable`** — [[boolean]] *(optional)*: If true, the minable state of the entity is ignored. Defaults to `false`. If false, an entity that isn't minable (set as not-minable in the prototype or isn't minable for other reasons) will fail to be mined.

**Returns:**
- [[boolean]]: Whether mining succeeded.

**Raises:**
- [[script_raised_destroy]] *(timeframe: instantly)*: Raised if the `raise_destroyed` flag was set and the entity was successfully mined.

### spawn_decorations
Triggers spawn_decoration actions defined in the entity prototype or does nothing if entity is not "turret" or "unit-spawner".

### get_priority_target
Get the entity ID at the specified position in the turret's priority list.

**Parameters:**
- **`index`** — [[uint32]]: The index of the entry to fetch.

**Returns:**
- [[LuaEntityPrototype]] *(optional)*

### set_priority_target
Set the entity ID name at the specified position in the turret's priority list.

**Parameters:**
- **`index`** — [[uint32]]: The index of the entry to set.
- **`entity_id`** — [[EntityID]] *(optional)*: The name of the entity prototype, or `nil` to clear the entry.

### can_wires_reach
Can wires reach between these entities.

**Parameters:**
- **`entity`** — [[LuaEntity]]

**Returns:**
- [[boolean]]

### get_connected_rolling_stock
Gets rolling stock connected to the given end of this stock.
*Only available on:* `RollingStock`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[LuaEntity]] *(optional)*: The rolling stock connected at the given end, `nil` if none is connected there.
- [[defines.rail_direction]] *(optional)*: The rail direction of the connected rolling stock if any.

### is_registered_for_construction
Is this entity or tile ghost or item request proxy registered for construction? If false, it means a construction robot has been dispatched to build the entity, or it is not an entity that can be constructed.

**Returns:**
- [[boolean]]

### is_registered_for_deconstruction
Is this entity registered for deconstruction with this force? If false, it means a construction robot has been dispatched to deconstruct it, or it is not marked for deconstruction. The complexity is effectively O(1) - it depends on the number of objects targeting this entity which should be small enough.

**Parameters:**
- **`force`** — [[ForceID]]: The force construction manager to check.

**Returns:**
- [[boolean]]

### is_registered_for_upgrade
Is this entity registered for upgrade? If false, it means a construction robot has been dispatched to upgrade it, or it is not marked for upgrade. This is worst-case O(N) complexity where N is the current number of things in the upgrade queue.

**Returns:**
- [[boolean]]

### is_registered_for_repair
Is this entity registered for repair? If false, it means a construction robot has been dispatched to repair it, or it is not damaged. This is worst-case O(N) complexity where N is the current number of things in the repair queue.

**Returns:**
- [[boolean]]

### add_autopilot_destination
Adds the given position to this spidertron's autopilot's queue of destinations.
*Only available on:* `SpiderVehicle`

**Parameters:**
- **`position`** — [[MapPosition]]: The position the spidertron should move to.
- **`attempt_patrol`** — [[boolean]] *(optional)*: If the autopilot logic should attempt to initiate patrol mode at the given position. Defaults to `false`.

### connect_linked_belts
Connects current linked belt with another one.

Neighbours have to be of different type. If given linked belt is connected to something else it will be disconnected first. If provided neighbour is connected to something else it will also be disconnected first. Automatically updates neighbour to be connected back to this one.
*Only available on:* `LinkedBelt`

**Parameters:**
- **`neighbour`** — [[LuaEntity]] *(optional)*: Another linked belt or entity ghost containing linked belt to connect or nil to disconnect

### disconnect_linked_belts
Disconnects linked belt from its neighbour.
*Only available on:* `LinkedBelt`

### get_spider_legs
Gets legs of given SpiderVehicle.
*Only available on:* `SpiderVehicle`

**Returns:**
- array<[[LuaEntity]]>

### stop_spider
Sets the [[LuaEntity#speed|speed]] of the given SpiderVehicle to zero. Notably does not clear its [[LuaEntity#autopilot_destination|autopilot_destination]], which it will continue moving towards if set.
*Only available on:* `SpiderVehicle`

### get_wire_connector
Gets a single wire connector of this entity, if any.

**Parameters:**
- **`wire_connector_id`** — [[defines.wire_connector_id]]: Identifier of a specific connector to get
- **`or_create`** — [[boolean]]: If true and connector does not exist, it will be allocated if possible

**Returns:**
- [[LuaWireConnector]] *(optional)*

### get_wire_connectors
Gets all wire connectors of this entity

**Parameters:**
- **`or_create`** — [[boolean]]: If true, it will try to create all connectors possible

**Returns:**
- dictionary<[[defines.wire_connector_id]] → [[LuaWireConnector]]>

### get_rail_end
Gets a LuaRailEnd object for specified end of this rail
*Only available on:* `Rail`

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[LuaRailEnd]]

### get_electric_input_flow_limit
The input flow limit for the electric energy source. `nil` if the entity doesn't have an electric energy source.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_electric_output_flow_limit
The output flow limit for the electric energy source. `nil` if the entity doesn't have an electric energy source.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_beacons
Returns a table with all beacons affecting this effect receiver. Can only be used when the entity has an effect receiver (AssemblingMachine, Furnace, Lab, MiningDrills)

**Returns:**
- array<[[LuaEntity]]> *(optional)*

### get_beacon_effect_receivers
Returns a table with all entities affected by this beacon
*Only available on:* `Beacon`

**Returns:**
- array<[[LuaEntity]]>

### force_finish_ascending
Take an ascending cargo pod and safely make it skip all animation and immediately switch surface.
*Only available on:* `CargoPod`

**Raises:**
- [[on_cargo_pod_finished_ascending]] *(timeframe: instantly)*

### force_finish_descending
Take a descending cargo pod and safely make it arrive and deposit cargo.
*Only available on:* `CargoPod`

**Raises:**
- [[on_cargo_pod_delivered_cargo]] *(timeframe: instantly)*: Raised instantly if landing on the ground (i.e. destination type is [[defines.cargo_destination#surface|surface]]. If landing in a [[defines.cargo_destination#station|station]], event will be raised after parking is complete.
- [[on_cargo_pod_finished_descending]] *(timeframe: instantly)*

### create_cargo_pod
Creates a cargo pod if possible.

Cargo pod will be created with [[defines.cargo_destination#invalid|invalid]] destination type. Setting [[LuaEntity#cargo_pod_destination|cargo_pod_destination]] will cause it to launch.
*Only available on:* `RocketSilo`, `CargoLandingPad`, `SpacePlatformHub`

Takes a table with the following fields:
- **`cargo_hatch`** — [[LuaCargoHatch]] *(optional)*: The hatch to create the pod at. A random (available) one is picked if not provided.
- **`cargo_pod_prototype`** — [[EntityID]] *(optional)*: The cargo pod prototype to create. If not provided, the default cargo pod prototype of the hatch is used.

**Returns:**
- [[LuaEntity]] *(optional)*

### get_cargo_bays
Gets the cargo bays connected to this cargo landing pad or space platform hub.
*Only available on:* `CargoLandingPad`, `SpacePlatformHub`

**Returns:**
- array<[[LuaEntity]]>

### inventory_supports_bar
The same as [[LuaInventory#supports_bar|LuaInventory::supports_bar]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]

**Returns:**
- [[boolean]]

### get_inventory_bar
The same as [[LuaInventory#get_bar|LuaInventory::get_bar]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]

**Returns:**
- [[uint32]]

### set_inventory_bar
The same as [[LuaInventory#set_bar|LuaInventory::set_bar]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]
- **`bar`** — [[uint32]] *(optional)*: The new limit. Omitting this parameter or passing `nil` will clear the limit.

### inventory_supports_filters
The same as [[LuaInventory#supports_filters|LuaInventory::supports_filters]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]

**Returns:**
- [[boolean]]

### is_inventory_filtered
The same as [[LuaInventory#is_filtered|LuaInventory::is_filtered]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]

**Returns:**
- [[boolean]]

### can_set_inventory_filter
The same as [[LuaInventory#can_set_filter|LuaInventory::can_set_filter]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]
- **`index`** — [[uint32]]: The item stack index
- **`filter`** — [[ItemFilter]]: The item filter

**Returns:**
- [[boolean]]

### get_inventory_filter
The same as [[LuaInventory#get_filter|LuaInventory::get_filter]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]
- **`index`** — [[uint32]]: The item stack index

**Returns:**
- [[ItemFilter]] *(optional)*: The current filter or `nil` if none.

### set_inventory_filter
The same as [[LuaInventory#set_filter|LuaInventory::set_filter]] but also works for ghosts where the inventory is not available through [[LuaControl#get_inventory|LuaControl::get_inventory]].

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]
- **`index`** — [[uint32]]: The item stack index.
- **`filter`** — [[ItemFilter]] | [[nil]]: The new filter. `nil` erases any existing filter.

**Returns:**
- [[boolean]]: If the filter was allowed to be set.

### register_tree
Registers the given tree in this agricultural tower.

If the tree is not within range of the tower it will not be registered.

If the tree is already registered with a tower it will not be registered.
*Only available on:* `AgriculturalTower`

**Parameters:**
- **`tree`** — [[LuaEntity]]

**Returns:**
- [[boolean]]: If the tree was registered.

### get_movement
Gets the combined movement vector (direction and speed) of this combat robot or asteroid. The entity moves by this vector each tick.

Note that for combat robots this does not include the constant drift in the direction they are facing.
*Only available on:* `CombatRobot`, `Asteroid`

**Returns:**
- [[Vector]]

### set_movement
Sets the movement direction and movement speed for this combat robot or asteroid.

Note that for combat robots this does not affect the constant drift in the direction they are facing.
*Only available on:* `CombatRobot`, `Asteroid`

**Parameters:**
- **`direction`** — [[Vector]]: This normalized form of this vector is used for the movement direction.
- **`speed`** — [[double]]: Speed in tiles per tick. Cannot be less than 0.

### get_logistic_sections
Gives logistic sections of this entity if it uses logistic sections.

**Returns:**
- [[LuaLogisticSections]] *(optional)*

### set_inventory_size_override
Sets inventory size override. When set, supported entity will ignore inventory size from prototype and will instead keep inventory size equal to the override. Setting `nil` will restore default inventory size.
*Only available on:* `ContainerEntity`, `CargoWagon`

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]
- **`size_override`** — [[uint16]] | [[nil]]
- **`overflow`** — [[LuaInventory]] *(optional)*: Items that would be deleted due to change of inventory size will be transferred to this inventory. Must be a script inventory or inventory of other entity. Inventory references obtained from proxy container are not allowed.

### get_inventory_size_override
Gets the inventory size override of the selected inventory if size override was set using [[LuaEntity#set_inventory_size_override|set_inventory_size_override]].
*Only available on:* `ContainerEntity`, `CargoWagon`

**Parameters:**
- **`inventory_index`** — [[defines.inventory]]

**Returns:**
- [[uint16]] *(optional)*

### get_fluid_source_tile
Gives TilePosition of a tile which this offshore pump uses to check what fluid should be produced.
*Only available on:* `OffshorePump`

**Returns:**
- [[TilePosition]]

### get_fluid_source_fluid
Checks what is expected fluid to be produced from the offshore pump's source tile. It accounts for visible tile, hidden tile and double hidden tile. It ignores currently set fluid box filter.
*Only available on:* `OffshorePump`

**Returns:**
- [[string]] *(optional)*: Name of fluid that should be produced by this offshore pump based on existing tiles.

### clear_stored_durability
*Only available on:* `Lab`

### get_stored_durability
*Only available on:* `Lab`

**Parameters:**
- **`item`** — [[ItemID]]: Item for which a stored durability is requested.

**Returns:**
- [[LabStoredDurability]]: Durability stored.

### set_stored_durability
*Only available on:* `Lab`

**Parameters:**
- **`item`** — [[ItemID]]: Item for which a stored durability is requested.
- **`durability`** — [[LabStoredDurability]]: Durability to set.

### clear_tooltip_fields
Removes all runtime tooltip fields attached to this entity.

### get_tooltip_fields
Gets all runtime tooltip fields attached to this entity.

**Returns:**
- array<[[RuntimeTooltipField]]>

### clear_tooltip_field
Removes selected runtime tooltip field.

**Parameters:**
- **`id`** — [[uint32]]

### get_tooltip_field
Gets selected runtime tooltip field.

**Parameters:**
- **`id`** — [[uint32]]

**Returns:**
- [[RuntimeTooltipField]] *(optional)*

### set_tooltip_field
Adds or changes runtime tooltip field. If `id` is not given a new one will be allocated in a way that makes it unique within this entity. If a value is given that is already used, existing line will be updated.

**Parameters:**
- **`field`** — [[RuntimeTooltipField]]

**Returns:**
- [[uint32]]: Identifier of the record that was given or allocated.
