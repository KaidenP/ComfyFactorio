---
title: on_train_schedule_changed
tags: [factorio-api, runtime, event]
---
# on_train_schedule_changed

Called when a trains schedule is changed either by the player or through script.

## Data

### train
- **Type:** [[LuaTrain]]

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who made the change if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
