---
title: FusionReactorGraphicsSet
tags: [factorio-api, prototype, type]
---
# FusionReactorGraphicsSet

## Properties

### structure
- **Type:** [[Sprite4Way]]
- **Optional**

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### default_fuel_glow_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{1, 1, 1}`

### light
- **Type:** [[LightDefinition]]
- **Optional**

### working_light_pictures
- **Type:** [[Sprite4Way]]
- **Optional**

### use_fuel_glow_color
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### fusion_effect_uv_map
- **Type:** [[Sprite]]
- **Optional**

### connections_graphics
- **Type:** array<[[FusionReactorConnectionGraphics]]>
- **Optional**

### direction_to_connections_graphics
- **Type:** dictionary<[[DirectionString]] → array<[[uint8 (type)]]>>
- **Optional**

### plasma_category
- **Type:** [[NeighbourConnectableConnectionCategory]]
Cannot be an empty string.

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
