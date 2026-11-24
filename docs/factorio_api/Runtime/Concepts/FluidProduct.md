---
title: FluidProduct
tags: [factorio-api, runtime, concept]
---
# FluidProduct

## Fields

### type
- **Type:** `"fluid"`

### name
- **Type:** [[string]]
Prototype name of the result.

### amount
- **Type:** [[double]]
- **Optional**
Amount of the fluid to give. If not returned, `amount_min` and `amount_max` will be present instead.

### amount_min
- **Type:** [[double]]
- **Optional**
Minimal amount of the fluid to give. Not returned if `amount` is returned.

### amount_max
- **Type:** [[double]]
- **Optional**
Maximum amount of the fluid to give. Not returned if `amount` is returned.

### independent_probability
- **Type:** [[double]]
A value in range `[0, 1]`. Fluid is only given with this probability; otherwise no product is produced.

### shared_probability
- **Type:** [[SharedProbabilityDefinition]]

### ignored_by_stats
- **Type:** [[double]]
- **Optional**
How much of this product is ignored by statistics.

### ignored_by_productivity
- **Type:** [[double]]
- **Optional**
How much of this product is ignored by productivity.

### temperature
- **Type:** [[float]]
- **Optional**
The fluid temperature of this product.

### fluidbox_index
- **Type:** [[uint32]]
- **Optional**

## Examples

```
-- Products of the "advanced-oil-processing" recipe
{{type="fluid", name="heavy-oil", amount=1},
  {type="fluid", name="light-oil", amount=4.5},
  {type="fluid", name="petroleum-gas", amount=5.5}}
```
