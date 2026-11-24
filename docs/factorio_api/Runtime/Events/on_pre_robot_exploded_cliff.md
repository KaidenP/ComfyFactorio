---
title: on_pre_robot_exploded_cliff
tags: [factorio-api, runtime, event]
---
# on_pre_robot_exploded_cliff

Called directly before a robot explodes cliffs.

## Data

### robot
- **Type:** [[LuaEntity]]

### cliff
- **Type:** [[LuaEntity]]

### item
- **Type:** [[LuaItemPrototype]]
The cliff explosive used.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of the cliff explosive used.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
