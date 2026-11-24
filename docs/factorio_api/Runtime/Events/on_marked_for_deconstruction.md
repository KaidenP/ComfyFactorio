---
title: on_marked_for_deconstruction
tags: [factorio-api, runtime, event]
---
# on_marked_for_deconstruction

Called when an entity is marked for deconstruction with the Deconstruction planner or via script.

## Filter

- **Type:** [[LuaEntityMarkedForDeconstructionEventFilter]]

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
