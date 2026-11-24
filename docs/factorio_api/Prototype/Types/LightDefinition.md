---
title: LightDefinition
tags: [factorio-api, prototype, type]
---
# LightDefinition

Specifies a light source. This is loaded either as a single light source or as an array of light sources.

## Type

struct | array<struct>

## Properties

### type
- **Type:** `"basic"` | `"oriented"`
- **Optional**
- **Default:** `"basic"`

### picture
- **Type:** [[Sprite]]
- **Optional**
Only loaded, and mandatory if `type` is `"oriented"`.

### rotation_shift
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `type` is `"oriented"`.

### intensity
- **Type:** [[float (type)]]
Brightness of the light in the range `[0, 1]`, where `0` is no light and `1` is the maximum light.

### size
- **Type:** [[float (type)]]
The radius of the light in tiles. Note that the light gets darker near the edges, so the effective size of the light will appear to be smaller.

### source_orientation_offset
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** `0`

### add_perspective
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### flicker_interval
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### flicker_min_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### flicker_max_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `flicker_min_modifier`

### offset_flicker
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Offsets tick used to calculate flicker by position hash. Useful to desynchronize flickering of multiple stationary lights.

### shift
- **Type:** [[Vector (type)]]
- **Optional**

### color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1}`
Color of the light.

### minimum_darkness
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

## Examples

```
-- The light of the orange state of the rail signal
orange_light = {intensity = 0.2, size = 4, color={r=1, g=0.5}}
```

```
-- The front lights of the car
light =
{
  {
    type = "oriented",
    minimum_darkness = 0.3,
    picture =
    {
      filename = "__core__/graphics/light-cone.png",
      priority = "extra-high",
      flags = { "light" },
      scale = 2,
      width = 200,
      height = 200
    },
    shift = {-0.6, -14},
    size = 2,
    intensity = 0.6,
    color = {r = 0.92, g = 0.77, b = 0.3}
  },
  {
    type = "oriented",
    minimum_darkness = 0.3,
    picture =
    {
      filename = "__core__/graphics/light-cone.png",
      priority = "extra-high",
      flags = { "light" },
      scale = 2,
      width = 200,
      height = 200
    },
    shift = {0.6, -14},
    size = 2,
    intensity = 0.6,
    color = {r = 0.92, g = 0.77, b = 0.3}
  }
}
```
