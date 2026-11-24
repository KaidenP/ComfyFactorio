---
title: ItemIngredientPrototype
tags: [factorio-api, prototype, type]
---
# ItemIngredientPrototype

An item ingredient definition.

## Properties

### type
- **Type:** `"item"`

### name
- **Type:** [[ItemID (type)]]

### amount
- **Type:** [[uint16 (type)]]
Cannot be `0`.

### ignored_by_stats
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Amount that should not be included in the consumption statistics, typically with a matching product having the same amount set as [[ItemProductPrototype#ignored_by_stats|ignored_by_stats]].

### quality_min
- **Type:** [[QualityID (type)]]
- **Optional**
Lowest possible quality of ingredient that will be accepted. If not provided but `quality_max` is given, it will be set to the lowest quality from a quality chain to which `quality_max` belongs. When set, if the recipe would require ingredient from a different quality chain (due to quality of the recipe or quality roll), `quality_min` will be used for the quality instead.

### quality_max
- **Type:** [[QualityID (type)]]
- **Optional**
Highest possible quality of ingredient that will be accepted. If not provided but `quality_min` is given, it will be set to the highest quality from a quality chain to which `quality_min` belongs. Must belong to the same quality chain as `quality_min` and be equal or better, meaning later in the chain when following [[QualityPrototype#next|QualityPrototype::next]].

### quality_change
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
Amount of quality levels up or down this ingredient will be adjusted.

This is the difference between the quality of the recipe and the quality of the ingredient. For a vanilla example, when legendary is selected for recipe quality, an ingredient with quality change `-1` would need to be epic quality, not legendary.

If `quality_min` is equal to `quality_max`, this is silently set to `0` as it does not make sense to define a quality jump when ingredient quality is fixed to one value for all qualities of recipe.

### spoil_weight
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Controls how much spoil percent of this ingredient should influence spoil percent of spoilable products.

Must be in range `[0, 1]`.

## Examples

```
{type="item", name="steel-plate", amount=8}
```

```
{type="item", name="iron-plate", amount=12}
```
