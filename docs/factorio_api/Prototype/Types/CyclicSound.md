---
title: CyclicSound
tags: [factorio-api, prototype, type]
---
# CyclicSound

Used by [[BaseAttackParameters]] to play a sound during the attack.

## Properties

### begin_sound
- **Type:** [[Sound]]
- **Optional**
Played once at the beginning of the overall cyclic sound.

### middle_sound
- **Type:** [[Sound]]
- **Optional**
Played repeatedly after the begin_sound was played.

### end_sound
- **Type:** [[Sound]]
- **Optional**
Played once when the overall cyclic sound is requested to end.
