---
title: VariableAmbientSoundVariableSound
tags: [factorio-api, prototype, type]
---
# VariableAmbientSoundVariableSound

## Properties

### layers
- **Type:** array<[[VariableAmbientSoundLayer]]>
Cannot be empty.

### intermezzo
- **Type:** [[Sound]]
- **Optional**

### states
- **Type:** array<[[VariableAmbientSoundState]]>
The first state is used as the starting state and cannot be an intermezzo state.

Cannot be empty.

### length_seconds
- **Type:** [[uint32 (type)]]
Cannot be zero.

### alignment_samples
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `12600`
Number of audio signal samples (sampling frequency is 44.1kHz) defining a time grid. Music samples are aligned with this grid when queued.
