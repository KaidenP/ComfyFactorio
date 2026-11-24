---
title: VariableAmbientSoundLayerStateProperties
tags: [factorio-api, prototype, type]
---
# VariableAmbientSoundLayerStateProperties

## Properties

### enabled
- **Type:** [[boolean (type)]]
- **Optional**

### variant
- **Type:** [[uint8 (type)]]
- **Optional**
Index of a layer's variant.

Cannot be zero.

### sequence_length
- **Type:** [[RandomRange]]
- **Optional**
Number of samples in a sequence.

The minimum cannot be zero.

Mandatory for layers with `"semi-randomized"` [[VariableAmbientSoundCompositionMode]].

Applicable for layers with `"randomized"` [[VariableAmbientSoundCompositionMode]].

Cannot be defined for layers with `"shuffled"` [[VariableAmbientSoundCompositionMode]].

### number_of_repetitions
- **Type:** [[RandomRange]] | [[ProbabilityTable]]
- **Optional**
The number of times a layer repeats itself until it's considered finished. If it's not defined, the layer never finishes on its own. What counts as repetition depends on the [[VariableAmbientSoundCompositionMode]].

Each sample played is counted as a repetition of `"randomized"` layer.

Repetition of `"semi-randomized"` layer is counted when its sequence is finished.

Repetition of `"shuffled"` layer is counted when all samples play once.

Each sample played is counted as a repetition of `"layer-controlled"` layer.

If `number_of_repetitions` of [[VariableAmbientSoundLayer#control_layer|VariableAmbientSoundLayer::control_layer]] of `"layer-controlled"` layer is smaller than `number_of_repetitions` of the controlled layer, `number_of_repetitions` of the control layer is used for the purposes of `pause_between_repetitions` and `end_pause`.

Cannot be zero.

### start_pause
- **Type:** [[RandomRange]]
- **Optional**
Pause before a layer starts playing.

### pause_between_samples
- **Type:** [[RandomRange]]
- **Optional**
Pause between individual samples within a sequence.

Cannot be defined for `"randomized"` layers without defining `sequence_length` as well. Alternatively, use `pause_between_repetitions` instead.

Cannot be defined for layers with `sublayer_offset` defined.

### pause_between_repetitions
- **Type:** [[RandomRange]]
- **Optional**
Pause between each repetition of a layer. The repetition is not counted until the pause finishes.

### end_pause
- **Type:** [[RandomRange]]
- **Optional**
Pause before a layer finishes playing. The last repetition and consequently the layer being finished is not counted until the pause finishes.

### silence_instead_of_sample_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`
A sample replaced by silence still counts as played for the purposes of sequence count, repetition count, pauses, etc.

Must be in the `[0.0, 1.0]` interval.
