---
title: LuaEntityPrototype
tags: [factorio-api, runtime, class]
---
# LuaEntityPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of an entity.

## Attributes

### infinite_resource
- **Type:** [[boolean]]
- **Optional**
Whether this resource is infinite.

### minimum_resource_amount
- **Type:** [[uint32]]
- **Optional**
Minimum amount of this resource.

### normal_resource_amount
- **Type:** [[uint32]]
- **Optional**
The normal amount for this resource.

### infinite_depletion_resource_amount
- **Type:** [[uint32]]
- **Optional**
Every time this infinite resource 'ticks' down, it is reduced by this amount. Meaningless if this isn't an infinite resource.

### resource_category
- **Type:** [[string]]
- **Optional**
Name of the category of this resource.

During data stage, this property is named "category".

### mineable_properties
- **Type:** [[MineableProperties]]
Whether this entity is minable and what can be obtained by mining it.

### items_to_place_this
- **Type:** array<[[ItemToPlace]]>
- **Optional**
Items that when placed will produce this entity, if any. Construction bots will choose the first item in the list to build this entity.

### collision_box
- **Type:** [[BoundingBox]]
The bounding box used for collision checking.

### secondary_collision_box
- **Type:** [[BoundingBox]]
- **Optional**
The secondary bounding box used for collision checking, if any. This is only used in rails and rail remnants.

### map_generator_bounding_box
- **Type:** [[BoundingBox]]
The bounding box used for map generator collision checking.

### selection_box
- **Type:** [[BoundingBox]]
The bounding box used for drawing selection.

### drawing_box_vertical_extension
- **Type:** [[double]]
Extra vertical space needed to see the whole entity in GUIs. This is used to calculate the correct zoom and positioning in the entity info gui, for example in the entity tooltip.

### sticker_box
- **Type:** [[BoundingBox]]
The bounding box used to attach sticker type entities.

### collision_mask
- **Type:** [[CollisionMask]]
The collision masks this entity uses

### trigger_target_mask
- **Type:** dictionary<[[string]] → `true`>
The trigger target mask for this entity prototype type.

### attack_target_mask
- **Type:** [[TriggerTargetMask]]
- **Optional**

### ignore_target_mask
- **Type:** [[TriggerTargetMask]]
- **Optional**

### healing_per_tick
- **Type:** [[float]]
- **Optional**
Amount this entity can heal per tick, if any.

### emissions_per_second
- **Type:** dictionary<[[string]] → [[double]]>
A table of pollution emissions per second the entity will create, grouped by the name of the pollution type.

### corpses
- **Type:** dictionary<[[string]] → [[LuaEntityPrototype]]>
- **Optional**
Corpses used when this entity is destroyed. It is a dictionary indexed by the corpse's prototype name.

### folded_turret_corpses
- **Type:** dictionary<[[string]] → [[LuaEntityPrototype]]>
- **Optional**

### selectable_in_game
- **Type:** [[boolean]]
Is this entity selectable?

### selection_priority
- **Type:** [[uint32]]
The selection priority of this entity - a value between `0` and `255`.

### weight
- **Type:** [[double]]
- **Optional**
The weight of this vehicle prototype.

### platform_weight
- **Type:** [[Weight]]
- **Optional**
Weight which this entity adds to total space platform weight when placed.

### resistances
- **Type:** dictionary<[[string]] → [[Resistance]]>
- **Optional**
List of resistances towards each damage type. It is a dictionary indexed by damage type names (see `data/base/prototypes/damage-type.lua`).

### fast_replaceable_group
- **Type:** [[string]]
- **Optional**
The group of mutually fast-replaceable entities, if any.

### next_upgrade
- **Type:** [[LuaEntityPrototype]]
- **Optional**
The next upgrade for this entity, if any.

### icons_positioning
- **Type:** array<[[IconSequencePositioning]]>
- **Optional**
The icon positioning for inventories of this entity, if defined.

### icon_draw_specification
- **Type:** [[IconDrawSpecification]]
The definition of where and how the alt-mode icons of this entity should be drawn.

### loot
- **Type:** array<[[ItemProduct]]>
- **Optional**
Loot that will be dropped when this entity is killed, if any.

### repair_speed_modifier
- **Type:** [[float]]
- **Optional**
Repair-speed modifier for this entity, if any. Actual repair speed will be `tool_repair_speed * entity_repair_speed_modifier`.

### platform_repair_speed_modifier
- **Type:** [[float]]
- **Optional**
Repair speed of entities is multiplied by this value when they are on a space platform with this hub prototype.

### turret_range
- **Type:** [[uint32]]
- **Optional**
The range of this turret.

### turret_prepare_range
- **Type:** [[double]]
- **Optional**

### autoplace_specification
- **Type:** [[AutoplaceSpecification]]
- **Optional**
Autoplace specification for this entity prototype, if any.

### belt_speed
- **Type:** [[double]]
- **Optional**
The speed of this transport belt.

### result_units
- **Type:** array<[[UnitSpawnDefinition]]>
- **Optional**
The result units and spawn points with weight and evolution factor for a biter spawner entity.

### attack_result
- **Type:** array<[[TriggerItem]]>
- **Optional**
The attack result of this entity, if any.

### final_attack_result
- **Type:** array<[[TriggerItem]]>
- **Optional**
The final attack result for this entity if it has one.

### attack_parameters
- **Type:** [[AttackParameters]]
- **Optional**
The attack parameters for this entity, if any.

