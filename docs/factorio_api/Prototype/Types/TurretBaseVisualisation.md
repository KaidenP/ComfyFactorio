---
title: TurretBaseVisualisation
tags: [factorio-api, prototype, type]
---
# TurretBaseVisualisation

## Properties

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### enabled_states
- **Type:** array<[[TurretState]]>
- **Optional**
If not defined, visualisation will be drawn in all states.

### draw_when_has_energy
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_when_no_energy
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_when_has_ammo
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_when_no_ammo
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_when_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_when_not_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### animation
- **Type:** [[Animation4Way]]
