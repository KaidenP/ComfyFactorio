---
title: StatelessVisualisation
tags: [factorio-api, prototype, type]
---
# StatelessVisualisation

## Properties

### animation
- **Type:** [[AnimationVariations]]
- **Optional**
One of `nested_visualisations`, `animation` and `light` needs to be defined.

### shadow
- **Type:** [[AnimationVariations]]
- **Optional**
Shadow variation count must be equal to animation variation count.

Only loaded if `animation` is defined.

### light
- **Type:** [[LightDefinition]]
- **Optional**
One of `nested_visualisations`, `animation` and `light` needs to be defined.

### count
- **Type:** [[uint16 (type)]]
- **Optional**

### min_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `1`
Only loaded if `count` is not defined.

### max_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** Value of `min_count`
Only loaded if `count` is not defined.

### period
- **Type:** [[uint16 (type)]]
- **Optional**

### particle_tick_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Silently clamped to be between 0 and 1.

### offset_x
- **Type:** [[RangedValue]]
- **Optional**

### offset_y
- **Type:** [[RangedValue]]
- **Optional**

### offset_z
- **Type:** [[RangedValue]]
- **Optional**

### speed_x
- **Type:** [[RangedValue]]
- **Optional**

### speed_y
- **Type:** [[RangedValue]]
- **Optional**

### speed_z
- **Type:** [[RangedValue]]
- **Optional**

### acceleration_x
- **Type:** [[float (type)]]
- **Optional**

### acceleration_y
- **Type:** [[float (type)]]
- **Optional**

### acceleration_z
- **Type:** [[float (type)]]
- **Optional**

### movement_slowdown_factor_x
- **Type:** [[float (type)]]
- **Optional**
Silently clamped to be between 0 and 1.

### movement_slowdown_factor_y
- **Type:** [[float (type)]]
- **Optional**
Silently clamped to be between 0 and 1.

### movement_slowdown_factor_z
- **Type:** [[float (type)]]
- **Optional**
Silently clamped to be between 0 and 1.

### scale
- **Type:** [[RangedValue]]
- **Optional**

### begin_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### end_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### fade_in_progress_duration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### fade_out_progress_duration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### spread_progress_duration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### adjust_animation_speed_by_base_scale
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### affected_by_wind
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### positions
- **Type:** array<[[Vector (type)]]>
- **Optional**
Array may be at most 32 elements.

### nested_visualisations
- **Type:** [[StatelessVisualisation]] | array<[[StatelessVisualisation]]>
- **Optional**
One of `nested_visualisations`, `animation` and `light` needs to be defined.

### can_lay_on_the_ground
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
