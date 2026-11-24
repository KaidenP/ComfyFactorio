---
title: ProcessionAudioEvent
tags: [factorio-api, prototype, type]
---
# ProcessionAudioEvent

Controls sounds during procession.

## Properties

### type
- **Type:** [[ProcessionAudioEventType]]

### usage
- **Type:** [[ProcessionAudioUsage]]
- **Optional**
Has to be defined unless the type is "stop-looped-sound".

### audio
- **Type:** [[ProcessionAudio]]
- **Optional**
Has to be defined unless the type is "stop-looped-sound".

### loop_id
- **Type:** [[uint32 (type)]]
- **Optional**
Has to be defined unless the type is "play-sound".
