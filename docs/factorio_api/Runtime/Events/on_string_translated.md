---
title: on_string_translated
tags: [factorio-api, runtime, event]
---
# on_string_translated

Called when a translation request generated through [[LuaPlayer#request_translation|LuaPlayer::request_translation]] or [[LuaPlayer#request_translations|LuaPlayer::request_translations]] has been completed.

## Data

### player_index
- **Type:** [[uint32]]
The player whose locale was used for the translation.

### localised_string
- **Type:** [[LocalisedString]]
The localised string being translated.

### result
- **Type:** [[string]]
The translated `localised_string`.

### id
- **Type:** [[uint32]]
The unique id for this translation request.

### translated
- **Type:** [[boolean]]
Whether the requested localised string was valid and could be translated.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
