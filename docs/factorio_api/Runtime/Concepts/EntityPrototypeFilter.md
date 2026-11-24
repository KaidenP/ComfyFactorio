---
title: EntityPrototypeFilter
tags: [factorio-api, runtime, concept]
---
# EntityPrototypeFilter

## Fields

### filter
- **Type:** `"flying-robot"` | `"robot-with-logistics-interface"` | `"rail"` | `"ghost"` | `"explosion"` | `"vehicle"` | `"crafting-machine"` | `"rolling-stock"` | `"turret"` | `"transport-belt-connectable"` | `"wall-connectable"` | `"buildable"` | `"placable-in-editor"` | `"clonable"` | `"selectable"` | `"hidden"` | `"hidden-in-factoriopedia"` | `"is-parameter"` | `"entity-with-health"` | `"building"` | `"fast-replaceable"` | `"uses-direction"` | `"minable"` | `"circuit-connectable"` | `"autoplace"` | `"blueprintable"` | `"item-to-place"` | `"name"` | `"type"` | `"collision-mask"` | `"flag"` | `"selection-priority"` | `"emissions-per-second"` | `"crafting-category"`
The condition to filter on.

### mode
- **Type:** `"or"` | `"and"`
- **Optional**
How to combine this with the previous filter. Defaults to `"or"`. When evaluating the filters, `"and"` has higher precedence than `"or"`.

### invert
- **Type:** [[boolean]]
- **Optional**
Inverts the condition. Default is `false`.
