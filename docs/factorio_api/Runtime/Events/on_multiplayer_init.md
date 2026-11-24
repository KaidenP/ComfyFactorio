---
title: on_multiplayer_init
tags: [factorio-api, runtime, event]
---
# on_multiplayer_init

Called when [[LuaGameScript#is_multiplayer|LuaGameScript::is_multiplayer]] changes to true. May also be raised when it was already true but a game was loaded from a save file and with hosting.

## Data

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
