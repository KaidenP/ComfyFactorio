---
title: on_trigger_fired_artillery
tags: [factorio-api, runtime, event]
---
# on_trigger_fired_artillery

Called when an entity with a trigger prototype (such as capsules) fire an artillery projectile AND that trigger prototype defined `trigger_fired_artillery=true`.

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
