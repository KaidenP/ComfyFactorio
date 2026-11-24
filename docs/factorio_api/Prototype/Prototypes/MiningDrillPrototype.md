---
title: MiningDrillPrototype
tags: [factorio-api, prototype]
---
# MiningDrillPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `mining-drill`

A mining drill for automatically extracting resources from [[ResourceEntityPrototype|resource entities]]. This prototype type is used by [burner mining drill](https://wiki.factorio.com/Burner_mining_drill), [electric mining drill](https://wiki.factorio.com/Electric_mining_drill) and [pumpjack](https://wiki.factorio.com/Pumpjack) in vanilla.

## Properties

### vector_to_place_result
- **Type:** [[Vector (type)]]
The position where any item results are placed, when the mining drill is facing north (default direction). If the drill does not produce any solid items but uses a fluidbox output instead (e.g. pumpjacks), a vector of `{0,0}` disables the yellow arrow alt-mode indicator for the placed item location.

### use_mirroring
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### require_resources_to_place
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### resource_searching_radius
- **Type:** [[double (type)]]
The distance from the center of the mining drill to search for resources in.

This is 2.49 for electric mining drills (a 5x5 area) and 0.99 for burner mining drills (a 2x2 area). The drill searches resource outside its natural boundary box, which is 0.01 (the middle of the entity); making it 2.5 and 1.0 gives it another block radius.

### resource_searching_offset
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Offset of the `resource_searching_radius` from the entity center when the mining drill is facing north.

### energy_usage
- **Type:** [[Energy]]
The amount of energy used by the drill while mining. Can't be less than or equal to 0.
**Examples:**

```
energy_usage = "150kW"
```

### mining_speed
- **Type:** [[double (type)]]
The speed of this drill.

### energy_source
- **Type:** [[EnergySource]]
The energy source of this mining drill.

### resource_categories
- **Type:** array<[[ResourceCategoryID]]>
The names of the [[ResourceCategory]] that can be mined by this drill. For a list of built-in categories, see [here](https://wiki.factorio.com/Data.raw#resource-category).

Note: Categories containing resources which produce items, fluids, or items+fluids may be combined on the same entity, but may not work as expected. Examples: Miner does not rotate fluid-resulting resources until depletion. Fluid isn't output (fluid resource change and fluidbox matches previous fluid). Miner with no `vector_to_place_result` can't output an item result and halts.

### output_fluid_box
- **Type:** [[FluidBox]]
- **Optional**

### input_fluid_box
- **Type:** [[FluidBox]]
- **Optional**

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
Only loaded if `input_fluid_box` is defined. If specified, an input fluid below this temperature will cause the mining drill to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
Only loaded if `input_fluid_box` is defined. If specified, an input fluid above this temperature will cause the mining drill to stop working.

### graphics_set
- **Type:** [[MiningDrillGraphicsSet]]
- **Optional**

### graphics_set_flipped
- **Type:** [[MiningDrillGraphicsSet]]
- **Optional**

### wet_mining_graphics_set
- **Type:** [[MiningDrillGraphicsSet]]
- **Optional**

### wet_mining_graphics_set_flipped
- **Type:** [[MiningDrillGraphicsSet]]
- **Optional**

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed.

### effect_receiver
- **Type:** [[EffectReceiver (type)]]
- **Optional**

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
- **Default:** All effects are allowed
Sets the [[ModulePrototype|modules]] and [[BeaconPrototype|beacon]] effects that are allowed to be used on this mining drill.

### allowed_module_categories
- **Type:** array<[[ModuleCategoryID]]>
- **Optional**
- **Default:** All module categories are allowed
Sets the [[ModuleCategory|module categories]] that are allowed to be inserted into this machine.

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**
The sprite used to show the range of the mining drill.

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

### resource_drain_rate_percent
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `100`
May not be `0` or larger than `100`.

### shuffle_resources_to_mine
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### drops_full_belt_stacks
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Requires:** `space_age`

### uses_force_mining_productivity_bonus
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### quality_affects_mining_radius
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#mining_drill_mining_radius_bonus|QualityPrototype::mining_drill_mining_radius_bonus]] will be added to resource_searching_radius.

### moving_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### drilling_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### drilling_sound_animation_start_frame
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### drilling_sound_animation_end_frame
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### monitor_visualization_tint
- **Type:** [[Color (type)]]
- **Optional**
When this mining drill is connected to the circuit network, the resource that it is reading (either the entire resource patch, or the resource in the mining area of the drill, depending on circuit network setting), is tinted in this color when mousing over the mining drill.

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### circuit_connector_flipped
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### filter_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
How many filters this mining drill has. Maximum count of filtered resources in a mining drill is 5.

### migrate_horizontal_mirroring
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When a save file from version 2.0.x or older is loaded and this property is `true`, entities facing east or west direction are migrated to flipped state.
