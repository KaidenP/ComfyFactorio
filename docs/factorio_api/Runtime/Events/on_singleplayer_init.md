---
title: on_singleplayer_init
tags: [factorio-api, runtime, event]
---
# on_singleplayer_init

Called when [[LuaGameScript#is_multiplayer|LuaGameScript::is_multiplayer]] changes to false. May also be raised when it was already false but a game was loaded from a save file without hosting.

## Data

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
