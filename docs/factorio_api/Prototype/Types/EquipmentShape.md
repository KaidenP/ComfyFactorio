---
title: EquipmentShape
tags: [factorio-api, prototype, type]
---
# EquipmentShape

The shape and dimensions of an equipment module.

## Properties

### width
- **Type:** [[uint32 (type)]]

### height
- **Type:** [[uint32 (type)]]

### type
- **Type:** `"full"` | `"manual"`
The shape. When using "manual", `points` must be defined.

### points
- **Type:** array<array<[[uint32 (type)]]>>
- **Optional**
Only used when when `type` is `"manual"`. Each inner array is a "position" inside width×height of the equipment. Each positions that is defined is a filled squares of the equipment shape. `{0, 0}` is the upper left corner of the equipment.
**Examples:**

```
-- A set of points which fall within the width/height - can't be empty
points =
{
  {0, 0}, {1, 0}, {2, 0}, {3, 0},
  {0, 1},                 {3, 1},
  {0, 2},                 {3, 2},
  {0, 3}, {1, 3}, {2, 3}, {3, 3}
}
```
