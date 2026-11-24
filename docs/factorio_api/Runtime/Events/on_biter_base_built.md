---
title: on_biter_base_built
tags: [factorio-api, runtime, event]
---
# on_biter_base_built

Called when a biter migration builds a base.

This will be called multiple times for each migration, once for every biter that is sacrificed to build part of the new base.

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was built.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
