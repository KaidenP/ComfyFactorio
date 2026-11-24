---
title: LuaPreGhostDeconstructedEventFilter
tags: [factorio-api, runtime, concept]
---
# LuaPreGhostDeconstructedEventFilter

## Fields

### filter
- **Type:** `"ghost"` | `"rail"` | `"rail-signal"` | `"rolling-stock"` | `"robot-with-logistics-interface"` | `"vehicle"` | `"turret"` | `"crafting-machine"` | `"wall-connectable"` | `"transport-belt-connectable"` | `"circuit-network-connectable"` | `"type"` | `"name"` | `"ghost_type"` | `"ghost_name"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
