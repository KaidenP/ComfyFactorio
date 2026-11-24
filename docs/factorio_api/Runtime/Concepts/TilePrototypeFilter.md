---
title: TilePrototypeFilter
tags: [factorio-api, runtime, concept]
---
# TilePrototypeFilter

## Fields

### filter
- **Type:** `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"minable"` | `"autoplace"` | `"blueprintable"` | `"item-to-place"` | `"collision-mask"` | `"walking-speed-modifier"` | `"vehicle-friction-modifier"` | `"decorative-removal-probability"` | `"absorptions-per-second"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
