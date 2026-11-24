---
title: FluidPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# FluidPrototypeFilter

## Fields

### filter
- **Type:** `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"name"` | `"subgroup"` | `"default-temperature"` | `"max-temperature"` | `"heat-capacity"` | `"fuel-value"` | `"emissions-multiplier"` | `"gas-temperature"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
