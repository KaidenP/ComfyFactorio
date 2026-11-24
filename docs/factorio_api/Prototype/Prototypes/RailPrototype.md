---
title: RailPrototype
tags: [factorio-api, prototype]
---
# RailPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

The abstract base of all rail prototypes.

## Properties

### walking_sound
- **Type:** [[Sound]]
- **Optional**
Sound played when a character walks over this rail.

### pictures
- **Type:** [[RailPictureSet]]
- **Optional**

### fence_pictures
- **Type:** [[RailFenceGraphicsSet]]
- **Optional**

### extra_planner_penalty
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### extra_planner_goal_penalty
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### forced_fence_segment_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Must be 0, 2 or 4. Can't be non-zero if `fence_pictures` is defined.

### ending_shifts
- **Type:** array<[[Vector (type)]]>
- **Optional**

### deconstruction_marker_positions
- **Type:** array<[[Vector (type)]]>
- **Optional**

### removes_soft_decoratives
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### build_grid_size
- **Type:** `2`
- **Optional**
- **Default:** `2`
- **Overrides parent**
Has to be 2 for 2x2 grid.

### selection_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Overrides parent**
The rail [[EntityPrototype#selection_box|selection_boxes]] are automatically calculated from the collision boxes, which are hardcoded. So effectively the selection boxes also hardcoded.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `45`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
