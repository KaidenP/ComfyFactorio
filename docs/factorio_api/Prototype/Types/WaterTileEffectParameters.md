---
title: WaterTileEffectParameters
tags: [factorio-api, prototype, type]
---
# WaterTileEffectParameters

## Properties

### shader_variation
- **Type:** [[EffectVariation]]
- **Optional**
- **Default:** `"water"`

### noise_textures
- **Type:** array<[[EffectTexture]]>
- **Optional**
Shader variants `"water"` and `"wetland-water"` must have 1 texture, and `"lava"` and `"oil"` must have 2 textures.

### image_textures
- **Type:** array<[[EffectArrayTexture]]>
- **Optional**
The image is split into 512x512 slices which are used as randomly chosen variations.

Shader variant `"water"` must have 0 textures, `"lava"` and `"wetland-water"` must have 1 texture, and `"oil"` must have 2 textures.

### specular_lightness
- **Type:** [[Color (type)]]
Affects specular lightness for `"water"` `shader_variation`. Affects panning/warping vector for all other `shader_variation`s.

Any alpha value set here is ignored and will always be `1` in the shader.

### foam_color
- **Type:** [[Color (type)]]
Affects foam color for `"water"` `shader_variation`. Affects panning/warping vector for all other `shader_variation`s.

Any alpha value set here is ignored and will always be `1` in the shader.

### foam_color_multiplier
- **Type:** [[float (type)]]
Multiplies the rgb values of `foam_color` before they are passed to the shader.

### tick_scale
- **Type:** [[float (type)]]
Affects distortion speed for `"water"` `shader_variation`. Affects panning/warping speed for all other `shader_variation`s.

### animation_speed
- **Type:** [[float (type)]]
Affects distortion speed for `"water"` `shader_variation`. Affects panning/warping speed for all other `shader_variation`s.

### animation_scale
- **Type:** [[float (type)]] | ([[float (type)]], [[float (type)]])
Affects animation scale for `"water"` `shader_variation`. Affects warp effect intensity for `"lava"` `shader_variation`. Affects depth contrast for `"wetland-water"` `shader_variation`. Affects thin film effect intensity for `"oil"` `shader_variation`.

### dark_threshold
- **Type:** [[float (type)]] | ([[float (type)]], [[float (type)]])
Affects dark threshold for `"water"` `shader_variation`. Affects brightness of the shoreline lava for `"lava"` `shader_variation`. Affects water depth for `"wetland-water"` `shader_variation`. Affects thin film effect noise scale for `"oil"` `shader_variation`.

### reflection_threshold
- **Type:** [[float (type)]] | ([[float (type)]], [[float (type)]])
Affects reflection threshold for `"water"` `shader_variation`. Affects distortion scale for `"lava"` `shader_variation`. Affects distortion tiling for `"wetland-water"` `shader_variation`. Affects distortion map scale for `"oil"` `shader_variation`.

### specular_threshold
- **Type:** [[float (type)]] | ([[float (type)]], [[float (type)]])
Affects specular threshold for `"water"` and `"wetland-water"` `shader_variation`s. Affects shoreline lava for `"lava"` `shader_variation`. Affects nothing for `"oil"` `shader_variation`.

### near_zoom
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2.0`
If they are set to a tuple, the properties `animation_scale`, `dark_threshold`, `reflection_threshold` and `specular_threshold` are linearly interpolated between each of their two values based on the current zoom level expressed as a ratio between `near_zoom` and `far_zoom`. E.g. if current zoom level is equal to `near_zoom`, the first tuple value is picked.

### far_zoom
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
If they are set to a tuple, the properties `animation_scale`, `dark_threshold`, `reflection_threshold` and `specular_threshold` are linearly interpolated between each of their two values based on the current zoom level expressed as a ratio between `near_zoom` and `far_zoom`. E.g. if current zoom level is equal to `far_zoom`, the second tuple value is picked.

### lightmap_alpha
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
- **Requires:** `space_age`
Value 0 makes water appear as water in water mask, but does not occlude lights, and doesn't overwrite lightmap alpha drawn to pixel previously (by background layer of tile transition, or underwater sprite). Light emitted by water-like-tile (for example lava) will blend additively with previously rendered light. Value 1 makes water occlude lights, but won't be recognized as water in water mask used for masking decals by water.
