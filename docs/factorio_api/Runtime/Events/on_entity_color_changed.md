---
title: on_entity_color_changed
tags: [factorio-api, runtime, event]
---
# on_entity_color_changed

Called after an entity has been recolored either by the player or through script.

Automatic recoloring due to [[LuaPlayer#color|LuaPlayer::color]] will not raise events, as that is a separate mechanism.

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was recolored.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
