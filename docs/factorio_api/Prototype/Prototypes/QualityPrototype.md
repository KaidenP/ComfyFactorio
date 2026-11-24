---
title: QualityPrototype
tags: [factorio-api, prototype]
---
# QualityPrototype

> **Parent:** [[Prototype]] · **Type name:** `quality` · **Instance limit:** 255

One quality step. Its effects are specified by the level and the various multiplier and bonus properties. Properties ending in `_multiplier` are applied multiplicatively to their base property, properties ending in `_bonus` are applied additively.

## Properties

### draw_sprite_by_default
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### color
- **Type:** [[Color (type)]]

### level
- **Type:** [[uint32 (type)]]
Requires Space Age to use level greater than `0`.

### next
- **Type:** [[QualityID (type)]]
- **Optional**

### next_probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Probability that a crafting machine affected by a 100% quality [[ModulePrototype#effect|effect from modules]] will cause quality to be increased.

Probability is scaled linearly with quality effect. E.g. for `next_probability = 1`, 100% quality effect means quality is always increased, at 50% quality effect the quality is increased 50% of the time and so on.

Must be >= 0.

### chain_probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** clamp(`next_probability * 0.1, 0, 1)`
Probability of additional quality increase happening after quality was increased to reach this quality in the same crafting/mining operation.

Must be in range `[0, 1]`.

### previous_probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Probability that a crafting machine affected by a -100% quality [[ModulePrototype#effect|effect from modules]] will cause quality to be decreased.

Probability is scaled linearly with quality effect. E.g. for `previous_probability = 1`, -100% quality effect means quality is always decreased, at -50% quality effect the quality is decreased 50% of the time and so on.

Must be >= 0.

Note: for a machine to have a negative quality effect, [[EffectReceiver (type)#quality_limits|EffectReceiver::quality_limits]] needs to be set.

### previous_chain_probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** clamp(`previous_probability * 0.1, 0, 1)`
Probability of additional quality decrease happening after quality was decreased to reach this quality in the same crafting/mining operation.

Must be in range `[0, 1]`.

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.

### beacon_power_usage_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be >= 0.01.

### mining_drill_resource_drain_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be in range `[0, 1]`.

### science_pack_drain_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be in range `[0, 1]`.

Only affects labs with [[LabPrototype#uses_quality_drain_modifier|LabPrototype::uses_quality_drain_modifier]] set.

### name
- **Type:** [[string (type)]]
- **Overrides parent**
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

Requires Space Age to create prototypes with name other than `normal` or `quality-unknown`.

### default_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + 0.3 * `level`
Must be >= 0.01.

### inserter_speed_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### fluid_wagon_capacity_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

Only affects fluid wagons with [[FluidWagonPrototype#quality_affects_capacity|FluidWagonPrototype::quality_affects_capacity]] set.

### inventory_size_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### cargo_wagon_inventory_size_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `inventory_size_multiplier`
Must be >= 0.01.

### locomotive_power_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + 0.01 * `level`
Must be >= 0.01.

### rolling_stock_max_speed_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + 0.01 * `level`
Must be >= 0.01.

### lab_research_speed_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### crafting_machine_speed_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

Will be ignored by crafting machines with [[CraftingMachinePrototype#crafting_speed_quality_multiplier|CraftingMachinePrototype::crafting_speed_quality_multiplier]] set.

### crafting_machine_energy_usage_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Must be >= 0.01.

Only affects crafting machines with [[CraftingMachinePrototype#quality_affects_energy_usage|CraftingMachinePrototype::quality_affects_energy_usage]] set.

Will be ignored by crafting machines with [[CraftingMachinePrototype#energy_usage_quality_multiplier|CraftingMachinePrototype::energy_usage_quality_multiplier]] set.

### logistic_cell_charging_energy_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### tool_durability_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + `level`
Must be >= 0.01.

Affects the durability of [[ToolPrototype|tool items]] like repair tools and armor.

### science_capacity_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `tool_durability_multiplier`
Must be >= 0.01.

Affects how much research will lab be able to do using item of that quality.

Only used for items that are not a [[ToolPrototype|tool]].

### accumulator_capacity_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + `level`
Must be >= 0.01.

### flying_robot_max_energy_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 1 + `level`
Must be >= 0.01.

### range_multiplier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** min(1 + 0.1 * `level`, 3)
Must be within `[1, 3]`.

Affects the range of [[AttackParameters (type)|attack parameters]], e.g. those used by combat robots, units, guns and turrets.

### asteroid_collector_collection_radius_bonus
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `level`
Must be >= 0.

Performance warning: the navigation has to pre-calculate ranges for the highest tier collector possible, so you should keep this collection radius within reasonable values.

### equipment_grid_width_bonus
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** Value of `level`

### equipment_grid_height_bonus
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** Value of `level`

### electric_pole_wire_reach_bonus
- **Type:** [[float (type)]]
- **Optional**
- **Default:** 2 * `level`
Must be >= 0.

### electric_pole_supply_area_distance_bonus
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `level`
Must be >= 0.

### beacon_supply_area_distance_bonus
- **Type:** [[float (type)]]
- **Optional**
- **Default:** clamp(`level`, 0, 64)
Only affects beacons with [[BeaconPrototype#quality_affects_supply_area_distance|BeaconPrototype::quality_affects_supply_area_distance]] set.

Must be >= 0 and <= 64.

### mining_drill_mining_radius_bonus
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects mining drills with [[MiningDrillPrototype#quality_affects_mining_radius|MiningDrillPrototype::quality_affects_mining_radius]] set.

Must be >= 0.

### module_consumption_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### module_speed_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### module_productivity_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### module_pollution_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### module_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

### spoil_ticks_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_multiplier`
Must be >= 0.01.

Only affects items with [[ItemPrototype#quality_affects_spoil_ticks|ItemPrototype::quality_affects_spoil_ticks]] set.

### logistic_cell_charging_station_count_bonus
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects roboports with [[RoboportPrototype#charging_station_count_affected_by_quality|RoboportPrototype::charging_station_count_affected_by_quality]] set.

Only affects roboport equipment with [[RoboportEquipmentPrototype#charging_station_count_affected_by_quality|RoboportEquipmentPrototype::charging_station_count_affected_by_quality]] set.

### beacon_module_slots_bonus
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects beacons with [[BeaconPrototype#quality_affects_module_slots|BeaconPrototype::quality_affects_module_slots]] set.

### crafting_machine_module_slots_bonus
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects crafting machines with [[CraftingMachinePrototype#quality_affects_module_slots|CraftingMachinePrototype::quality_affects_module_slots]] set.

Will be ignored by crafting machines with [[CraftingMachinePrototype#module_slots_quality_bonus|CraftingMachinePrototype::module_slots_quality_bonus]] set.

### mining_drill_module_slots_bonus
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects mining drills with [[MiningDrillPrototype#quality_affects_module_slots|MiningDrillPrototype::quality_affects_module_slots]] set.

### lab_module_slots_bonus
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** Value of `level`
Only affects labs with [[LabPrototype#quality_affects_module_slots|LabPrototype::quality_affects_module_slots]] set.
