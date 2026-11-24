---
title: on_force_friends_changed
tags: [factorio-api, runtime, event]
---
# on_force_friends_changed

Called when the a forces friends change.

## Data

### force
- **Type:** [[LuaForce]]
The force who's friends changed.

### other_force
- **Type:** [[LuaForce]]
Which force was added or removed.

### added
- **Type:** [[boolean]]
If the other force was added or removed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
