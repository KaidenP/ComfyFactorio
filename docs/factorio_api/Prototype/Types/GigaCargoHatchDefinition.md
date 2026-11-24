---
title: GigaCargoHatchDefinition
tags: [factorio-api, prototype, type]
---
# GigaCargoHatchDefinition

## Properties

### hatch_graphics_back
- **Type:** [[Animation]]
- **Optional**

### hatch_graphics_front
- **Type:** [[Animation]]
- **Optional**

### hatch_render_layer_back
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"higher-object-under"`

### hatch_render_layer_front
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"higher-object-above"`

### covered_hatches
- **Type:** array<[[uint32 (type)]]>

### opening_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.

### closing_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.
