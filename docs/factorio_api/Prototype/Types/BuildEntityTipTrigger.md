---
title: BuildEntityTipTrigger
tags: [factorio-api, prototype, type]
---
# BuildEntityTipTrigger

> **Parent:** [[CountBasedTipTrigger]]

## Properties

### type
- **Type:** `"build-entity"`

### entity
- **Type:** [[EntityID (type)]]
- **Optional**

### match_type_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### build_by_dragging
- **Type:** [[boolean (type)]]
- **Optional**

### consecutive
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Building is considered consecutive when the built entity is the same as the last built entity.

### linear_power_pole_line
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### build_in_line
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### quality
- **Type:** [[QualityID (type)]]
- **Optional**
