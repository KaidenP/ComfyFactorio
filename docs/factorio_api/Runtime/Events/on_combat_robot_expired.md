---
title: on_combat_robot_expired
tags: [factorio-api, runtime, event]
---
# on_combat_robot_expired

Called when a combat robot expires through a lack of energy, or timeout.

## Data

### robot
- **Type:** [[LuaEntity]]

### owner
- **Type:** [[LuaEntity]]
- **Optional**
The entity that owns the robot if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
