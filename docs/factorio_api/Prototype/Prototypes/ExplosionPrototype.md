---
title: ExplosionPrototype
tags: [factorio-api, prototype]
---
# ExplosionPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `explosion`

Used to play an animation and a sound.

## Properties

### animations
- **Type:** [[AnimationVariations]]

### sound
- **Type:** [[Sound]]
- **Optional**

### smoke
- **Type:** [[TrivialSmokeID (type)]]
- **Optional**
Mandatory if `smoke_count` > 0.

### height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### smoke_slow_down_factor
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### smoke_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### rotate
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### beam
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### correct_rotation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### scale_animation_speed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### fade_in_duration
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### fade_out_duration
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"explosion"`

### scale_in_duration
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### scale_out_duration
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### scale_end
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### scale_increment_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### light_intensity_factor_initial
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`
Silently clamped to be between 0 and 1.

### light_intensity_factor_final
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`
Silently clamped to be between 0 and 1.

### light_size_factor_initial
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.05`
Silently clamped to be between 0 and 1.

### light_size_factor_final
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`
Silently clamped to be between 0 and 1.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### light_intensity_peak_start_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### light_intensity_peak_end_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.9`

### light_size_peak_start_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.1`

### light_size_peak_end_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### scale_initial
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### scale_initial_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### scale_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### delay
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
Number of ticks to delay the explosion effects by.

### delay_deviation
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
The maximum number of ticks to randomly delay the explosion effects by. In addition to the number of ticks defined by `delay`, the explosion will be delayed by a random number of ticks between 0 and `delay_deviation` (inclusive).

### explosion_effect
- **Type:** [[Trigger]]
- **Optional**
The effect/trigger that happens when the explosion effect triggers after the initial delay as defined by `delay` and `delay_deviation`.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
