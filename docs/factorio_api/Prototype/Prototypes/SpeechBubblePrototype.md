---
title: SpeechBubblePrototype
tags: [factorio-api, prototype]
---
# SpeechBubblePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `speech-bubble`

A speech bubble. It floats in the world and can display text.

## Properties

### style
- **Type:** [[string (type)]]
Needs a style of the type "speech_bubble_style", defined inside the gui styles.

### wrapper_flow_style
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"flow_style"`
Needs a style of the type "flow_style", defined inside the gui styles.

### y_offset
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### fade_in_out_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `60`

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
