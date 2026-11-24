---
title: on_pre_ghost_deconstructed
tags: [factorio-api, runtime, event]
---
# on_pre_ghost_deconstructed

Called before a ghost entity is destroyed as a result of being marked for deconstruction.

Also called for item request proxies before they are destroyed as a result of being marked for deconstruction.

## Filter

- **Type:** [[LuaPreGhostDeconstructedEventFilter]]

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that did the deconstruction if any.

### ghost
- **Type:** [[LuaEntity]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
