---
title: SpaceLocationPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# SpaceLocationPrototypeFilter

## Fields

### filter
- **Type:** `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"fly-condition"` | `"type"` | `"solar-power-in-space"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