### revenge_attack_parameters
- **Type:** [[AttackParameters]]
- **Optional**
The revenge attack parameters for this entity, if any. These attack parameters are used in addition to [[LuaEntityPrototype#attack_parameters|LuaEntityPrototype::attack_parameters]] if the entity is attacking a target that has previously dealt damage to the entity.

### spawn_cooldown
- **Type:** table
- **Optional**
The spawning cooldown for this enemy spawner prototype.

### mining_drill_radius
- **Type:** [[double]]
- **Optional**
The mining radius of this mining drill prototype.

### drops_full_belt_stacks
- **Type:** [[boolean]]
- **Optional**
If this mining drill puts full belt stacks onto belts.

### quality_affects_mining_radius
- **Type:** [[boolean]]
- **Optional**

### mining_speed
- **Type:** [[double]]
- **Optional**
The mining speed of this mining drill/character prototype.

### resource_drain_rate_percent
- **Type:** [[uint8]]
- **Optional**
The resource drain rate percent of this mining drill prototype.

### uses_force_mining_productivity_bonus
- **Type:** [[boolean]]
- **Optional**
If this drill uses force productivity bonus

### require_resources_to_place
- **Type:** [[boolean]]
- **Optional**
If this drill requires minable resources before it can be placed.

### logistic_mode
- **Type:** `"requester"` | `"active-provider"` | `"passive-provider"` | `"buffer"` | `"storage"` | `"none"`
- **Optional**
The logistic mode of this logistic container.

### max_underground_distance
- **Type:** [[uint8]]
- **Optional**
The max underground distance for underground belts and underground pipes.

### flags
- **Type:** [[EntityPrototypeFlags]]
The flags for this entity prototype.

### remains_when_mined
- **Type:** array<[[LuaEntityPrototype]]>
The remains left behind when this entity is mined.

### additional_pastable_entities
- **Type:** array<[[LuaEntityPrototype]]>
Entities this entity can be pasted onto in addition to the normal allowed ones.

### allow_copy_paste
- **Type:** [[boolean]]
When false copy-paste is not allowed for this entity.

### shooting_cursor_size
- **Type:** [[float]]
The cursor size used when shooting at this entity.

### created_smoke
- **Type:** table
- **Optional**
The smoke trigger run when this entity is built, if any.

### created_effect
- **Type:** array<[[TriggerItem]]>
- **Optional**
The trigger to run when this entity is created, if any.

### update_effects
- **Type:** array<[[TriggerEffectWithCooldown]]>
- **Optional**
The trigger effects to run every tick when on cooldown.

### update_effects_while_enraged
- **Type:** array<[[TriggerEffectWithCooldown]]>
- **Optional**
The trigger effects to run every tick when on cooldown while the owning [[LuaSegmentedUnit]] is enraged.

### map_color
- **Type:** [[Color]]
- **Optional**
The map color used when charting this entity if a friendly or enemy color isn't defined, if any.

### friendly_map_color
- **Type:** [[Color]]
The friendly map color used when charting this entity.

### enemy_map_color
- **Type:** [[Color]]
The enemy map color used when charting this entity.

### instruments
- **Type:** array<[[ProgrammableSpeakerInstrument]]>
- **Optional**
The instruments for this programmable speaker.

### max_polyphony
- **Type:** [[uint32]]
- **Optional**
The maximum polyphony for this programmable speaker.

### module_inventory_size
- **Type:** [[uint32]]
- **Optional**
The module inventory size. `nil` if this entity doesn't support modules.

Returns the inventory size if this entity is of normal quality. Use [[LuaEntityPrototype#get_inventory_size|LuaEntityPrototype::get_inventory_size]] for other qualities.

### quality_affects_module_slots
- **Type:** [[boolean]]
- **Optional**

### module_slots_quality_bonus
- **Type:** dictionary<[[QualityID]] → [[ItemStackIndex]]>
- **Optional**

### inventory_type
- **Type:** `"normal"` | `"with_bar"` | `"with_filters"` | `"with_filters_and_bar"` | `"with_weight_limit"` | `"with_custom_stack_size"`
- **Optional**
The inventory type this container or linked container uses.

### inventory_weight_limit
- **Type:** [[Weight]]
- **Optional**
Weight limit of the inventory if inventory_type is `"with_weight_limit"`.

### quality_affects_inventory_size
- **Type:** [[boolean]]
- **Optional**

### inventory_properties
- **Type:** [[InventoryWithCustomStackSizeSpecification]]
- **Optional**
Properties of custom inventory. Only provided if `inventory_type` is `"with_custom_stack_size"`.

### ingredient_count
- **Type:** [[uint32]]
- **Optional**
The max number of ingredients this crafting machine prototype supports.

### max_item_product_count
- **Type:** [[uint32]]
- **Optional**
The max number of item products this crafting machine prototype supports.

### crafting_speed_quality_multiplier
- **Type:** dictionary<[[QualityID]] → [[double]]>
- **Optional**

### crafting_categories
- **Type:** dictionary<[[string]] → `true`>
- **Optional**
The [[LuaRecipeCategoryPrototype|crafting categories]] this entity prototype supports.

The value in the dictionary is meaningless and exists just to allow for easy lookup.

### quality_affects_energy_usage
- **Type:** [[boolean]]
- **Optional**

### energy_usage_quality_multiplier
- **Type:** dictionary<[[QualityID]] → [[double]]>
- **Optional**

### resource_categories
- **Type:** dictionary<[[string]] → `true`>
- **Optional**
The [[LuaResourceCategoryPrototype|resource categories]] this character or mining drill supports.

The value in the dictionary is meaningless and exists just to allow for easy lookup.

### energy_usage
- **Type:** [[double]]
- **Optional**
The direct energy usage of this entity, if any.

### effectivity
- **Type:** [[double]]
- **Optional**
The effectivity of this car prototype, generator prototype.

### consumption
- **Type:** [[double]]
- **Optional**
The energy consumption of this car prototype.

### friction_force
- **Type:** [[double]]
- **Optional**
The friction of this vehicle prototype.

### braking_force
- **Type:** [[double]]
- **Optional**
The braking force of this vehicle prototype.

### air_resistance
- **Type:** [[double]]
- **Optional**
The air resistance of this rolling stock prototype.

### tank_driving
- **Type:** [[boolean]]
- **Optional**
If this car prototype uses tank controls to drive.

### rotation_speed
- **Type:** [[double]]
- **Optional**
The rotation speed of this car prototype.

### rotation_snap_angle
- **Type:** [[double]]
- **Optional**
The rotation snap angle of this car prototype.

### turret_rotation_speed
- **Type:** [[float]]
- **Optional**
The turret rotation speed of this prototype.

### guns
- **Type:** dictionary<[[string]] → [[LuaItemPrototype]]>
- **Optional**
A mapping of the gun name to the gun prototype this prototype uses. `nil` if this entity prototype doesn't use guns.

### indexed_guns
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**
A vector of the gun prototypes of this car, spider vehicle, artillery wagon, or turret.

### speed
- **Type:** [[double]]
- **Optional**
The default speed of this flying robot, or unit.

### speed_multiplier_when_out_of_energy
- **Type:** [[float]]
- **Optional**
The speed multiplier when this flying robot is out of energy.

### max_payload_size
- **Type:** [[uint32]]
- **Optional**
The cargo carrying capacity of this logistics or construction robot.

### max_payload_size_after_bonus
- **Type:** [[uint32]]
- **Optional**
The maximum possible cargo carrying capacity of this logistics or construction robot. Bonuses from technologies/forces can't increase the carrying capacity beyond this number.

### require_charge_to_mine
- **Type:** [[boolean]]
- **Optional**
If this robot with logistic interface requires it be charged to manually mine.

### draw_cargo
- **Type:** [[boolean]]
- **Optional**
Whether this logistics or construction robot renders its cargo when flying.

### energy_per_move
- **Type:** [[double]]
- **Optional**
The energy consumed per tile moved for this flying robot.

### energy_per_tick
- **Type:** [[double]]
- **Optional**
The energy consumed per tick for this flying robot.

### min_to_charge
- **Type:** [[float]]
- **Optional**
The minimum energy for this flying robot before it tries to recharge.

### max_to_charge
- **Type:** [[float]]
- **Optional**
The maximum energy for this flying robot above which it won't try to recharge when stationing.

### burner_prototype
- **Type:** [[LuaBurnerPrototype]]
- **Optional**
The burner energy source prototype this entity uses, if any.

### electric_energy_source_prototype
- **Type:** [[LuaElectricEnergySourcePrototype]]
- **Optional**
The electric energy source prototype this entity uses, if any.

### heat_energy_source_prototype
- **Type:** [[LuaHeatEnergySourcePrototype]]
- **Optional**
The heat energy source prototype this entity uses, if any.

### fluid_energy_source_prototype
- **Type:** [[LuaFluidEnergySourcePrototype]]
- **Optional**
The fluid energy source prototype this entity uses, if any.

### void_energy_source_prototype
- **Type:** [[LuaVoidEnergySourcePrototype]]
- **Optional**
The void energy source prototype this entity uses, if any.

### heat_buffer_prototype
- **Type:** [[LuaHeatBufferPrototype]]
- **Optional**
The heat buffer prototype this entity uses, if any.

### build_grid_size
- **Type:** [[uint32]]
The [[EntityPrototype#build_grid_size|grid size]] of the building.

### maximum_temperature
- **Type:** [[double]]
- **Optional**
The maximum fluid temperature of this generator prototype.

### burns_fluid
- **Type:** [[boolean]]
- **Optional**
Whether this generator prototype burns fluid.

### scale_fluid_usage
- **Type:** [[boolean]]
- **Optional**
Whether this generator prototype scales fluid usage.

### destroy_non_fuel_fluid
- **Type:** [[boolean]]
- **Optional**
Whether this generator prototype destroys non-fuel fluids.

### spent_fluid
- **Type:** [[SpentFluidSpecification]]
- **Optional**

### minimum_input_temperature
- **Type:** [[float]]
- **Optional**
The minimum input temperature that this prototype accepts, if specified. An input fluid below this temperature will cause the machine to stop working.

### maximum_input_temperature
- **Type:** [[float]]
- **Optional**
The maximum input temperature that this prototype accepts, if specified. An input fluid above this temperature will cause the machine to stop working.

### minimum_fuel_temperature
- **Type:** [[float]]
- **Optional**
The minimum fuel temperature that this thruster accepts, if specified. Fuel below this temperature will cause the thruster to stop working.

### maximum_fuel_temperature
- **Type:** [[float]]
- **Optional**
The maximum fuel temperature that this thruster accepts, if specified. Fuel above this temperature will cause the thruster to stop working.

### minimum_oxidizer_temperature
- **Type:** [[float]]
- **Optional**
The minimum oxidizer temperature that this thruster accepts, if specified. Oxidizer below this temperature will cause the thruster to stop working.

### maximum_oxidizer_temperature
- **Type:** [[float]]
- **Optional**
The maximum oxidizer temperature that this thruster accepts, if specified. Oxidizer above this temperature will cause the thruster to stop working.

### target_temperature
- **Type:** [[float]]
- **Optional**
The target temperature of this boiler or fusion reactor prototype. If `nil` on a fusion reactor, the target temperature is the default temperature of the output fluid. If specified on a boiler, an input fluid above this temperature will cause the boiler to stop working.

### boiler_mode
- **Type:** `"heat-fluid-inside"` | `"output-to-separate-pipe"`
- **Optional**
The boiler operation mode of this boiler prototype.

### fluid_capacity
- **Type:** [[double]]
The fluid capacity of this entity or 0 if this entity doesn't support fluids.

Crafting machines will report 0 due to their fluid capacity being whatever a given recipe needs.

### valve_mode
- **Type:** [[ValveMode]]
- **Optional**
The mode of operation of this valve.

### valve_threshold
- **Type:** [[float]]
- **Optional**
The default threshold of this valve.

### bulk
- **Type:** [[boolean]]
- **Optional**
Whether this inserter is a bulk-type.

### uses_inserter_stack_size_bonus
- **Type:** [[boolean]]
- **Optional**

### fluid_source_offset
- **Type:** [[Vector]]
- **Optional**

### flow_scaling
- **Type:** [[boolean]]
- **Optional**

### allow_custom_vectors
- **Type:** [[boolean]]
- **Optional**
Whether this inserter allows custom pickup and drop vectors.

### allow_burner_leech
- **Type:** [[boolean]]
- **Optional**
Whether this inserter allows burner leeching.

### inserter_pickup_position
- **Type:** [[Vector]]
- **Optional**
The pickup position for this inserter.

### inserter_drop_position
- **Type:** [[Vector]]
- **Optional**
The drop position for this inserter.

### inserter_chases_belt_items
- **Type:** [[boolean]]
- **Optional**
True if this inserter chases items on belts for pickup.

### inserter_max_belt_stack_size
- **Type:** [[uint8]]
- **Optional**
The max belt stack size for this inserter.

### loader_max_belt_stack_size
- **Type:** [[uint8]]
- **Optional**
The max belt stack size for this loader.

### loader_adjustable_belt_stack_size
- **Type:** [[boolean]]
- **Optional**
True if this loader supports a runtime-adjustable belt stack size.

### loader_wait_for_full_stack
- **Type:** [[boolean]]
- **Optional**
True if this loader will not drop items for which total amount is less than a full belt stack.

### loader_respect_insert_limits
- **Type:** [[boolean]]
- **Optional**

### count_as_rock_for_filtered_deconstruction
- **Type:** [[boolean]]
- **Optional**
If this simple-entity is counted as a rock for the deconstruction planner "trees and rocks only" filter.

### filter_count
- **Type:** [[uint32]]
- **Optional**
The filter count of this inserter, loader, mining drill, roboport or logistic chest. For logistic containers, `nil` means no limit.

### time_to_live
- **Type:** [[MapTick]]
The time to live for this prototype or `0` if prototype doesn't have time_to_live or time_before_removed.

### alert_after_time
- **Type:** [[uint32]]
- **Optional**

### distribution_effectivity
- **Type:** [[double]]
- **Optional**
The distribution effectivity for this beacon prototype.

### distribution_effectivity_bonus_per_quality_level
- **Type:** [[double]]
- **Optional**
The distribution effectivity bonus per quality level for this beacon prototype.

### profile
- **Type:** array<[[double]]>
- **Optional**
The beacon profile: extra multiplier applied to the effects received from beacon by the effect receiver based on amount of beacons that reach that effect receiver

### beacon_counter
- **Type:** `"total"` | `"same_type"`
- **Optional**
The beacon counter used by effect receiver when deciding which sample to take from beacon profile.

### quality_affects_supply_area_distance
- **Type:** [[boolean]]
- **Optional**

### explosion_beam
- **Type:** [[double]]
- **Optional**
Whether this explosion has a beam.

### explosion_rotate
- **Type:** [[double]]
- **Optional**
Whether this explosion rotates.

### tree_color_count
- **Type:** [[uint8]]
- **Optional**
If it is a tree, return the number of colors it supports.

### alert_when_damaged
- **Type:** [[boolean]]
- **Optional**
Whether this entity raises an alert when damaged.

### alert_when_attacking
- **Type:** [[boolean]]
- **Optional**
Whether this turret raises an alert when attacking

### color
- **Type:** [[Color]]
- **Optional**
The color of the prototype, if any.

### collision_mask_collides_with_self
- **Type:** [[boolean]]
Does this prototype collision mask collide with itself?

### collision_mask_collides_with_tiles_only
- **Type:** [[boolean]]
Does this prototype collision mask collide with tiles only?

### collision_mask_considers_tile_transitions
- **Type:** [[boolean]]
Does this prototype collision mask consider tile transitions?

### allowed_effects
- **Type:** dictionary<[[string]] → [[boolean]]>
- **Optional**
The allowed module effects for this entity, if any.

### allowed_module_categories
- **Type:** dictionary<[[string]] → `true`>
- **Optional**
The allowed module categories for this entity, if any.

### rocket_parts_required
- **Type:** [[uint32]]
- **Optional**
The rocket parts required for this rocket silo prototype.

### lift_weight
- **Type:** [[Weight]]
- **Optional**

### rocket_rising_delay
- **Type:** [[uint8]]
- **Optional**
The rocket rising delay for this rocket silo prototype.

### launch_wait_time
- **Type:** [[uint8]]
- **Optional**
The rocket launch delay for this rocket silo prototype.

### light_blinking_speed
- **Type:** [[double]]
- **Optional**
The light blinking speed for this rocket silo prototype.

### door_opening_speed
- **Type:** [[double]]
- **Optional**
The door opening speed for this rocket silo prototype.

### launch_to_space_platforms
- **Type:** [[boolean]]
- **Optional**

### rising_speed
- **Type:** [[double]]
- **Optional**
The rising speed for this rocket silo rocket prototype.

### engine_starting_speed
- **Type:** [[double]]
- **Optional**
The engine starting speed for this rocket silo rocket prototype.

### flying_speed
- **Type:** [[double]]
- **Optional**
The flying speed for this rocket silo rocket prototype.

### flying_acceleration
- **Type:** [[double]]
- **Optional**
The flying acceleration for this rocket silo rocket prototype.

### fixed_recipe
- **Type:** [[LuaRecipePrototype]]
- **Optional**
The fixed recipe for this assembling machine prototype, if any.

### fixed_quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**
The fixed recipe quality for this assembling machine prototype, if any.

### construction_radius
- **Type:** [[double]]
- **Optional**
The construction radius for this roboport prototype.

### logistic_radius
- **Type:** [[double]]
- **Optional**
The logistic radius for this roboport prototype.

### energy_per_hit_point
- **Type:** [[double]]
- **Optional**
The energy used per hit point taken for this vehicle during collisions.

### create_ghost_on_death
- **Type:** [[boolean]]
If this prototype will attempt to create a ghost of itself on death.

If this is false then a ghost will never be made, if it's true a ghost may be made.

### ammo_category
- **Type:** [[string]]
- **Optional**
Name of the ammo category of this land mine.

### timeout
- **Type:** [[uint32]]
- **Optional**
The time it takes this land mine to arm.

### trigger_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**
The collision mask entities must collide with to make this landmine blow up.

### fluidbox_prototypes
- **Type:** array<[[LuaFluidBoxPrototype]]>
The fluidbox prototypes for this entity.

### neighbour_bonus
- **Type:** [[double]]
- **Optional**

### container_distance
- **Type:** [[double]]
- **Optional**

### belt_distance
- **Type:** [[double]]
- **Optional**

### belt_length
- **Type:** [[double]]
- **Optional**

### per_lane_filters
- **Type:** [[boolean]]
- **Optional**

### is_building
- **Type:** [[boolean]]
These are the objects that are considered buildings:

- AccumulatorPrototype
- AgriculturalTowerPrototype
- ArtilleryTurretPrototype
- AsteroidCollectorPrototype
- BeaconPrototype
- BoilerPrototype
- BurnerGeneratorPrototype
- CargoBayPrototype
- CargoLandingPadPrototype
- CombinatorPrototype → ArithmeticCombinator, DeciderCombinator, SelectorCombinator
- ConstantCombinatorPrototype
- ContainerPrototype → LogisticContainer, InfinityContainer, TemporaryContainer
- CraftingMachinePrototype → AssemblingMachine, RocketSilo, Furnace
- DisplayPanelPrototype
- ElectricEnergyInterfacePrototype
- ElectricPolePrototype
- EnemySpawnerPrototype
- FusionGeneratorPrototype
- FusionReactorPrototype
- GatePrototype
- GeneratorPrototype
- HeatInterfacePrototype
- HeatPipePrototype
- InserterPrototype
- LabPrototype
- LampPrototype
- LightningAttractorPrototype
- LinkedContainerPrototype
- MarketPrototype
- MiningDrillPrototype
- OffshorePumpPrototype
- PipePrototype → InfinityPipe
- PipeToGroundPrototype
- PowerSwitchPrototype
- ProgrammableSpeakerPrototype
- ProxyContainerPrototype
- PumpPrototype
- RadarPrototype
- RailPrototype → CurvedRailA, ElevatedCurvedRailA, CurvedRailB, ElevatedCurvedRailB, HalfDiagonalRail, ElevatedHalfDiagonalRail, LegacyCurvedRail, LegacyStraightRail, RailRamp, StraightRail, ElevatedStraightRail
- RailSignalBasePrototype → RailChainSignal, RailSignal
- RailSupportPrototype
- ReactorPrototype
- RoboportPrototype
- SimpleEntityPrototype
- SimpleEntityWithOwnerPrototype → SimpleEntityWithForce
- SolarPanelPrototype
- SpacePlatformHubPrototype
- StorageTankPrototype
- ThrusterPrototype
- TrainStopPrototype
- TransportBeltConnectablePrototype → LaneSplitter, LinkedBelt, Loader1x1, Loader1x2, Splitter, TransportBelt, UndergroundBelt
- TurretPrototype → AmmoTurret, ElectricTurret, FluidTurret
- ValvePrototype
- WallPrototype

### automated_ammo_count
- **Type:** [[uint32]]
- **Optional**
The amount of ammo that inserters automatically insert into this ammo turret, artillery turret or artillery wagon.

### max_speed
- **Type:** [[double]]
- **Optional**
The max speed of this projectile or flying robot prototype.

### darkness_for_all_lamps_on
- **Type:** [[float]]
- **Optional**
Value between 0 and 1 darkness where all lamps of this lamp prototype are on.

### darkness_for_all_lamps_off
- **Type:** [[float]]
- **Optional**
Value between 0 and 1 darkness where all lamps of this lamp prototype are off.

### always_on
- **Type:** [[boolean]]
- **Optional**
Whether the lamp is always on (except when out of power or turned off by the circuit network).

### min_darkness_to_spawn
- **Type:** [[float]]
- **Optional**
The minimum darkness at which this unit spawner can spawn entities.

### max_darkness_to_spawn
- **Type:** [[float]]
- **Optional**
The maximum darkness at which this unit spawner can spawn entities.

### call_for_help_radius
- **Type:** [[double]]
- **Optional**

### max_count_of_owned_units
- **Type:** [[double]]
- **Optional**
Count of enemies this spawner can sustain.

### max_count_of_owned_defensive_units
- **Type:** [[double]]
- **Optional**
Count of defensive enemies this spawner can sustain.

### max_friends_around_to_spawn
- **Type:** [[double]]
- **Optional**
How many friendly units are required within the spawning_radius of this spawner for it to stop producing more units.

### max_defensive_friends_around_to_spawn
- **Type:** [[double]]
- **Optional**
How many defensive friendly units are required within the spawning_radius of this spawner for it to stop producing more units.

### spawning_radius
- **Type:** [[double]]
- **Optional**
How far from the spawner can the units be spawned.

### spawning_spacing
- **Type:** [[double]]
- **Optional**
What spaces should be between the spawned units.

### radius
- **Type:** [[double]]
The radius of this entity prototype. The radius is defined as half the distance between the top left corner and bottom right corner of the collision box.

### show_fluid_visualization_when_in_cursor
- **Type:** [[boolean]]

### cliff_explosive_prototype
- **Type:** [[string]]
- **Optional**
The item prototype name used to destroy this cliff.

### rocket_entity_prototype
- **Type:** [[LuaEntityPrototype]]
- **Optional**
The rocket entity prototype associated with this rocket silo prototype.

### has_belt_immunity
- **Type:** [[boolean]]
- **Optional**
Whether this unit, car, or character prototype has belt immunity.

### vision_distance
- **Type:** [[double]]
- **Optional**
The vision distance of this unit prototype.

### absorptions_to_join_attack
- **Type:** dictionary<[[string]] → [[float]]>
- **Optional**
A table of pollutions amounts that has to be absorbed by the unit's spawner before the unit will leave the spawner and attack the source of the pollution, indexed by the name of each absorbed pollution type.

### min_pursue_time
- **Type:** [[uint32]]
- **Optional**
The minimum pursue time of this unit prototype.

### max_pursue_distance
- **Type:** [[double]]
- **Optional**
The maximum pursue distance of this unit prototype.

### radar_range
- **Type:** [[uint32]]
- **Optional**

### move_while_shooting
- **Type:** [[boolean]]
- **Optional**
Whether this unit prototype can move while shooting.

### can_open_gates
- **Type:** [[boolean]]
- **Optional**
Whether this unit prototype can open gates.

### affected_by_tiles
- **Type:** [[boolean]]
- **Optional**
Whether this unit prototype is affected by tile walking speed modifiers.

### distraction_cooldown
- **Type:** [[uint32]]
- **Optional**
The distraction cooldown of this unit prototype.

### spawning_time_modifier
- **Type:** [[double]]
- **Optional**
The spawning time modifier of this unit prototype.

### alert_icon_shift
- **Type:** [[Vector]]
The alert icon shift of this entity prototype.

### alert_icon_scale
- **Type:** [[float]]
The alert icon scale of this entity prototype.

### lab_inputs
- **Type:** array<[[string]]>
- **Optional**
The item prototype names that are the inputs of this lab prototype.

### uses_quality_drain_modifier
- **Type:** [[boolean]]
- **Optional**
If this lab uses the quality drain modifier when consuming science packs.

### science_pack_drain_rate_percent
- **Type:** [[uint8]]
- **Optional**
How much science pack durability is required to research one science point.

### default_technology_level_signal
- **Type:** [[SignalID]]
- **Optional**

### effect_receiver
- **Type:** [[EffectReceiver]]
- **Optional**
Effect receiver prototype of crafting machine, lab, mining drill, or agricultural tower.

### allow_access_to_all_forces
- **Type:** [[boolean]]
- **Optional**
Whether this market allows access to all forces or just friendly ones.

### supports_direction
- **Type:** [[boolean]]
Whether this entity prototype could possibly ever be rotated.

### terrain_friction_modifier
- **Type:** [[float]]
- **Optional**
The terrain friction modifier for this vehicle.

### allow_passengers
- **Type:** [[boolean]]
- **Optional**
Whether this vehicle allows passengers.

### grid_prototype
- **Type:** [[LuaEquipmentGridPrototype]]
- **Optional**
The equipment grid prototype for this entity, if any.

### remove_decoratives
- **Type:** `"automatic"` | `"true"` | `"false"`
Whether this entity should remove decoratives that collide with it when this entity is built.

### related_underground_belt
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### inserter_stack_size_bonus
- **Type:** [[uint32]]
- **Optional**
The built-in stack size bonus of this inserter prototype.

### protected_from_tile_building
- **Type:** [[boolean]]
True if this entity prototype should be included during tile collision checks with [[LuaTilePrototype#check_collision_with_entities|LuaTilePrototype::check_collision_with_entities]] enabled.

### is_entity_with_owner
- **Type:** [[boolean]]
True if this is entity-with-owner

### is_military_target
- **Type:** [[boolean]]
- **Optional**
True if this entity-with-owner is military target

### allow_run_time_change_of_is_military_target
- **Type:** [[boolean]]
- **Optional**
True if this entity-with-owner's is_military_target can be changed run-time (on the entity, not on the prototype itself)

### logistic_parameters
- **Type:** table
- **Optional**
The logistic parameters for this roboport.

### height
- **Type:** [[double]]
- **Optional**
The height of this spider unit, spider vehicle or projectile.

### torso_rotation_speed
- **Type:** [[double]]
- **Optional**
The torso rotation speed of this spider vehicle prototype.

### torso_bob_speed
- **Type:** [[double]]
- **Optional**
The torso bob speed of this spider vehicle prototype.

### automatic_weapon_cycling
- **Type:** [[boolean]]
- **Optional**
Whether this spider vehicle prototype automatically cycles weapons.

### chain_shooting_cooldown_modifier
- **Type:** [[double]]
- **Optional**
The chain shooting cooldown modifier of this spider vehicle prototype.

### spider_engine
- **Type:** [[SpiderEngineSpecification]]
- **Optional**

### chunk_exploration_radius
- **Type:** [[double]]
- **Optional**
The chunk exploration radius of this vehicle prototype.

### animation_speed_coefficient
- **Type:** [[double]]
- **Optional**
The animation speed coefficient of this belt connectable prototype.

### manual_range_modifier
- **Type:** [[double]]
- **Optional**
The manual range modifier for this artillery turret or wagon prototype.

### disable_automatic_firing
- **Type:** [[boolean]]
- **Optional**
If automatic firing is disabled for this artillery turret or artillery wagon.

### ammo_stack_limit
- **Type:** [[ItemCountType]]
- **Optional**
The max stack size of ammo in this artillery turret or artillery wagon.

### dying_speed
- **Type:** [[float]]
- **Optional**
The dying time of this corpse prototype.

### active_energy_usage
- **Type:** [[double]]
- **Optional**
The active energy usage of this rocket silo or combinator prototype.

### lamp_energy_usage
- **Type:** [[double]]
- **Optional**
The lamp energy usage of this rocket silo prototype.

### crane_energy_usage
- **Type:** [[double]]
- **Optional**
The crane energy usage of this agricultural tower prototype.

### use_exact_mode
- **Type:** [[boolean]]
- **Optional**
Whether this logistic container prototype uses exact mode

### tile_width
- **Type:** [[uint32]]
Specifies the tiling size of the entity, is used to decide, if the center should be in the center of the tile (odd tile size dimension) or on the tile border (even tile size dimension)

### tile_height
- **Type:** [[uint32]]
Specifies the tiling size of the entity, is used to decide, if the center should be in the center of the tile (odd tile size dimension) or on the tile border (even tile size dimension)

### vertical_selection_shift
- **Type:** [[double]]
- **Optional**
Vertical selection shift used by rolling stocks. It affects selection box vertical position but is also used to shift rolling stock graphics along the rails to fine tune train's look.

### spawn_decoration
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### spawn_decorations_on_expansion
- **Type:** [[boolean]]
- **Optional**

### connection_distance
- **Type:** [[double]]
- **Optional**

### joint_distance
- **Type:** [[double]]
- **Optional**

### radius_visualisation_specification
- **Type:** [[RadiusVisualisationSpecification]]
- **Optional**

### growth_ticks
- **Type:** [[uint32]]
- **Optional**

### harvest_emissions
- **Type:** dictionary<[[string]] → [[double]]>
- **Optional**
A table of pollutants that this plant will release when it is harvested.

### agricultural_tower_radius
- **Type:** [[double]]
- **Optional**

### growth_area_radius
- **Type:** [[double]]
- **Optional**

### growth_grid_tile_size
- **Type:** [[uint32]]
- **Optional**

### randomize_planting_tile
- **Type:** [[boolean]]
- **Optional**

### random_growth_offset
- **Type:** [[double]]
- **Optional**

### vector_to_place_result
- **Type:** [[Vector]]
- **Optional**

### surface_conditions
- **Type:** array<[[SurfaceCondition]]>
- **Optional**
The surface conditions required to build this entity.

### heating_energy
- **Type:** [[double]]
The energy required to keep this entity from freezing. Zero energy means it doesn't freeze.

### auto_setup_collision_box
- **Type:** [[boolean]]
- **Optional**

### factoriopedia_alternative
- **Type:** [[LuaEntityPrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### rewire_neighbours_when_destroying
- **Type:** [[boolean]]
- **Optional**

### solar_panel_performance_at_day
- **Type:** [[double]]
- **Optional**

### solar_panel_performance_at_night
- **Type:** [[double]]
- **Optional**

### solar_panel_solar_coefficient_property
- **Type:** [[LuaSurfacePropertyPrototype]]
- **Optional**

### accepted_seeds
- **Type:** array<[[string]]>
- **Optional**

### captured_spawner_entity
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### min_performance
- **Type:** [[ThrusterPerformancePoint]]
- **Optional**

### max_performance
- **Type:** [[ThrusterPerformancePoint]]
- **Optional**

### two_direction_only
- **Type:** [[boolean]]
- **Optional**

### perceived_performance
- **Type:** [[PerceivedPerformance]]
- **Optional**

### overkill_fraction
- **Type:** [[float]]
- **Optional**

### dying_explosion
- **Type:** array<[[ExplosionDefinition]]>
- **Optional**

### rocket_dying_explosion
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### dying_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### damaged_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### attack_reaction
- **Type:** array<[[AttackReactionItem]]>
- **Optional**

### hide_resistances
- **Type:** [[boolean]]
- **Optional**

### random_corpse_variation
- **Type:** [[boolean]]
- **Optional**

### neighbour_connectable
- **Type:** [[NeighbourConnectable]]
- **Optional**

### tile_buildability_rules
- **Type:** array<[[TileBuildabilityRule]]>
- **Optional**

### support_range
- **Type:** [[float]]
- **Optional**

### reversing_power_modifier
- **Type:** [[double]]
- **Optional**

### use_mirroring
- **Type:** [[boolean]]
- **Optional**

### allows_flipping
- **Type:** [[boolean]]
When this entity is part of blueprint, will it allow flipping of the blueprint?

### territory_radius
- **Type:** [[uint32]]
- **Optional**

### enraged_duration
- **Type:** [[MapTick]]
- **Optional**

### patrolling_speed
- **Type:** [[double]]
- **Optional**

### investigating_speed
- **Type:** [[double]]
- **Optional**

### attacking_speed
- **Type:** [[double]]
- **Optional**

### enraged_speed
- **Type:** [[double]]
- **Optional**

### acceleration_rate
- **Type:** [[double]]
- **Optional**

### turn_radius
- **Type:** [[double]]
- **Optional**

### patrolling_turn_radius
- **Type:** [[double]]
- **Optional**

### turn_smoothing
- **Type:** [[double]]
- **Optional**

### ticks_per_scan
- **Type:** [[uint32]]
- **Optional**

### segment_engine
- **Type:** [[SegmentEngineSpecification]]
- **Optional**

### running_speed
- **Type:** [[double]]
- **Optional**
The movement speed of this character prototype.

### maximum_corner_sliding_distance
- **Type:** [[double]]
- **Optional**

### build_distance
- **Type:** [[uint32]]
- **Optional**

### drop_item_distance
- **Type:** [[uint32]]
- **Optional**

### reach_distance
- **Type:** [[uint32]]
- **Optional**

### reach_resource_distance
- **Type:** [[double]]
- **Optional**

### item_pickup_distance
- **Type:** [[double]]
- **Optional**

### loot_pickup_distance
- **Type:** [[double]]
- **Optional**

### enter_vehicle_distance
- **Type:** [[double]]
- **Optional**

### ticks_to_keep_gun
- **Type:** [[uint32]]
- **Optional**

### ticks_to_keep_aiming_direction
- **Type:** [[uint32]]
- **Optional**

### ticks_to_stay_in_combat
- **Type:** [[uint32]]
- **Optional**

### respawn_time
- **Type:** [[uint32]]
- **Optional**

### damage_hit_tint
- **Type:** [[Color]]
- **Optional**

### character_corpse
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### grounded_landing_search_radius
- **Type:** [[double]]
- **Optional**

### tool_attack_distance
- **Type:** [[double]]
- **Optional**

### flying_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**

### tool_attack_result
- **Type:** array<[[TriggerItem]]>
- **Optional**

### footstep_particle_triggers
- **Type:** dictionary<[[LuaTilePrototype]] → array<[[TriggerEffectItem]]>>
- **Optional**

### synced_footstep_particle_triggers
- **Type:** dictionary<[[LuaTilePrototype]] → array<[[TriggerEffectItem]]>>
- **Optional**

### footprint_particles
- **Type:** dictionary<[[LuaTilePrototype]] → array<[[LuaParticlePrototype]]>>
- **Optional**

### arm_inventory_size_quality_increase
- **Type:** [[ItemStackIndex]]
- **Optional**

### inventory_size_quality_increase
- **Type:** [[ItemStackIndex]]
- **Optional**

### passive_energy_usage
- **Type:** [[double]]
- **Optional**

### arm_energy_usage
- **Type:** [[double]]
- **Optional**

### arm_slow_energy_usage
- **Type:** [[double]]
- **Optional**

### energy_usage_quality_scaling
- **Type:** [[float]]
- **Optional**

### arm_count_base
- **Type:** [[uint32]]
- **Optional**

### arm_count_quality_scaling
- **Type:** [[uint32]]
- **Optional**

### head_collection_radius
- **Type:** [[float]]
- **Optional**

### collection_box_offset
- **Type:** [[float]]
- **Optional**

### deposit_radius
- **Type:** [[float]]
- **Optional**

### arm_speed_base
- **Type:** [[float]]
- **Optional**

### arm_speed_quality_scaling
- **Type:** [[float]]
- **Optional**

### arm_angular_speed_cap_base
- **Type:** [[float]]
- **Optional**

### arm_angular_speed_cap_quality_scaling
- **Type:** [[float]]
- **Optional**

### tether_size
- **Type:** [[float]]
- **Optional**

### unpowered_arm_speed_scale
- **Type:** [[float]]
- **Optional**

### minimal_arm_swing_segment_retraction
- **Type:** [[uint32]]
- **Optional**

### held_items_offset
- **Type:** [[float]]
- **Optional**

### held_items_spread
- **Type:** [[float]]
- **Optional**

### held_items_display_count
- **Type:** [[uint8]]
- **Optional**

### arm_color_gradient
- **Type:** array<[[Color]]>
- **Optional**

### fluid_buffer_size
- **Type:** [[FluidAmount]]
- **Optional**

### activation_buffer_ratio
- **Type:** [[FluidAmount]]
- **Optional**

### fluid_buffer_input_flow
- **Type:** [[FluidAmount]]
- **Optional**

### range_from_player
- **Type:** [[double]]
- **Optional**

### combat_robot_friction
- **Type:** [[double]]
- **Optional**

### destroy_action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### follows_player
- **Type:** [[boolean]]
- **Optional**

### separation_range
- **Type:** [[double]]
- **Optional**

### max_separation_force
- **Type:** [[double]]
- **Optional**

### separation_force_factor
- **Type:** [[double]]
- **Optional**

### strike_effect
- **Type:** array<[[TriggerItem]]>
- **Optional**

### attractor_hit_effect
- **Type:** array<[[TriggerItem]]>
- **Optional**

### damage
- **Type:** [[DamageParameters]]
- **Optional**
When lightning strikes something that is not a lightning attractor, this damage is applied to the target.

For stickers the damage is applied every [[LuaEntityPrototype#damage_interval|LuaEntityPrototype::damage_interval]] ticks.

### energy
- **Type:** [[double]]
- **Optional**
When lightning hits a lightning attractor this amount of energy is transferred to the lightning attractor.

### source_offset
- **Type:** [[Vector]]
- **Optional**

### source_variance
- **Type:** [[Vector]]
- **Optional**

### time_to_damage
- **Type:** [[uint16]]
- **Optional**

### effect_duration
- **Type:** [[uint16]]
- **Optional**

### connection_category
- **Type:** array<[[string]]>
- **Optional**

### quality_affects_capacity
- **Type:** [[boolean]]
- **Optional**

### default_output_signal
- **Type:** [[SignalID]]
- **Optional**

### energy_per_shot
- **Type:** [[double]]
- **Optional**

### prepare_with_no_ammo
- **Type:** [[boolean]]
- **Optional**

### life_time
- **Type:** [[uint16]]
- **Optional**

### regular_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### regular_trigger_effect_frequency
- **Type:** [[uint32]]
- **Optional**

### ended_in_water_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### movement_modifier_when_on_ground
- **Type:** [[double]]
- **Optional**

### movement_modifier
- **Type:** [[double]]
- **Optional**

### creation_shift
- **Type:** [[Vector]]
- **Optional**

### initial_speed
- **Type:** [[Vector]]
- **Optional**

### initial_height
- **Type:** [[float]]
- **Optional**

### initial_vertical_speed
- **Type:** [[float]]
- **Optional**

### shots_per_flare
- **Type:** [[uint32]]
- **Optional**

### early_death_ticks
- **Type:** [[uint32]]
- **Optional**

### shot_category
- **Type:** [[LuaAmmoCategoryPrototype]]
- **Optional**

### height_from_ground
- **Type:** [[float]]
- **Optional**

### reveal_map
- **Type:** [[boolean]]
- **Optional**

### gui_title_key
- **Type:** [[string]]
- **Optional**

### default_recipe_finished_signal
- **Type:** [[SignalID]]
- **Optional**

### default_working_signal
- **Type:** [[SignalID]]
- **Optional**

### disabled_when_recipe_not_researched
- **Type:** [[boolean]]
- **Optional**

### fluid_boxes_off_when_no_fluid_recipe
- **Type:** [[boolean]]
- **Optional**

### damage_per_hp
- **Type:** [[float]]
- **Optional**

### width
- **Type:** [[float]]
- **Optional**

### damage_interval
- **Type:** [[uint32]]
- **Optional**

### action_triggered_automatically
- **Type:** [[boolean]]
- **Optional**

### steering_settings
- **Type:** [[SteeringSettings]]
- **Optional**

### ai_settings
- **Type:** [[UnitAISettings]]
- **Optional**

### capture_speed
- **Type:** [[double]]
- **Optional**

### search_radius
- **Type:** [[double]]
- **Optional**

### auto_sort_inventory
- **Type:** [[boolean]]
- **Optional**

### immune_to_tree_impacts
- **Type:** [[boolean]]
- **Optional**

### immune_to_rock_impacts
- **Type:** [[boolean]]
- **Optional**

### immune_to_cliff_impacts
- **Type:** [[boolean]]
- **Optional**

### immune_to_all_impacts
- **Type:** [[boolean]]
- **Optional**

### track_particle_triggers
- **Type:** dictionary<[[LuaTilePrototype]] → array<[[TriggerEffectItem]]>>
- **Optional**

### destroy_on_empty
- **Type:** [[boolean]]
- **Optional**

### has_direction
- **Type:** [[boolean]]
- **Optional**

### allow_unloading
- **Type:** [[boolean]]
- **Optional**

### use_unloading_distance_limit
- **Type:** [[boolean]]
- **Optional**

### hatch_definitions
- **Type:** array<[[CargoHatchDefinition]]>
- **Optional**

### connectable_box
- **Type:** [[BoundingBox]]
- **Optional**

### cargo_station_parameters
- **Type:** [[CargoStationParameters]]
- **Optional**

### shadow_slave_entity
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### sticker_movement_modifiers
- **Type:** table
- **Optional**

### sticker_vehicle_modifiers
- **Type:** table
- **Optional**

### fire_spread_entity
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### fire_spread_cooldown
- **Type:** [[uint8]]
- **Optional**

### fire_spread_radius
- **Type:** [[float]]
- **Optional**

### stickers_per_square_meter
- **Type:** [[float]]
- **Optional**

### should_ground_target
- **Type:** [[boolean]]
- **Optional**

### force_visibility
- **Type:** [[ForceCondition]]
- **Optional**

### use_damage_substitute
- **Type:** [[boolean]]
- **Optional**

### orientations
- **Type:** [[OrientedCliffPrototypeSet]]
- **Optional**

### grid_size
- **Type:** [[Vector]]
- **Optional**

### grid_offset
- **Type:** [[Vector]]
- **Optional**

### place_as_crater
- **Type:** [[CraterPlacementDefinition]]
- **Optional**

### pulse_duration
- **Type:** [[uint32]]
- **Optional**

### direction_count
- **Type:** [[uint8]]
- **Optional**

### default_status
- **Type:** [[defines.entity_status]]
- **Optional**

### default_empty_slots_signal
- **Type:** [[SignalID]]
- **Optional**

### expires
- **Type:** [[boolean]]
- **Optional**

### remove_on_entity_placement
- **Type:** [[boolean]]
- **Optional**

### remove_on_tile_placement
- **Type:** [[boolean]]
- **Optional**

### input_connection_bounding_box
- **Type:** [[BoundingBox]]
- **Optional**

### output_connection_bounding_box
- **Type:** [[BoundingBox]]
- **Optional**

### max_text_width
- **Type:** [[uint32]]
- **Optional**

### max_text_length
- **Type:** [[uint32]]
- **Optional**

### max_records_count
- **Type:** [[uint32]]
- **Optional**

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**

### track_coverage_during_drag_building
- **Type:** [[boolean]]
- **Optional**

### auto_connect_up_to_n_wires
- **Type:** [[uint8]]
- **Optional**

### start_attacking_only_when_can_shoot
- **Type:** [[boolean]]
- **Optional**

### leave_attacking_if_shoot_fails
- **Type:** [[boolean]]
- **Optional**

### shoot_in_prepare_state
- **Type:** [[boolean]]
- **Optional**

### allow_turning_when_starting_attack
- **Type:** [[boolean]]
- **Optional**

### can_retarget_while_starting_attack
- **Type:** [[boolean]]
- **Optional**

### turret_base_has_direction
- **Type:** [[boolean]]
- **Optional**

### max_richness_for_spawn_shift
- **Type:** [[double]]
- **Optional**

### absorptions_per_second
- **Type:** dictionary<[[string]] → [[EnemySpawnerAbsorption]]>
- **Optional**

### time_to_capture
- **Type:** [[MapTick]]
- **Optional**

### spawn_blocked_trigger
- **Type:** array<[[TriggerItem]]>
- **Optional**

### smoke
- **Type:** [[LuaTrivialSmokePrototype]]
- **Optional**

### smoke_count
- **Type:** [[uint16]]
- **Optional**

### explosion_effect
- **Type:** array<[[TriggerItem]]>
- **Optional**

### spawn_entity
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### damage_per_tick
- **Type:** [[DamageParameters]]
- **Optional**

### maximum_spread_count
- **Type:** [[uint16]]
- **Optional**

### initial_flame_count
- **Type:** [[uint8]]
- **Optional**

### uses_alternative_behavior
- **Type:** [[boolean]]
- **Optional**

### limit_overlapping_particles
- **Type:** [[boolean]]
- **Optional**

### spread_delay
- **Type:** [[uint32]]
- **Optional**

### spread_delay_deviation
- **Type:** [[uint32]]
- **Optional**

### tree_dying_factor
- **Type:** [[float]]
- **Optional**

### initial_lifetime
- **Type:** [[uint32]]
- **Optional**

### damage_multiplier_decrease_per_tick
- **Type:** [[float]]
- **Optional**

### damage_multiplier_increase_per_added_fuel
- **Type:** [[float]]
- **Optional**

### maximum_damage_multiplier
- **Type:** [[float]]
- **Optional**

### lifetime_increase_by
- **Type:** [[uint32]]
- **Optional**

### lifetime_increase_cooldown
- **Type:** [[uint32]]
- **Optional**

### maximum_lifetime
- **Type:** [[uint32]]
- **Optional**

### add_fuel_cooldown
- **Type:** [[uint32]]
- **Optional**

### delay_between_initial_flames
- **Type:** [[uint32]]
- **Optional**

### on_fuel_added_action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### on_damage_tick_effect
- **Type:** array<[[TriggerItem]]>
- **Optional**

### smoke_sources
- **Type:** array<[[SmokeSource]]>
- **Optional**

### initial_action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### special_neutral_target_damage
- **Type:** [[DamageParameters]]
- **Optional**

### particle_buffer_size
- **Type:** [[uint16]]
- **Optional**

### particle_spawn_interval
- **Type:** [[uint16]]
- **Optional**

### particle_spawn_timeout
- **Type:** [[uint16]]
- **Optional**

### stream_particle_horizontal_speed
- **Type:** [[float]]
- **Optional**

### stream_particle_horizontal_speed_deviation
- **Type:** [[float]]
- **Optional**

### particle_vertical_acceleration
- **Type:** [[float]]
- **Optional**

### progress_to_create_smoke
- **Type:** [[float]]
- **Optional**

### target_position_deviation
- **Type:** [[double]]
- **Optional**

### target_initial_position_only
- **Type:** [[boolean]]
- **Optional**

### drive_over_tie_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### drive_over_tie_trigger_minimal_speed
- **Type:** [[double]]
- **Optional**

### tie_distance
- **Type:** [[double]]
- **Optional**

### allow_manual_color
- **Type:** [[boolean]]
- **Optional**

### allow_robot_dispatch_in_automatic_mode
- **Type:** [[boolean]]
- **Optional**

### default_copy_color_from_train_stop
- **Type:** [[boolean]]
- **Optional**

### quality_affects_max_speed
- **Type:** [[boolean]]
- **Optional**

### transition_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**

### elevated_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**

### elevated_selection_priority
- **Type:** [[uint8]]
- **Optional**

### drive_over_elevated_tie_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### cant_insert_at_source_message_key
- **Type:** [[string]]
- **Optional**

### custom_input_slot_tooltip_key
- **Type:** [[string]]
- **Optional**

### opening_speed
- **Type:** [[float]]
- **Optional**

### activation_distance
- **Type:** [[double]]
- **Optional**

### timeout_to_close
- **Type:** [[uint32]]
- **Optional**

### opened_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**

### heating_radius
- **Type:** [[float]]
- **Optional**

### erase_contents_when_mined
- **Type:** [[boolean]]
- **Optional**

### preserve_contents_when_created
- **Type:** [[boolean]]
- **Optional**

### energy_per_movement
- **Type:** [[double]]
- **Optional**

### energy_per_rotation
- **Type:** [[double]]
- **Optional**

### use_easter_egg
- **Type:** [[boolean]]
- **Optional**

### grab_less_to_match_belt_stack
- **Type:** [[boolean]]
- **Optional**

### wait_for_full_hand
- **Type:** [[boolean]]
- **Optional**

### enter_drop_mode_if_held_stack_spoiled
- **Type:** [[boolean]]
- **Optional**

### default_stack_control_input_signal
- **Type:** [[SignalID]]
- **Optional**

### default_red_signal
- **Type:** [[SignalID]]
- **Optional**

### default_green_signal
- **Type:** [[SignalID]]
- **Optional**

### default_blue_signal
- **Type:** [[SignalID]]
- **Optional**

### default_rgb_signal
- **Type:** [[SignalID]]
- **Optional**

### trigger_interval
- **Type:** [[uint32]]
- **Optional**

### trigger_radius
- **Type:** [[double]]
- **Optional**

### force_die_on_attack
- **Type:** [[boolean]]
- **Optional**

### trigger_force
- **Type:** [[ForceCondition]]
- **Optional**

### allow_clone_connection
- **Type:** [[boolean]]
- **Optional**

### allow_blueprint_connection
- **Type:** [[boolean]]
- **Optional**

### allow_side_loading
- **Type:** [[boolean]]
- **Optional**

### allow_rail_interaction
- **Type:** [[boolean]]
- **Optional**

### allow_container_interaction
- **Type:** [[boolean]]
- **Optional**

### energy_per_item
- **Type:** [[double]]
- **Optional**

### max_snap_to_train_stop_distance
- **Type:** [[float]]
- **Optional**

### shuffle_resources_to_mine
- **Type:** [[boolean]]
- **Optional**

### remove_on_tile_collision
- **Type:** [[boolean]]
- **Optional**

### particle
- **Type:** [[LuaParticlePrototype]]
- **Optional**

### particle_time_to_live
- **Type:** [[DeviatedValue]]
- **Optional**

### particle_time_before_start
- **Type:** [[DeviatedValue]]
- **Optional**

### particle_height
- **Type:** [[DeviatedValue]]
- **Optional**

### particle_vertical_speed
- **Type:** [[DeviatedValue]]
- **Optional**

### particle_horizontal_speed
- **Type:** [[DeviatedValue]]
- **Optional**

### rotatable
- **Type:** [[boolean]]
- **Optional**

### direction_only
- **Type:** [[boolean]]
- **Optional**

### hit_at_collision_position
- **Type:** [[boolean]]
- **Optional**

### piercing_damage
- **Type:** [[float]]
- **Optional**

### acceleration
- **Type:** [[double]]
- **Optional**

### turn_speed
- **Type:** [[float]]
- **Optional**

### speed_modifier
- **Type:** [[Vector]]
- **Optional**

### hit_collision_mask
- **Type:** [[CollisionMask]]
- **Optional**

### turning_speed_increases_exponentially_with_projectile_speed
- **Type:** [[boolean]]
- **Optional**

### fluid_wagon_connector_speed
- **Type:** [[double]]
- **Optional**

### fluid_wagon_tank_valve_max_distance
- **Type:** [[double]]
- **Optional**

### energy_per_sector
- **Type:** [[double]]
- **Optional**

### energy_per_nearby_scan
- **Type:** [[double]]
- **Optional**

### connects_to_other_radars
- **Type:** [[boolean]]
- **Optional**

### energy_fraction_to_connect
- **Type:** [[float]]
- **Optional**

### energy_fraction_to_disconnect
- **Type:** [[float]]
- **Optional**

### default_universe_channel
- **Type:** [[SignalID]]
- **Optional**

### default_red_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_orange_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_green_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_blue_output_signal
- **Type:** [[SignalID]]
- **Optional**

### collision_mask_allow_on_deep_oil_ocean
- **Type:** [[CollisionMask]]
- **Optional**

### related_rail
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### not_buildable_if_no_rails
- **Type:** [[boolean]]
- **Optional**

### snap_to_spots_distance
- **Type:** [[float]]
- **Optional**

### elevated_selection_boxes
- **Type:** array<[[BoundingBox]]>
- **Optional**

### meltdown_action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### scale_energy_usage
- **Type:** [[boolean]]
- **Optional**

### default_temperature_signal
- **Type:** [[SignalID]]
- **Optional**

### map_grid
- **Type:** [[boolean]]
- **Optional**

### resource_patch_search_radius
- **Type:** [[uint32]]
- **Optional**

### tree_removal_probability
- **Type:** [[double]]
- **Optional**

### cliff_removal_probability
- **Type:** [[double]]
- **Optional**

### tree_removal_max_distance
- **Type:** [[double]]
- **Optional**

### recharge_minimum
- **Type:** [[double]]
- **Optional**

### open_door_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### close_door_trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### default_available_logistic_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_total_logistic_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_available_construction_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_total_construction_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_roboport_count_output_signal
- **Type:** [[SignalID]]
- **Optional**

### cargo_pod_entity
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### flying_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### rocket_parts_storage_cap
- **Type:** [[uint32]]
- **Optional**

### rocket_quick_relaunch_start_offset
- **Type:** [[double]]
- **Optional**

### rocket_rising_speed_modifier_per_quality_level
- **Type:** [[double]]
- **Optional**

### rocket_engine_starting_speed_modifier_per_quality_level
- **Type:** [[double]]
- **Optional**

### arms_speed_modifier_per_quality_level
- **Type:** [[double]]
- **Optional**

### alarm_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### clamps_on_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### clamps_off_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### doors_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### raise_rocket_trigger
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### can_launch_without_landing_pads
- **Type:** [[boolean]]
- **Optional**

### default_launched_signal
- **Type:** [[SignalID]]
- **Optional**

### default_game_tick_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_day_tick_output_signal
- **Type:** [[SignalID]]
- **Optional**

### default_day_length_output_signal
- **Type:** [[SignalID]]
- **Optional**

### action
- **Type:** array<[[TriggerItem]]>
- **Optional**

### action_cooldown
- **Type:** [[uint32]]
- **Optional**

### particle_count
- **Type:** [[uint8]]
- **Optional**

### attach_to_target
- **Type:** [[boolean]]
- **Optional**

### exchange_input_lines
- **Type:** [[boolean]]
- **Optional**

### exchange_output_lines
- **Type:** [[boolean]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### has_flag
Test whether this entity prototype has a certain flag set.

**Parameters:**
- **`flag`** — [[EntityPrototypeFlag]]: The flag to test.

**Returns:**
- [[boolean]]: `true` if this prototype has the given flag set.

### get_inventory_size
Gets the base size of the given inventory on this entity or `nil` if the given inventory doesn't exist.

**Parameters:**
- **`index`** — [[defines.inventory]]
- **`quality`** — [[QualityID]] *(optional)*: Defaults to `"normal"`.

**Returns:**
- [[ItemStackIndex]] *(optional)*

### get_crafting_speed
The crafting speed of this crafting-machine or character.
*Only available on:* `CraftingMachine`, `Character`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_supply_area_distance
The supply area of this electric pole or beacon prototype.
*Only available on:* `ElectricPole`, `Beacon`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_max_wire_distance
The maximum wire distance for this entity. 0 if the entity doesn't support wires.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]

### get_max_circuit_wire_distance
The maximum circuit wire distance for this entity. 0 if the entity doesn't support circuit wires.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]

### get_max_energy_usage
The theoretical maximum energy usage for this entity.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]

### get_max_energy_production
The theoretical maximum energy production for this entity.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]

### get_max_energy
The max energy for this flying robot prototype.
*Only available on:* `FlyingRobot`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_inserter_extension_speed
The extension speed of this inserter.
*Only available on:* `Inserter`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_inserter_rotation_speed
The rotation speed of this inserter.
*Only available on:* `Inserter`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_researching_speed
The base researching speed of this lab prototype.
*Only available on:* `Lab`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_max_distance_of_sector_revealed
The radius of the area this radar can chart, in chunks.
*Only available on:* `Radar`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]] *(optional)*

### get_max_distance_of_nearby_sector_revealed
The radius of the area constantly revealed by this radar, or cargo landing pad, in chunks.
*Only available on:* `Radar`, `CargoLandingPad`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]] *(optional)*

### get_max_health
Max health of this entity. Will be `0` if this is not an entity with health.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[float]]

### get_fluid_usage_per_tick
The fluid usage of this generator, fusion generator or fusion reactor prototype.
*Only available on:* `Generator`, `FusionGenerator`, `FusionReactor`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_max_power_output
The maximum power output of this burner generator or generator prototype.
*Only available on:* `BurnerGenerator`, `Generator`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_pumping_speed
The pumping speed of this offshore pump or normal pump.
*Only available on:* `OffshorePump`, `Pump`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_valve_flow_rate
The maximum flow rate through this valve.
*Only available on:* `Valve`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_max_speed
The maximum speed of this rolling stock if defined.
*Only available on:* `RollingStock`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_duration
*Only available on:* `Sticker`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[uint32]] *(optional)*

### get_inventory_size_bonus
*Only available on:* `CargoBay`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[ItemStackIndex]] *(optional)*

### get_mining_drill_radius
The mining radius of this mining drill prototype.
*Only available on:* `MiningDrill`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_fluid_capacity
Gets the fluid capacity of this entity or 0 if this entity doesn't support fluids.

Crafting machines will report 0 due to their fluid capacity being whatever a given recipe needs.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]

### get_attraction_range_elongation
*Only available on:* `LightningAttractor`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*

### get_energy_distribution_efficiency
*Only available on:* `LightningAttractor`

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]] *(optional)*
