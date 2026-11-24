---
title: SmokePrototype
tags: [factorio-api, prototype]
---
# SmokePrototype

> **Parent:** [[EntityPrototype]] · **Abstract**

Abstract entity that has an animation.

## Properties

### animation
- **Type:** [[Animation]]
- **Optional**

### cyclic
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false then the smoke expires when the animation has played once.

### duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
May not be 0 if `cyclic` is true. If `cyclic` is false then the smoke will be expire when the animation has played once, even if there would still be duration left.

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

### start_scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`

### end_scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`

### color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=0.375, g=0.375, b=0.375, a=0.375}`

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

### movement_slow_down_factor
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.995`
Value between 0 and 1, with 0 being no movement.

### glow_fade_away_duration
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** The value of `fade_away_duration`

### glow_animation
- **Type:** [[Animation]]
- **Optional**

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
- **Overrides parent**
Must have a collision box size of zero.
**Examples:**

```
collision_box = {{0, 0}, {0, 0}}
```

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
