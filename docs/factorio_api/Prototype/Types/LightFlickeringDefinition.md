---
title: LightFlickeringDefinition
tags: [factorio-api, prototype, type]
---
# LightFlickeringDefinition

Specifies the light flicker. Note that this defaults to "showing a white light" instead of the usually expected "showing nothing".

## Properties

### minimum_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.2`
Brightness of the light in the range `[0, 1]` where `0` is no light and `1` is the maximum light.

### maximum_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.8`
Brightness of the light in the range `[0, 1]` where `0` is no light and `1` is the maximum light.

### derivation_change_frequency
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.3`

### derivation_change_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.06`

### border_fix_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.02`

### minimum_light_size
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
The radius of the light in tiles. Note, that the light gets darker near the edges, so the effective size of the light seems to be smaller.

### light_intensity_to_size_coefficient
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** {r=1, g=1, b=1} (White)
Color of the light.
