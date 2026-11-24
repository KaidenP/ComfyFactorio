---
title: LuaQualityPrototype
tags: [factorio-api, runtime, class]
---
# LuaQualityPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a quality.

## Attributes

### color
- **Type:** [[Color]]
The color of the prototype

### level
- **Type:** [[uint32]]
Level basically specifies the stat-increasing value of this quality level.

### next
- **Type:** [[LuaQualityPrototype]]
- **Optional**
The next higher level of the quality

### next_probability
- **Type:** [[double]]
The probability multiplier of getting the next level of quality.

### chain_probability
- **Type:** [[double]]
Probability of additional quality increase happening after quality was increased to reach this quality in the same crafting/mining operation.

### previous
- **Type:** [[LuaQualityPrototype]]
- **Optional**

### previous_probability
- **Type:** [[double]]
The probability multiplier of getting the previous level of quality.

### previous_chain_probability
- **Type:** [[double]]
Probability of additional quality decrease happening after quality was decreased to reach this quality in the same crafting/mining operation.

### draw_sprite_by_default
- **Type:** [[boolean]]

### beacon_power_usage_multiplier
- **Type:** [[float]]

### mining_drill_resource_drain_multiplier
- **Type:** [[float]]

### science_pack_drain_multiplier
- **Type:** [[float]]

### default_multiplier
- **Type:** [[double]]

### inserter_speed_multiplier
- **Type:** [[double]]

### fluid_wagon_capacity_multiplier
- **Type:** [[double]]

### inventory_size_multiplier
- **Type:** [[double]]

### cargo_wagon_inventory_size_multiplier
- **Type:** [[double]]

### locomotive_power_multiplier
- **Type:** [[double]]

### rolling_stock_max_speed_multiplier
- **Type:** [[double]]

### lab_research_speed_multiplier
- **Type:** [[double]]

### crafting_machine_speed_multiplier
- **Type:** [[double]]

### crafting_machine_energy_usage_multiplier
- **Type:** [[double]]

### logistic_cell_charging_energy_multiplier
- **Type:** [[double]]

### tool_durability_multiplier
- **Type:** [[double]]

### science_capacity_multiplier
- **Type:** [[double]]

### accumulator_capacity_multiplier
- **Type:** [[double]]

### flying_robot_max_energy_multiplier
- **Type:** [[double]]

### range_multiplier
- **Type:** [[double]]

### equipment_grid_width_bonus
- **Type:** [[int16]]

### equipment_grid_height_bonus
- **Type:** [[int16]]

### electric_pole_wire_reach_bonus
- **Type:** [[float]]

### electric_pole_supply_area_distance_bonus
- **Type:** [[float]]

### beacon_supply_area_distance_bonus
- **Type:** [[float]]

### mining_drill_mining_radius_bonus
- **Type:** [[float]]

### module_consumption_multiplier
- **Type:** [[float]]

### module_speed_multiplier
- **Type:** [[float]]

### module_productivity_multiplier
- **Type:** [[float]]

### module_pollution_multiplier
- **Type:** [[float]]

### module_quality_multiplier
- **Type:** [[float]]

### spoil_ticks_multiplier
- **Type:** [[float]]

### logistic_cell_charging_station_count_bonus
- **Type:** [[uint32]]

### asteroid_collector_collection_radius_bonus
- **Type:** [[uint32]]

### beacon_module_slots_bonus
- **Type:** [[ItemStackIndex]]

### crafting_machine_module_slots_bonus
- **Type:** [[ItemStackIndex]]

### mining_drill_module_slots_bonus
- **Type:** [[ItemStackIndex]]

### lab_module_slots_bonus
- **Type:** [[ItemStackIndex]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### roll_quality
Performs quality roll

**Parameters:**
- **`quality_effect`** — [[EffectValue]]: Strength of quality effect. Larger value makes it easier to roll better qualities.
- **`quality_seed`** — [[double]]: Random value in [0, 1) used to select result quality.
- **`force`** — [[ForceID]] *(optional)*: Force which is doing the quality roll. Used to select unlocked qualities. If not provided, all qualities are considered unlocked.

**Returns:**
- [[LuaQualityPrototype]]

### get_roll_chances
Computes probabilities of rolling various qualities given a quality effect

**Parameters:**
- **`quality_effect`** — [[EffectValue]]: Strength of quality effect. Larger value makes it easier to roll better qualities.
- **`force`** — [[ForceID]] *(optional)*: Force to select unlocked qualities. If not provided, all qualities are considered unlocked.

**Returns:**
- dictionary<[[string]] → [[double]]>: Roll chances per quality. Only positive values are listed. All values should sum to 1.
