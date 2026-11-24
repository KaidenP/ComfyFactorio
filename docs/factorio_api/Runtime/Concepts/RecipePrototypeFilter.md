---
title: RecipePrototypeFilter
tags: [factorio-api, runtime, concept]
---
# RecipePrototypeFilter

## Fields

### filter
- **Type:** `"enabled"` | `"hidden"` | `"hidden-from-flow-stats"` | `"hidden-from-player-crafting"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"allow-as-intermediate"` | `"allow-intermediates"` | `"allow-decomposition"` | `"always-show-made-in"` | `"has-ingredients"` | `"has-products"` | `"has-ingredient-item"` | `"has-ingredient-fluid"` | `"has-product-item"` | `"has-product-fluid"` | `"subgroup"` | `"category"` | `"energy"` | `"emissions-multiplier"` | `"request-paste-multiplier"` | `"overload-multiplier"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
