---
title: on_robot_pre_mined
tags: [factorio-api, runtime, event]
---
# on_robot_pre_mined

Called before a robot mines an entity.

## Filter

- **Type:** [[LuaPreRobotMinedEntityEventFilter]]

## Data

### robot
- **Type:** [[LuaEntity]]
The robot that's about to do the mining.

### entity
- **Type:** [[LuaEntity]]
The entity which is about to be mined.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
