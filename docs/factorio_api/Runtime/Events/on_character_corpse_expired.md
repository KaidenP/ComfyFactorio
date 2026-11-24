---
title: on_character_corpse_expired
tags: [factorio-api, runtime, event]
---
# on_character_corpse_expired

Called when a character corpse expires due to timeout or all of the items being removed from it.

this is not called if the corpse is mined. See [[defines.events#on_pre_player_mined_item|defines.events.on_pre_player_mined_item]] to detect that.

## Data

### corpse
- **Type:** [[LuaEntity]]
The corpse.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
