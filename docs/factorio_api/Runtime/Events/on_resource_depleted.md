---
title: on_resource_depleted
tags: [factorio-api, runtime, event]
---
# on_resource_depleted

Called when a resource entity reaches 0 or its minimum yield for infinite resources.

## Data

### entity
- **Type:** [[LuaEntity]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
