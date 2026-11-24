---
title: InfinityPipeFilter
tags: [factorio-api, runtime, concept]
---
# InfinityPipeFilter

A single filter used by an infinity-pipe type entity.

## Fields

### name
- **Type:** [[string]]
Name of the fluid.

### percentage
- **Type:** [[double]]
- **Optional**
The fill percentage the pipe (for example `0.5` for 50%). Can't be negative.

### temperature
- **Type:** [[double]]
- **Optional**
The temperature of the fluid. Defaults to the default/minimum temperature of the fluid.

### mode
- **Type:** `"at-least"` | `"at-most"` | `"exactly"` | `"add"` | `"remove"`
- **Optional**
Defaults to `"at-least"`.
