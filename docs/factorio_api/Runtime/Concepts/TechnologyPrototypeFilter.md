---
title: TechnologyPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# TechnologyPrototypeFilter

## Fields

### filter
- **Type:** `"enabled"` | `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"upgrade"` | `"visible-when-disabled"` | `"has-effects"` | `"has-prerequisites"` | `"research-unit-ingredient"` | `"unlocks-recipe"` | `"level"` | `"max-level"` | `"time"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
