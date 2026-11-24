---
title: ItemProduct
tags: [factorio-api, runtime, concept]
---
# ItemProduct

## Fields

### type
- **Type:** `"item"`

### name
- **Type:** [[string]]
Prototype name of the result.

### amount
- **Type:** [[uint16]]
- **Optional**
Amount of the item to give. If not returned, `amount_min` and `amount_max` will be present instead.

### amount_min
- **Type:** [[uint16]]
- **Optional**
Minimal amount of the item to give. Not returned if `amount` is returned.

### amount_max
- **Type:** [[uint16]]
- **Optional**
Maximum amount of the item to give. Not returned if `amount` is returned.

### independent_probability
- **Type:** [[double]]
A value in range `[0, 1]`. Item is only given with this probability; otherwise no product is produced.

### shared_probability
- **Type:** [[SharedProbabilityDefinition]]

### ignored_by_stats
- **Type:** [[uint16]]
- **Optional**
How much of this product is ignored by statistics.

### ignored_by_productivity
- **Type:** [[uint16]]
- **Optional**
How much of this product is ignored by productivity.

### extra_count_fraction
- **Type:** [[float]]
- **Optional**
Probability that a craft will yield one additional product. Also applies to bonus crafts caused by productivity.

### percent_spoiled
- **Type:** [[float]]
- **Optional**

### always_fresh
- **Type:** [[boolean]]
- **Optional**

### reset_freshness_on_craft
- **Type:** [[boolean]]
- **Optional**

### quality_min
- **Type:** [[QualityID]]
- **Optional**

### quality_max
- **Type:** [[QualityID]]
- **Optional**

### quality_change
- **Type:** [[int8]]
- **Optional**

### affected_by_quality
- **Type:** [[boolean]]

## Examples

```
-- Products of the "steel-chest" recipe (an array of Product)
{{type="item", name="steel-chest", amount=1}}
```

```
-- What a custom recipe would look like that had a probability of 0.5 to return a
-- minimum amount of 1 and a maximum amount of 5
{{type="item", name="custom-item", independent_probability=0.5, amount_min=1, amount_max=5}}
```
