---
title: FluidProductPrototype
tags: [factorio-api, prototype, type]
---
# FluidProductPrototype

> **Parent:** [[ProductPrototypeBase]]

A fluid product definition.

## Properties

### type
- **Type:** `"fluid"`

### name
- **Type:** [[FluidID (type)]]
The name of a [[FluidPrototype]].

### amount
- **Type:** [[FluidAmount (type)]]
- **Optional**
Can not be `< 0`.

### amount_min
- **Type:** [[FluidAmount (type)]]
- **Optional**
Only loaded, and mandatory if `amount` is not defined.

Can not be `< 0`.

### amount_max
- **Type:** [[FluidAmount (type)]]
- **Optional**
Only loaded, and mandatory if `amount` is not defined.

If set to a number that is less than `amount_min`, the game will use `amount_min` instead.

### ignored_by_stats
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** `0`
Amount that should not be included in the fluid production statistics, typically with a matching ingredient having the same amount set as [[FluidIngredientPrototype#ignored_by_stats|ignored_by_stats]].

If `ignored_by_stats` is larger than the amount crafted (for instance due to probability) it will instead show as consumed.

Products with `ignored_by_stats` defined will not be set as recipe through the circuit network when using the product's fluid-signal.

### ignored_by_productivity
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** Value of `ignored_by_stats`
Amount that should be deducted from any productivity induced bonus crafts.

This value can safely be set larger than the maximum expected craft amount, any excess is ignored.

This value is ignored when [[RecipePrototype#allow_productivity|allow_productivity]] is `false`.

### temperature
- **Type:** [[float (type)]]
- **Optional**
The temperature of the fluid product.

### fluidbox_index
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Used to specify which [[CraftingMachinePrototype#fluid_boxes|CraftingMachinePrototype::fluid_boxes]] this product should use. It will use this one fluidbox. The index is 1-based and separate for input and output fluidboxes.

### fluidbox_multiplier
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `3`
Used to set crafting machine fluidbox volumes. Must be at least 1.

### optional_fluidbox_indexes
- **Type:** array<[[uint32 (type)]]>
- **Optional**
Additional fluid boxes that will be also used by this fluid product. If a machine does not have a fluid box with that index, then this index will be silently skipped without making recipe uncraftable.

Only loaded if `fluidbox_index` is defined.
