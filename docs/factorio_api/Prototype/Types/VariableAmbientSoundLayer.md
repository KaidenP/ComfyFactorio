---
title: VariableAmbientSoundLayer
tags: [factorio-api, prototype, type]
---
# VariableAmbientSoundLayer

## Properties

### name
- **Type:** [[string (type)]]
Name has to be unique across all layers.

### variants
- **Type:** array<[[Sound]]>
Cannot be empty.

Samples within a layer are the [[Sound#variations|Sound::variations]].

Number of samples must be the same across all variants.

Samples cannot have variable volume and all samples must have the same default volume.

Samples are required to have sampling frequency of 44.1kHz. This is checked at runtime.

### composition_mode
- **Type:** [[VariableAmbientSoundCompositionMode]]

### control_layer
- **Type:** [[string (type)]]
- **Optional**
Name of a layer which controls this layer, a layer cannot control itself.

Only loaded, and mandatory if `composition_mode` is `"layer-controlled"`.

### control_layer_sample_mapping
- **Type:** array<array<[[uint8 (type)]]>>
- **Optional**
Defines a mapping between controlling layer's samples and this (controlled) layer's samples. The number of items in the mapping must be the same as the number of samples in the controlling layer. Item in the mapping with index N defines which samples of this layer can play when the sample N is playing in the controlling layer.

Only loaded, and mandatory if `composition_mode` is `"layer-controlled"`.

### has_start_sample
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the first of [[Sound#variations|Sound::variations]] is played at the start of a sequence. The start sample counts towards the [[VariableAmbientSoundLayerStateProperties#sequence_length|VariableAmbientSoundLayerStateProperties::sequence_length]]

### has_end_sample
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the last of [[Sound#variations|Sound::variations]] is played at the end of a sequence (if the sequence is long enough). The end sample counts towards the [[VariableAmbientSoundLayerStateProperties#sequence_length|VariableAmbientSoundLayerStateProperties::sequence_length]].

### number_of_sublayers
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
If greater than one, samples are composed in overlapping sub-layers, offset from each other.

If greater than one, one of `sublayer_starting_offset` or `sublayer_offset` must be defined. Both cannot be defined together.

Cannot be defined for layers with `"shuffled"` `composition_mode`.

Cannot be zero.

### sublayer_starting_offset
- **Type:** [[RandomRange]] | [[ProbabilityTable]]
- **Optional**
Specifies starting offset of the second sub-layer.

Only loaded if `number_of_sublayers` is greater than one.

Cannot be defined together with `sublayer_offset`.

The minimum of [[RandomRange]] variant cannot be zero.

### sublayer_offset
- **Type:** [[RandomRange]] | [[ProbabilityTable]]
- **Optional**
Specifies offset between two sub-layers' samples.

This implicitly dictates the sample lengths as two sub-layer offsets.

Only loaded if `number_of_sublayers` is greater than one.

Cannot be defined together with `sublayer_starting_offset`.

The minimum of [[RandomRange]] variant cannot be zero.

### sample_length
- **Type:** [[RandomRange]]
- **Optional**
Explicitly defines sample lengths. The whole sample is played when this is not specified.

Cannot be defined together with `sublayer_offset`.

The minimum cannot be zero.
