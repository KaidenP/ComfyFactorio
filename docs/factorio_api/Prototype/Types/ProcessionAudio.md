---
title: ProcessionAudio
tags: [factorio-api, prototype, type]
---
# ProcessionAudio

## Properties

### type
- **Type:** [[ProcessionAudioType]]

### sound
- **Type:** [[Sound]]
- **Optional**
Mandatory if `type` is `"sound"`.

### looped_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Mandatory if `type` is `"looped-sound"`.

### catalogue_id
- **Type:** [[uint32 (type)]]
- **Optional**
Mandatory if `type` is `"pod_catalogue"` or `type` is `"location_catalogue"`.
