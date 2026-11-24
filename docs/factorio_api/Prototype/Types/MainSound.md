---
title: MainSound
tags: [factorio-api, prototype, type]
---
# MainSound

## Properties

### sound
- **Type:** [[Sound]]
- **Optional**
Cannot be empty.

### probability
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Modifies how often the sound is played.

Silently clamped to the [0.0, 1.0] range.

Unused when [[WorkingSound#persistent|WorkingSound::persistent]] is `true`.
**Examples:**

```
probability = 1 / (3 * 60) -- average pause between the sound is 3 seconds
```

### fade_in_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `8`
Can't be used when `match_progress_to_activity` is `true`.

### fade_out_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `20`
Can't be used when `match_progress_to_activity` is `true`.

### activity_to_volume_modifiers
- **Type:** [[ActivityMatchingModifiers]]
- **Optional**

### activity_to_speed_modifiers
- **Type:** [[ActivityMatchingModifiers]]
- **Optional**

### match_progress_to_activity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Unused when [[WorkingSound#persistent|WorkingSound::persistent]] is `true`.

### match_volume_to_activity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### match_speed_to_activity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### play_for_working_visualisations
- **Type:** array<[[string (type)]]>
- **Optional**
Array of [[WorkingVisualisation#name|WorkingVisualisation::name]]s, individual names cannot be empty.

The `sound` is played when at least one of the specified working visualisations is drawn.

Unused when [[WorkingSound#persistent|WorkingSound::persistent]] is `true`.

### play_for_directions
- **Type:** array<[[defines.direction]]>
- **Optional**
The `sound` is played when the entity has one the specified direction.

Unused when [[WorkingSound#persistent|WorkingSound::persistent]] is `true`.

### volume_smoothing_window_size
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Only used if [[WorkingSound#persistent|WorkingSound::persistent]] is `true`.
