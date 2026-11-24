---
title: on_robot_mined_entity
tags: [factorio-api, runtime, event]
---
# on_robot_mined_entity

Called after the results of an entity being mined are collected just before the entity is destroyed.

After this event any items in the buffer will be transferred into the robot as if they came from mining the entity.

The buffer inventory is special in that it's only valid during this event and has a dynamic size expanding as more items are transferred into it.

## Filter

- **Type:** [[LuaRobotMinedEntityEventFilter]]

## Data

### robot
- **Type:** [[LuaEntity]]
The robot doing the mining.

### entity
- **Type:** [[LuaEntity]]
The entity that has been mined.

### buffer
- **Type:** [[LuaInventory]]
The temporary inventory that holds the result of mining the entity.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
