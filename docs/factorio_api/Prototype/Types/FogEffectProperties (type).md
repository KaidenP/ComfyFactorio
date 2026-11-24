---
title: FogEffectProperties
tags: [factorio-api, prototype, type]
---
# FogEffectProperties

*Note: `FogEffectProperties (type)`.*

## Properties

### fog_type
- **Type:** `"vulcanus"` | `"gleba"`
- **Optional**
- **Default:** `"vulcanus"`
`gleba` type is rendered per chunk and opacity of fog depends on count of tiles with [[TilePrototype#lowland_fog|lowland_fog]] set to `true` on the chunk.

### shape_noise_texture
- **Type:** [[EffectTexture]]

### detail_noise_texture
- **Type:** [[EffectTexture]]

### color1
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** {1, 1, 1, 1}

### color2
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** {1, 1, 1, 1}

### tick_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `5e-06`
