---
title: SoundAccent
tags: [factorio-api, prototype, type]
---
# SoundAccent

## Properties

### sound
- **Type:** [[Sound]]
- **Optional**

### frame
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### play_for_working_visualisation
- **Type:** [[string (type)]]
- **Optional**
Play the `sound` for a working visualisation of a given [[WorkingVisualisation#name|WorkingVisualisation::name]].

The name cannot be empty.

### play_for_directions
- **Type:** array<[[defines.direction]]>
- **Optional**
The `sound` is played when the entity has one the specified direction.
