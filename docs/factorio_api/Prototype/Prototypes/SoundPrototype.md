---
title: SoundPrototype
tags: [factorio-api, prototype]
---
# SoundPrototype

> **Type name:** `sound`

Specifies a sound that can be used with [[SoundPath]] at runtime.

## Properties

### type
- **Type:** `"sound"`

### name
- **Type:** [[string (type)]]
Name of the sound. Can be used as a [[SoundPath]] at runtime.

### category
- **Type:** [[SoundType (type)]]
- **Optional**
- **Default:** `"game-effect"`

### priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `127`
Sounds with higher priority will replace a sound with lower priority if the maximum sounds limit is reached.

0 is the highest priority, 255 is the lowest priority.

### aggregation
- **Type:** [[AggregationSpecification]]
- **Optional**

### allow_random_repeat
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### audible_distance_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.0`
Modifies how far a sound can be heard. Must be between `0` and `1` inclusive.

### game_controller_vibration_data
- **Type:** [[GameControllerVibrationData]]
- **Optional**

### advanced_volume_control
- **Type:** [[AdvancedVolumeControl]]
- **Optional**

### speed_smoothing_window_size
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### variations
- **Type:** [[SoundDefinition]] | array<[[SoundDefinition]]>
- **Optional**

### filename
- **Type:** [[FileName]]
- **Optional**
Supported sound file formats are `.ogg` (Vorbis and Opus) and `.wav`.

Only loaded, and mandatory if `variations` is not defined.

### volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `variations` is not defined.

This sets both min and max volumes.

Must be `>= 0`.

### min_volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `variations` and `volume` are not defined.

Must be `>= 0`.

### max_volume
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Only loaded if `variations` is not defined.

Only loaded if `min_volume` is defined.

Must be `>= min_volume`.

### preload
- **Type:** [[boolean (type)]]
- **Optional**
Only loaded if `variations` is not defined.

### speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Speed must be `>= 1 / 64`. This sets both min and max speeds.

Only loaded if `variations` is not defined.

### min_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Must be `>= 1 / 64`.

Only loaded if both `variations` and `speed` are not defined.

### max_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
Must be `>= min_speed`.

Only loaded if `variations` is not defined. Only loaded, and mandatory if `min_speed` is defined.

### modifiers
- **Type:** [[SoundModifier]] | array<[[SoundModifier]]>
- **Optional**
Only loaded if `variations` is not defined.
