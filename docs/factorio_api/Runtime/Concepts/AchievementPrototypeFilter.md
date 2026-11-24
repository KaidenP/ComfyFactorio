---
title: AchievementPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# AchievementPrototypeFilter

## Fields

### filter
- **Type:** `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"allowed-without-fight"` | `"type"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
