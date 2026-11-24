---
title: on_robot_mined
tags: [factorio-api, runtime, event]
---
# on_robot_mined

Called when a robot mines an entity.

## Data

### robot
- **Type:** [[LuaEntity]]
The robot that did the mining.

### item_stack
- **Type:** [[ItemWithQualityCount]]
The entity the robot just picked up.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
