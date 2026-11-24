---
title: on_trigger_created_entity
tags: [factorio-api, runtime, event]
---
# on_trigger_created_entity

Called when an entity with a trigger prototype (such as capsules) create an entity AND that trigger prototype defined `trigger_created_entity=true`.

## Data

### entity
- **Type:** [[LuaEntity]]

### source
- **Type:** [[LuaEntity]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
