---
title: TurretSpecialEffect
tags: [factorio-api, prototype, type]
---
# TurretSpecialEffect

## Properties

### type
- **Type:** `"mask-by-circle"`

### center
- **Type:** [[TurretSpecialEffectCenter]]
- **Optional**

### min_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `type` is `"mask-by-circle"`.

### max_radius
- **Type:** [[float (type)]]
- **Optional**
Only loaded, and mandatory if `type` is `"mask-by-circle"`.

### falloff
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `type` is `"mask-by-circle"`.

### attacking_min_radius
- **Type:** [[float (type)]]
- **Optional**
Only loaded if `type` is `"mask-by-circle"`.

### attacking_max_radius
- **Type:** [[float (type)]]
- **Optional**
Only loaded if `type` is `"mask-by-circle"`.

### attacking_falloff
- **Type:** [[float (type)]]
- **Optional**
Only loaded if `type` is `"mask-by-circle"`.
