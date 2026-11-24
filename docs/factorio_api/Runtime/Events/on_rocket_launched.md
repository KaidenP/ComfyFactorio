---
title: on_rocket_launched
tags: [factorio-api, runtime, event]
---
# on_rocket_launched

Called when a rocket finishes ascending. (Triggers listening for finished rocket launch past 2.0 have been moved to 'on_cargo_pod_finished_ascending' as rocket and cargo pod are two separate entities)

## Data

### rocket
- **Type:** [[LuaEntity]]

### rocket_silo
- **Type:** [[LuaEntity]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
