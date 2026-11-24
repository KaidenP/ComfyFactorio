---
title: ItemPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# ItemPrototypeFilter

## Fields

### filter
- **Type:** `"tool"` | `"mergeable"` | `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"item-with-inventory"` | `"selection-tool"` | `"item-with-label"` | `"has-rocket-launch-products"` | `"fuel"` | `"used-by-labs"` | `"place-result"` | `"burnt-result"` | `"place-as-tile"` | `"placed-as-equipment-result"` | `"plant-result"` | `"spoil-result"` | `"name"` | `"type"` | `"flag"` | `"subgroup"` | `"fuel-category"` | `"stack-size"` | `"fuel-value"` | `"fuel-acceleration-multiplier"` | `"fuel-top-speed-multiplier"` | `"fuel-emissions-multiplier"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
