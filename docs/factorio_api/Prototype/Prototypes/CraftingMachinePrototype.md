---
title: CraftingMachinePrototype
tags: [factorio-api, prototype]
---
# CraftingMachinePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

The abstract basis of the assembling machines and furnaces. Contains the properties that both of them have.

Note that a crafting machine cannot be rotated unless it has at least one of the following: a fluid box, a heat energy source, a fluid energy source, or a non-square collision box. Crafting machines with non-square collision boxes can only be rotated before placement, not after.

## Properties

### quality_affects_energy_usage
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set, [[QualityPrototype#crafting_machine_energy_usage_multiplier|QualityPrototype::crafting_machine_energy_usage_multiplier]] will be applied to energy_usage.

### energy_usage
- **Type:** [[Energy]]
Sets how much energy this machine uses while crafting. Energy usage has to be positive.
**Examples:**

```
energy_usage = "90kW"
```

### crafting_speed
- **Type:** [[double (type)]]
How fast this crafting machine can craft. 1 means that for example a 1 second long recipe take 1 second to craft. 0.5 means it takes 2 seconds, and 2 means it takes 0.5 seconds.

Crafting speed has to be positive.

### crafting_categories
- **Type:** array<[[RecipeCategoryID (type)]]>
A list of [[RecipeCategory|recipe categories]] this crafting machine can use.
**Examples:**

```
crafting_categories = {"crafting", "smelting"}
```

### energy_source
- **Type:** [[EnergySource]]
Defines how the crafting machine is powered.

When using an electric energy source and `drain` is not specified, it will be set to `energy_usage ÷ 30` automatically.

### fluid_boxes
- **Type:** array<[[FluidBox]]>
- **Optional**
The crafting machine's fluid boxes. If an assembling machine has fluid boxes *and* [[AssemblingMachinePrototype#fluid_boxes_off_when_no_fluid_recipe|AssemblingMachinePrototype::fluid_boxes_off_when_no_fluid_recipe]] is true, the assembling machine can only be rotated when a recipe consuming or producing fluid is set, or if it has one of the other properties listed at the top of this page.

For assembling machines, any [[FluidBox#filter|filters]] set on the fluidboxes are ignored.
**Examples:**

```
fluid_boxes =
{
  {
    production_type = "input",
    pipe_picture = assembler2pipepictures(),
    pipe_covers = pipecoverspictures(),
    volume = 1000,
    pipe_connections = {{ flow_direction = "input", direction = defines.direction.north, position = {0, -1} }},
    secondary_draw_orders = { north = -1 }
  },
  {
    production_type = "output",
    pipe_picture = assembler2pipepictures(),
    pipe_covers = pipecoverspictures(),
    volume = 1000,
    pipe_connections = {{ flow_direction = "output", direction = defines.direction.south, position = {0, 1} }},
    secondary_draw_orders = { north = -1 }
  },
}
```

### effect_receiver
- **Type:** [[EffectReceiver (type)]]
- **Optional**

### module_slots
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`
The number of module slots in this machine.

### quality_affects_module_slots
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#crafting_machine_module_slots_bonus|QualityPrototype::crafting_machine_module_slots_bonus]] will be added to module slots count.

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

### show_recipe_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the "alt-mode icon" should be drawn at all.

### return_ingredients_on_change
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Controls whether the ingredients of an in-progress recipe are destroyed when mining the machine/changing the recipe. If set to true, the ingredients do not get destroyed. This affects only the ingredients of the recipe that is currently in progress, so those that visually have already been consumed while their resulting product has not yet been produced.

### draw_entity_info_icon_background
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the "alt-mode icon" should have a black background.

### match_animation_speed_to_activity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the speed of the animation and working visualization should be based on the machine's speed (boosted or slowed by modules).

### show_recipe_icon_on_map
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the recipe icon should be shown on the map.

### fast_transfer_modules_into_module_slots_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### ignore_output_full
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### animation_random_start_frame
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true the starting frame will be randomized upon placement.

### graphics_set
- **Type:** [[CraftingMachineGraphicsSet]]
- **Optional**

### graphics_set_flipped
- **Type:** [[CraftingMachineGraphicsSet]]
- **Optional**

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed.

### production_health_effect
- **Type:** [[ProductionHealthEffect]]
- **Optional**

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**

### vector_to_place_result
- **Type:** [[Vector (type)]]
- **Optional**

### use_mirroring
- **Type:** [[boolean (type)]]
- **Optional**
Defaults to true if `vector_to_place_result` is given.

### crafting_speed_quality_multiplier
- **Type:** dictionary<[[QualityID (type)]] → [[double (type)]]>
- **Optional**
Each value must be >= 0.01.

If value is not provided for a quality, then [[QualityPrototype#crafting_machine_speed_multiplier|QualityPrototype::crafting_machine_speed_multiplier]] will be used as a speed multiplier instead.

### module_slots_quality_bonus
- **Type:** dictionary<[[QualityID (type)]] → [[ItemStackIndex (type)]]>
- **Optional**
If value is not provided for a quality, then [[QualityPrototype#crafting_machine_module_slots_bonus|QualityPrototype::crafting_machine_module_slots_bonus]] will be used as a module slots bonus instead.

Does nothing if [[CraftingMachinePrototype#quality_affects_module_slots|CraftingMachinePrototype::quality_affects_module_slots]] is not set.

### energy_usage_quality_multiplier
- **Type:** dictionary<[[QualityID (type)]] → [[double (type)]]>
- **Optional**
Each value must be >= 0.01.

If value is not provided for a quality, then [[QualityPrototype#crafting_machine_energy_usage_multiplier|QualityPrototype::crafting_machine_energy_usage_multiplier]] will be used as an energy usage multiplier instead.

Does nothing if [[CraftingMachinePrototype#quality_affects_energy_usage|CraftingMachinePrototype::quality_affects_energy_usage]] is not set.
