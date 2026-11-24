---
title: PlatformBackdrop
tags: [factorio-api, prototype, type]
---
# PlatformBackdrop

*Note: `PlatformBackdrop (type)`.*

## Properties

### position
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{-450.0, -50.0}`

### radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `400.0`

### planet_surface
- **Type:** [[EffectTexture]]
- **Optional**
Wrapped around the surface of the sphere using equirectangular projection.

### planet_normal
- **Type:** [[EffectTexture]]
- **Optional**
Normal map of the surface deforming local sphere normal.

### planet_reflectivity
- **Type:** [[EffectTexture]]
- **Optional**
Glossiness of the surface in red channel.

### planet_emission
- **Type:** [[EffectTexture]]
- **Optional**
Emissive light added to the surface. Can be disabled on lit side using the `emission_scales_with_shadow` property.

### global_cloud
- **Type:** [[EffectTexture]]
- **Optional**
Cloud mapped over the planet as the surface texture.

### global_cloud_normal
- **Type:** [[EffectTexture]]
- **Optional**

### global_cloud_flow
- **Type:** [[EffectTexture]]
- **Optional**
Flow map distorting the global cloud.

### hero_clouds
- **Type:** array<[[PlatformBackdropHeroCloud (type)]]>
- **Optional**
Individual Hero Cloud decals over the planet surface. The maximum number is four.

### hero_cloud_texture_1
- **Type:** [[Animation]]
- **Optional**
Sprite or Animation to be referenced by `hero_clouds` definitions with `sprite_index` 1.

### hero_cloud_texture_2
- **Type:** [[Animation]]
- **Optional**
Sprite or Animation to be referenced by `hero_clouds` definitions with `sprite_index` 2.

### hero_cloud_texture_3
- **Type:** [[Animation]]
- **Optional**
Sprite or Animation to be referenced by `hero_clouds` definitions with `sprite_index` 3.

### rotation_seconds
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `340.0`
How many seconds it takes for the planet to do one revolution.

### planet_axis
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{-30.0, 20.0}`
Tilt and pitch of the planet axis.

### planet_axis_deviation_amplitude
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0.0, 0.0}`
How much tilt and pitch vary over time.

### planet_axis_deviation_seconds
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{609.2, 712.7}`
Number of seconds it takes for tilt and pitch to complete one cycle of deviation.

### parallax_strength
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{1.0, 1.0}`
How strongly the planet moves with camera. `{1.0, 1.0}` means it tracks the starfield. `{0.0, 0.0}` means it tracks the foreground tiles.

### flight_approach_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Scales the speed at which the planet appears in view when flown towards.

### emission_scales_with_shadow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When true only the dark side will receive emission.

### hero_clouds_are_emissive
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When true the hero clouds will add their color to emission as well.

### atmosphere_thickness
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.02`
Width of the atmosphere layer as portion of the total radius.

### atmosphere_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0.095, 0.15, 0.19, 1.0}`
Color of atmospheric light. Multiplied by 10 in shader.

### specular_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{1.0, 1.0, 1.0, 1.0}`
Color of specular light.

### light_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0.9804, 1.0, 1.0, 1.0}`
Color of light.

### light_direction
- **Type:** [[Vector3D (type)]]
- **Optional**
- **Default:** `{-1.0, 0.0, 0.5}`

### atmosphere_ray_light_color_1
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0.5, 0.26665, 0.0, 1.0}`
Color of dawn side of terminator light. Multiplied by 10 in shader.

### atmosphere_ray_light_color_2
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0.1, 0.08431, 0.05059, 1.0}`
Color of dusk side of terminator light. Multiplied by 10 in shader.

### surface_normal_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### cloud_normal_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### specular_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### cloudiness
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Amount of cloud texture to be used based off of the alpha channel of the cloud texture.

### emission_scalar
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2.0`

### light_radius
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `9.9`
Perceived size of the light. Also affects size of the specular spot.

### light_intensity_contrast
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.7`
Harshness of the terminator. Functions like atmosphere thickness.

### surface_vertical_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`
How far below the atmosphere layer should the surface be.

### cloud_vertical_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.015`
How far below the atmosphere layer should the clouds be.

### cloud_flow_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.3`
Intensity of the flow map effect. Begins to degenerate at high values.

### cloud_flow_seconds
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `32.0`
How many seconds it takes the flow effect to loop.

### cloud_panning_rate
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`
Rotational speed of the clouds laterally across the planet relative to `rotation_seconds` of the planet. `-1.0` means it counteracts the rotation rate and makes clouds remain in place. `0.0` means it drifts along with planet surface.
