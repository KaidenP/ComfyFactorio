---
title: SpiderTorsoGraphicsSet
tags: [factorio-api, prototype, type]
---
# SpiderTorsoGraphicsSet

## Properties

### base_animation
- **Type:** [[RotatedAnimation]]
- **Optional**

### shadow_base_animation
- **Type:** [[RotatedAnimation]]
- **Optional**
If no sprite flags are defined, then this animation is loaded and treated as a shadow by default.

### animation
- **Type:** [[RotatedAnimation]]
- **Optional**

### shadow_animation
- **Type:** [[RotatedAnimation]]
- **Optional**
If no sprite flags are defined, then this animation is loaded and treated as a shadow by default.

### base_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"higher-object-under"`

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"under-elevated"`

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
