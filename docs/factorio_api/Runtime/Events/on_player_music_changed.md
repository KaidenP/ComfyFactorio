---
title: on_player_music_changed
tags: [factorio-api, runtime, event]
---
# on_player_music_changed

Called when a player's current music track (ambient sound) changes. This includes when the music track finishes playing.

## Data

### player_index
- **Type:** [[uint32]]
The player whose current music has changed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
