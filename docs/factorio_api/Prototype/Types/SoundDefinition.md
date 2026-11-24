---
title: SoundDefinition
tags: [factorio-api, prototype, type]
---
# SoundDefinition

## Type

struct | [[FileName]]

## Properties

### filename
- **Type:** [[FileName]]
Supported sound file formats are `.ogg` (Vorbis and Opus) and `.wav`.

### volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
This sets both min and max volumes.

Must be `>= 0`.

### min_volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `volume` is not defined.

Must be `>= 0`.

### max_volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `min_volume` is defined.

Must be `>= min_volume`.

### preload
- **Type:** [[boolean (type)]]
- **Optional**

### speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Speed must be `>= 1 / 64`. This sets both min and max speeds.

### min_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `speed` is not defined.

Must be `>= 1 / 64`.

### max_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded, and mandatory, if `min_speed` is defined.

Must be `>= min_speed`.

### modifiers
- **Type:** [[SoundModifier]] | array<[[SoundModifier]]>
- **Optional**
