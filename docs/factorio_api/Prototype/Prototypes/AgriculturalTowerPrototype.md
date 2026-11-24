---
title: AgriculturalTowerPrototype
tags: [factorio-api, prototype]
---
# AgriculturalTowerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `agricultural-tower` · **Requires:** `space_age`

## Properties

### graphics_set
- **Type:** [[CraftingMachineGraphicsSet]]
- **Optional**

### crane
- **Type:** [[AgriculturalCraneProperties]]

### energy_source
- **Type:** [[EnergySource]]

### input_inventory_size
- **Type:** [[ItemStackIndex (type)]]

### output_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

### energy_usage
- **Type:** [[Energy]]
The amount of energy this agricultural tower uses for each planted or harvested [[PlantPrototype|plant]].

### crane_energy_usage
- **Type:** [[Energy]]
The amount of energy this agricultural tower uses while the crane is moving.

### radius
- **Type:** [[double (type)]]
The radius represents [[AgriculturalTowerPrototype#growth_grid_tile_size|grid tiles]] which are created around the agricultural tower from its [[EntityPrototype#collision_box|collision box]].

Must be positive.

### growth_grid_tile_size
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `3`
The size of one grid tile a [[PlantPrototype|plant]] is planted into.

Must be positive.

### growth_area_radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.95`
The minimum radius of empty space a [[PlantPrototype|plant]] requires around it to be planted.

Must be greater than or equal to 0 and less than or equal to `growth_grid_tile_size / 2`.

### random_growth_offset
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.25`
The maximum offset from the grid tile center which will be applied to the planting spot selected by this agricultural tower.

Must be greater than or equal to 0 and less than 1.

### randomize_planting_tile
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the agricultural tower will start from a random grid tile when given a planting task.

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**

### central_orienting_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### arm_extending_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### grappler_orienting_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### grappler_extending_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### planting_sound
- **Type:** [[Sound]]
- **Optional**

### harvesting_sound
- **Type:** [[Sound]]
- **Optional**

### central_orienting_sound_source
- **Type:** [[string (type)]]
- **Optional**

### arm_extending_sound_source
- **Type:** [[string (type)]]
- **Optional**

### grappler_orienting_sound_source
- **Type:** [[string (type)]]
- **Optional**

### grappler_extending_sound_source
- **Type:** [[string (type)]]
- **Optional**

### planting_procedure_points
- **Type:** array<[[Vector3D (type)]]>
- **Optional**

### harvesting_procedure_points
- **Type:** array<[[Vector3D (type)]]>
- **Optional**

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

### accepted_seeds
- **Type:** array<[[ItemID (type)]]>
- **Optional**
When missing, all items with [[ItemPrototype#plant_result|plant result]] will be accepted. When provided, only items on this list that have plant result will be accepted.

### module_slots
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
The number of module slots in this machine.

### quality_affects_module_slots
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#mining_drill_module_slots_bonus|QualityPrototype::mining_drill_module_slots_bonus]] will be added to module slots count.

### allowed_effects
- **Type:** [[EffectTypeLimitation]]
- **Optional**
- **Default:** No effects are allowed
Sets the [[ModulePrototype|modules]] and [[BeaconPrototype|beacon]] effects that are allowed to be used on this machine.

### allowed_module_categories
- **Type:** array<[[ModuleCategoryID]]>
- **Optional**
- **Default:** All module categories are allowed
Sets the [[ModuleCategory|module categories]] that are allowed to be inserted into this machine.

### effect_receiver
- **Type:** [[EffectReceiver (type)]]
- **Optional**
