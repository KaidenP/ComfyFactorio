---
title: PlayMusicSpecification
tags: [factorio-api, runtime, concept]
---
# PlayMusicSpecification

## Fields

### name
- **Type:** [[string]]
The name of ambient sound to play.

### skip_natural_pause
- **Type:** [[boolean]]
- **Optional**
Skip the natural pause between music tracks. If there is currently a track playing, this has no effect. Defaults to `false`.

### dont_transition_from
- **Type:** [[boolean]]
- **Optional**
Don't transition from this music track on surface change. Defaults to `false`.

### delay_duration
- **Type:** [[uint32]]
- **Optional**
Number of ticks for the music transition delay.

### fade_out_duration
- **Type:** [[uint32]]
- **Optional**
Number of ticks for the music transition fade out.

### pause_duration
- **Type:** [[uint32]]
- **Optional**
Number of ticks for the music transition pause.

### fade_in_duration
- **Type:** [[uint32]]
- **Optional**
Number of ticks for the music transition fade in.
