---
title: on_cargo_pod_started_ascending
tags: [factorio-api, runtime, event]
---
# on_cargo_pod_started_ascending

Called when a cargo pod departs from a space platform hub or by another method not attached to a rocket.

## Data

### cargo_pod
- **Type:** [[LuaEntity]]

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that is riding the cargo pod, if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
