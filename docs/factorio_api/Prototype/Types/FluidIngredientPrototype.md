---
title: FluidIngredientPrototype
tags: [factorio-api, prototype, type]
---
# FluidIngredientPrototype

A fluid ingredient definition.

## Properties

### type
- **Type:** `"fluid"`

### name
- **Type:** [[FluidID (type)]]
The name of a [[FluidPrototype]].

### amount
- **Type:** [[FluidAmount (type)]]
Can not be `<= 0`.

### temperature
- **Type:** [[float (type)]]
- **Optional**
Sets the expected temperature of the fluid ingredient.

### minimum_temperature
- **Type:** [[float (type)]]
- **Optional**
If `temperature` is not set, this sets the expected minimum temperature of the fluid ingredient.

### maximum_temperature
- **Type:** [[float (type)]]
- **Optional**
If `temperature` is not set, this sets the expected maximum temperature of the fluid ingredient.

### ignored_by_stats
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** `0`
Amount that should not be included in the consumption statistics, typically with a matching product having the same amount set as [[FluidProductPrototype#ignored_by_stats|ignored_by_stats]].

### fluidbox_index
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Used to specify which [[CraftingMachinePrototype#fluid_boxes|CraftingMachinePrototype::fluid_boxes]] this ingredient should use. It will use this one fluidbox. The index is 1-based and separate for input and output fluidboxes.

### optional_fluidbox_indexes
- **Type:** array<[[uint32 (type)]]>
- **Optional**
Additional fluid boxes that will be also used by this fluid ingredient. If a machine does not have a fluid box with that index, then this index will be silently skipped without making recipe uncraftable.

Only loaded if `fluidbox_index` is defined.

### fluidbox_multiplier
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `3`
Used to set crafting machine fluidbox volumes. Must be at least 1.

## Examples

```
{type="fluid", name="water", amount=50}
```
