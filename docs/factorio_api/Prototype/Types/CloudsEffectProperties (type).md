---
title: CloudsEffectProperties
tags: [factorio-api, prototype, type]
---
# CloudsEffectProperties

*Note: `CloudsEffectProperties (type)`.*

## Properties

### shape_noise_texture
- **Type:** [[EffectTexture]]

### detail_noise_texture
- **Type:** [[EffectTexture]]

### warp_sample_1
- **Type:** [[CloudsTextureCoordinateTransformation]]

### warp_sample_2
- **Type:** [[CloudsTextureCoordinateTransformation]]

### warped_shape_sample
- **Type:** [[CloudsTextureCoordinateTransformation]]

### additional_density_sample
- **Type:** [[CloudsTextureCoordinateTransformation]]

### detail_sample_1
- **Type:** [[CloudsTextureCoordinateTransformation]]

### detail_sample_2
- **Type:** [[CloudsTextureCoordinateTransformation]]

### scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### movement_speed_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.75`

### shape_warp_strength
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.06`

### shape_warp_weight
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.4`

### opacity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.25`

### opacity_at_night
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### density
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### density_at_night
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `density`

### detail_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.5`

### detail_factor_at_night
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `detail_factor`

### shape_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-1`

### detail_exponent
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### detail_sample_morph_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `256`
When set to 0, detail textures are not being "morphed" to each other, but lerped with ratio 0.5 instead.
