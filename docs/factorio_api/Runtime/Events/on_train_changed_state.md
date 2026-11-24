---
title: on_train_changed_state
tags: [factorio-api, runtime, event]
---
# on_train_changed_state

Called when a train changes state (started to stopped and vice versa)

## Data

### train
- **Type:** [[LuaTrain]]

### old_state
- **Type:** [[defines.train_state]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
