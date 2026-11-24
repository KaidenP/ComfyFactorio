---
title: on_entity_cloned
tags: [factorio-api, runtime, event]
---
# on_entity_cloned

Called when an entity is cloned. The filter applies to the source entity.

## Filter

- **Type:** [[LuaEntityClonedEventFilter]]

## Data

### source
- **Type:** [[LuaEntity]]

### destination
- **Type:** [[LuaEntity]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
