---
title: OffshorePumpGraphicsSet
tags: [factorio-api, prototype, type]
---
# OffshorePumpGraphicsSet

## Properties

### animation
- **Type:** [[Animation4Way]]
- **Optional**
Rendered in "object" layer, with secondary draw order 0.

### base_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"ground-patch"`

### underwater_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `1`

### fluid_animation
- **Type:** [[Animation4Way]]
- **Optional**
Rendered in "object" layer, with secondary draw order 20.

### glass_pictures
- **Type:** [[Sprite4Way]]
- **Optional**
Rendered in "object" layer, with secondary draw order 40.

### base_pictures
- **Type:** [[Sprite4Way]]
- **Optional**
Rendered in layer specified by `base_render_layer`, with secondary draw order 0.

### underwater_pictures
- **Type:** [[Sprite4Way]]
- **Optional**
Drawn by tile renderer when water animation is enabled.

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
