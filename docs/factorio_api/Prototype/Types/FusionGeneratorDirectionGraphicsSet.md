---
title: FusionGeneratorDirectionGraphicsSet
tags: [factorio-api, prototype, type]
---
# FusionGeneratorDirectionGraphicsSet

## Properties

### animation
- **Type:** [[Animation]]
- **Optional**

### working_light
- **Type:** [[Animation]]
- **Optional**

### fusion_effect_uv_map
- **Type:** [[Sprite]]
- **Optional**

### fluid_input_graphics
- **Type:** array<[[FusionGeneratorFluidInputGraphics]]>
- **Optional**
The amount of items in this array has to match the amount of [[FusionGeneratorPrototype#input_fluid_box|input fluid connections]]. Empty tables can be used as items to fulfill this requirement without defining graphics.
