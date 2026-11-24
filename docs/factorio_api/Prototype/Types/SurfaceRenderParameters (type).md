---
title: SurfaceRenderParameters
tags: [factorio-api, prototype, type]
---
# SurfaceRenderParameters

*Note: `SurfaceRenderParameters (type)`.*

## Properties

### day_night_cycle_color_lookup
- **Type:** [[DaytimeColorLookupTable (type)]]
- **Optional**

### shadow_opacity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### draw_sprite_clouds
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to `true` and `clouds` property is not set, the legacy sprite clouds will be rendered on the surface.

### clouds
- **Type:** [[CloudsEffectProperties (type)]]
- **Optional**

### fog
- **Type:** [[FogEffectProperties (type)]]
- **Optional**
- **Requires:** `space_age`

### terrain_tint_effect
- **Type:** [[GlobalTintEffectProperties (type)]]
- **Optional**
- **Requires:** `space_age`

### space_dust_background
- **Type:** [[SpaceDustEffectProperties (type)]]
- **Optional**
- **Requires:** `space_age`

### space_dust_foreground
- **Type:** [[SpaceDustEffectProperties (type)]]
- **Optional**
- **Requires:** `space_age`

### platform_backdrop
- **Type:** [[PlatformBackdrop (type)]]
- **Optional**
