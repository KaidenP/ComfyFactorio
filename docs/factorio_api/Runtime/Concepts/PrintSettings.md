---
title: PrintSettings
tags: [factorio-api, runtime, concept]
---
# PrintSettings

## Fields

### color
- **Type:** [[Color]]
- **Optional**
Color of the message to print. Defaults to white.

### sound
- **Type:** [[defines.print_sound]]
- **Optional**
If a sound should be emitted for this message. Defaults to `defines.print_sound.use_player_settings`.

### skip
- **Type:** [[defines.print_skip]]
- **Optional**
Condition when to skip adding message. Defaults to `defines.print_skip.if_redundant`.

### sound_path
- **Type:** [[SoundPath]]
- **Optional**
The sound to play. If not given, [[UtilitySounds#console_message|UtilitySounds::console_message]] will be used instead.

### volume_modifier
- **Type:** [[float]]
- **Optional**
The volume of the sound to play. Must be between 0 and 1 inclusive. Defaults to 1.

### game_state
- **Type:** [[boolean]]
- **Optional**
If set to false, message will not be part of game state and will disappear from output console after save-load. Defaults to `true`.
