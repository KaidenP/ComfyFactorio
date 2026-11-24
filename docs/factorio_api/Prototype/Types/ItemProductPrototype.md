---
title: ItemProductPrototype
tags: [factorio-api, prototype, type]
---
# ItemProductPrototype

> **Parent:** [[ProductPrototypeBase]]

An item product definition.

## Properties

### type
- **Type:** `"item"`

### name
- **Type:** [[ItemID (type)]]
The name of an [[ItemPrototype]].

### amount
- **Type:** [[uint16 (type)]]
- **Optional**

### amount_min
- **Type:** [[uint16 (type)]]
- **Optional**
Only loaded, and mandatory if `amount` is not defined.

### amount_max
- **Type:** [[uint16 (type)]]
- **Optional**
Only loaded, and mandatory if `amount` is not defined.

If set to a number that is less than `amount_min`, the game will use `amount_min` instead.

### ignored_by_stats
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Amount that should not be included in the item production statistics, typically with a matching ingredient having the same amount set as [[ItemIngredientPrototype#ignored_by_stats|ignored_by_stats]].

If `ignored_by_stats` is larger than the amount crafted (for instance due to probability) it will instead show as consumed.

Products with `ignored_by_stats` defined will not be set as recipe through the circuit network when using the product's item-signal.

### ignored_by_productivity
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** Value of `ignored_by_stats`
Amount that should be deducted from any productivity induced bonus crafts.

This value can safely be set larger than the maximum expected craft amount, any excess is ignored.

This value is ignored when [[RecipePrototype#allow_productivity|allow_productivity]] is `false`.

### extra_count_fraction
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Probability that a craft will yield one additional product. Also applies to bonus crafts caused by productivity.

### percent_spoiled
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Must be >= `0` and < `1`.

### always_fresh
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, the item produced will be produced fresh (using percent_spoiled) even when ingredients were spoiled.

Note: This may not work as expected outside of recipes (e.g. in mining drills).

### reset_freshness_on_craft
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, if the recipe successfully finishes crafting without spoiling, the result is produced fresh (non-spoiled).

Note: This may not work as expected outside of recipes (e.g. in mining drills).

### quality_min
- **Type:** [[QualityID (type)]]
- **Optional**
Lowest possible quality of item that will be given. If not provided but `quality_max` is given, it will be set to the lowest quality from a quality chain to which `quality_max` belongs. When set, if the recipe would produce items from a different quality chain (due to quality of the recipe or quality roll), `quality_min` will be used for the quality instead.

Note: If this is used outside of recipes (e.g. by mining drills), setting this to a custom quality chain will discard the quality roll.

### quality_max
- **Type:** [[QualityID (type)]]
- **Optional**
Highest possible quality of item that will be given. If not provided but `quality_min` is given, it will be set to the highest quality from a quality chain to which `quality_min` belongs. Must belong to the same quality chain as `quality_min` and be equal or better, meaning later in the chain when following [[QualityPrototype#next|QualityPrototype::next]].

Note: If this is used outside of recipes (e.g. by mining drills), setting this to a custom quality chain will discard the quality roll.

### quality_change
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
Amount of quality levels up or down this product will be adjusted.

This is the difference between the quality of the recipe and the quality of the product. For a vanilla example, when epic is selected for recipe quality, a product with quality change `1` would be legendary quality, not epic.

Note: This may not work as expected outside of recipes (e.g. in mining drills).

### affected_by_quality
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether quality roll affects quality of products given. If set to `false`, result of a quality roll will be ignored and an item of quality based on quality of selected recipe will be given.

Note: This may not work as expected outside of recipes (e.g. in mining drills).
