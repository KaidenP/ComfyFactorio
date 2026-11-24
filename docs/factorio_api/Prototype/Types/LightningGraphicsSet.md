---
title: LightningGraphicsSet
tags: [factorio-api, prototype, type]
---
# LightningGraphicsSet

## Properties

### shader_configuration
- **Type:** array<[[LightningShaderConfiguration]]>
- **Optional**
If not empty, enables the lightning shader.

### bolt_half_width
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.005`

### bolt_midpoint_variance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.05`

### max_bolt_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.35`

### max_fork_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.9`

### min_relative_fork_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### max_relative_fork_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.7`

### fork_orientation_variance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.05`

### fork_intensity_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.7`
Cannot be 1.

### relative_cloud_fork_length
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.2`

### cloud_fork_orientation_variance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.015`

### min_ground_streamer_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2`

### max_ground_streamer_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `4`

### ground_streamer_variance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### cloud_forks
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `5`
Cannot be 255.

### cloud_detail_level
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `3`
Must be less than or equal to `bolt_detail_level`.

### bolt_detail_level
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `6`

### cloud_background
- **Type:** [[Animation]]
- **Optional**

### explosion
- **Type:** [[AnimationVariations]]
- **Optional**

### attractor_hit_animation
- **Type:** [[Animation]]
- **Optional**

### ground_streamers
- **Type:** array<[[Animation]]>
- **Optional**

### light
- **Type:** [[LightDefinition]]
- **Optional**

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
