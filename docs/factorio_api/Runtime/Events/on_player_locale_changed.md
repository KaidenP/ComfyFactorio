---
title: on_player_locale_changed
tags: [factorio-api, runtime, event]
---
# on_player_locale_changed

Called when a player's active locale changes. See [[LuaPlayer#locale|LuaPlayer::locale]].

## Data

### player_index
- **Type:** [[uint32]]
The player whose locale was changed.

### old_locale
- **Type:** [[string]]
The previously active locale.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
