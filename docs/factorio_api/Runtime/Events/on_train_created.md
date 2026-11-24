---
title: on_train_created
tags: [factorio-api, runtime, event]
---
# on_train_created

Called when a new train is created either through disconnecting/connecting an existing one or building a new one.

## Data

### train
- **Type:** [[LuaTrain]]

### old_train_id_1
- **Type:** [[uint32]]
- **Optional**
The first old train id when splitting/merging trains.

### old_train_id_2
- **Type:** [[uint32]]
- **Optional**
The second old train id when splitting/merging trains.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
