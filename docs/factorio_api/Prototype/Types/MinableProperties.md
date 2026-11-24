---
title: MinableProperties
tags: [factorio-api, prototype, type]
---
# MinableProperties

The mining properties of objects. For formulas for the mining time, see [mining](https://wiki.factorio.com/Mining).

## Properties

### mining_time
- **Type:** [[double (type)]]
How many seconds are required to mine this object at 1 mining speed.

### include_in_show_counts
- **Type:** [[boolean (type)]]
- **Optional**

### transfer_entity_health_to_products
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### results
- **Type:** array<[[ProductPrototype]]>
- **Optional**
The items or fluids that are returned when this object is mined.

### result
- **Type:** [[ItemID (type)]]
- **Optional**
Only loaded if `results` is not defined.

Which item is dropped when this is mined. Cannot be empty. If you want the entity to not be minable, don't specify the minable properties, if you want it to be minable with no result item, don't specify the result at all.

### fluid_amount
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** `0`
The amount of fluid that is used up when this object is mined. If this is > 0, this object cannot be mined by hand.

### mining_particle
- **Type:** [[ParticleID (type)]]
- **Optional**
Name of a [[ParticlePrototype]]. Which set of particles to use.

### required_fluid
- **Type:** [[FluidID (type)]]
- **Optional**
Name of a [[FluidPrototype]]. The fluid that is used up when this object is mined.

### count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `results` is not defined.

How many of result are dropped.

### mining_trigger
- **Type:** [[Trigger]]
- **Optional**

## Examples

```
minable = { mining_time = 0.55, result = "wood", count = 4, mining_particle = "wooden-particle" }
```

```
minable =
{
  mining_time = 1,
  results =
  {
    {
      type = "fluid",
      name = "crude-oil",
      amount = 10
    }
  }
}
```
