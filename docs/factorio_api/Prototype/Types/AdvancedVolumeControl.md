---
title: AdvancedVolumeControl
tags: [factorio-api, prototype, type]
---
# AdvancedVolumeControl

## Properties

### attenuation
- **Type:** [[Fade]]
- **Optional**
Volume reduction (fade-out) controlled by distance (fraction of audible distance).

### fades
- **Type:** [[Fades]]
- **Optional**
Volume reduction (fade-out) or increase (fade-in) controlled by zoom level.

### darkness_threshold
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Has to be in the range [-1.0, 1.0].

Positive values are used for night sounds, the volume of the sound is 1.0 when darkness = threshold, 0.0 when darkness = 0.0 and linearly interpolated in between.

Negative values are used for day sounds, the sound of the sound is 0.0  when darkness = -threshold, 1.0 when darkness = 1.0 and linearly interpolated in between.
