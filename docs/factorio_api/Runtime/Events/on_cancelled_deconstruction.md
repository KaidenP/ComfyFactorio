---
title: on_cancelled_deconstruction
tags: [factorio-api, runtime, event]
---
# on_cancelled_deconstruction

Called when the deconstruction of an entity is canceled.

## Filter

- **Type:** [[LuaEntityDeconstructionCancelledEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]

### player_index
- **Type:** [[uint32]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
