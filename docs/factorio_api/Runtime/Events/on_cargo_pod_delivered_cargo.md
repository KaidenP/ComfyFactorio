---
title: on_cargo_pod_delivered_cargo
tags: [factorio-api, runtime, event]
---
# on_cargo_pod_delivered_cargo

Called after a cargo pod has delivered its cargo.

## Data

### cargo_pod
- **Type:** [[LuaEntity]]

### spawned_container
- **Type:** [[LuaEntity]]
- **Optional**
The spawned container if any. Created when destination type is [[defines.cargo_destination#surface|surface]].

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
