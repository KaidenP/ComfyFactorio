---
title: TrivialSmokePrototype
tags: [factorio-api, prototype]
---
# TrivialSmokePrototype

> **Parent:** [[Prototype]] · **Type name:** `trivial-smoke` · **Instance limit:** 255

Smoke, but it's not an entity for optimization purposes.

## Properties

### animation
- **Type:** [[Animation]]

### duration
- **Type:** [[uint32 (type)]]
Can't be 0 - the smoke will never render.

### glow_animation
- **Type:** [[Animation]]
- **Optional**

### color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=0.375, g=0.375, b=0.375, a=0.375}`

### start_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### end_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### movement_slow_down_factor
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.995`
Value between 0 and 1, with 1 being no slowdown and 0 being no movement.

### spread_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### fade_away_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
`fade_in_duration` + `fade_away_duration` must be <= `duration`.

### fade_in_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
`fade_in_duration` + `fade_away_duration` must be <= `duration`.

### glow_fade_away_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `fade_away_duration`

### cyclic
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### affected_by_wind
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Smoke always moves randomly unless `movement_slow_down_factor` is 0. If `affected_by_wind` is true, the smoke will also be moved by wind.

### show_when_smoke_off
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"smoke"`
