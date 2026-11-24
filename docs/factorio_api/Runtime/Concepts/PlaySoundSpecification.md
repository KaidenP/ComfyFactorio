---
title: PlaySoundSpecification
tags: [factorio-api, runtime, concept]
---
# PlaySoundSpecification

## Fields

### path
- **Type:** [[SoundPath]]
The sound to play.

### position
- **Type:** [[MapPosition]]
- **Optional**
Where the sound should be played. If not given, it's played globally on the player's controller's surface.

### volume_modifier
- **Type:** [[double]]
- **Optional**
The volume of the sound to play. Must be between 0 and 1 inclusive.

### override_sound_type
- **Type:** [[SoundType]]
- **Optional**
The volume mixer to play the sound through. Defaults to the default mixer for the given sound type.
