---
title: on_cargo_pod_finished_descending
tags: [factorio-api, runtime, event]
---
# on_cargo_pod_finished_descending

Called when a cargo pods lands on a surface, either at a station or on the ground.

## Data

### cargo_pod
- **Type:** [[LuaEntity]]

### launched_by_rocket
- **Type:** [[boolean]]
True for pods spawned on a rocket.

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
