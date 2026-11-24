---
title: CoverGraphicProcessionLayer
tags: [factorio-api, prototype, type]
---
# CoverGraphicProcessionLayer

Draws a layer of cloud texture covering the screen. It can fade in an out based on opacity and using the picture mask as gradient of areas which fade in soon or later.

There are two important concepts to understand:

- `mask` refers to something like a depth texture. It is applied across the whole screen and determines how the entire graphic fades in and out.

- `effect` in this context refers to clipping out portion of the cover graphic. It can use an effect_graphic. `is_cloud_effect_advanced` makes the `effect` modify opacity threshold of the `mask` rather than multiplying alpha.

Additionally an area can be masked out by range or effect mask.

## Properties

### type
- **Type:** `"cover-graphic"`

### reference_group
- **Type:** [[ProcessionLayerInheritanceGroupID]]
- **Optional**
The group this layer belongs to, for inheritance.

### inherit_from
- **Type:** [[ProcessionLayerInheritanceGroupID]]
- **Optional**
Adds the final position value from given layer to this one.

### graphic
- **Type:** [[ProcessionGraphic]]
- **Optional**
Main texture of the layer.

### mask_graphic
- **Type:** [[ProcessionGraphic]]
- **Optional**
Opacity gradient of the layer.

### effect_graphic
- **Type:** [[ProcessionGraphic]]
- **Optional**
Used by certain effects.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### is_cloud_effect_advanced
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Advanced cloud effect mask modifies the regular mask thresholds instead of being a flat multiplication of the resulting opacity.

### is_quad_texture
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
The texture and mask are interpreted as four smaller textures that are randomly tiled.

### rotate_with_pod
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Add rotation of the pod to the cloud rotation.

### texture_relative_to
- **Type:** [[EffectRelativeTo]]
- **Optional**
- **Default:** `"ground-origin"`
Where the tiled texture is centered and rotated.

### distance_traveled_strength
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** {0,0}
How much the pod's distance traveled moves the cloud coordinates

### pod_movement_strength
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** {1,1}
How much the pod's position moves the cloud coordinates

### world_size
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** {512, 512}
Size the textures are scaled to in the world.

### effect
- **Type:** [[CoverGraphicEffectData]]
- **Optional**
Clips the graphic.

### alt_effect
- **Type:** [[CoverGraphicEffectData]]
- **Optional**
Clips the graphic.

### frames
- **Type:** array<[[CoverGraphicProcessionLayerBezierControlPoint]]>
Default values if unspecified:

- opacity : 1.0

- rotation : 0.0

- effect_scale_min : 0.0

- effect_scale_max : 1.0

- effect_shift : {0, 0}

- alt_effect_scale_min : 0.0

- alt_effect_scale_max : 1.0

- alt_effect_shift : {0, 0}

- offset : {0, 0}
