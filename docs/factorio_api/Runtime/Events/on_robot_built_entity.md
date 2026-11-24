---
title: on_robot_built_entity
tags: [factorio-api, runtime, event]
---
# on_robot_built_entity

Called when a construction robot builds an entity.

## Filter

- **Type:** [[LuaRobotBuiltEntityEventFilter]]

## Data

### robot
- **Type:** [[LuaEntity]]
The robot that did the building.

### entity
- **Type:** [[LuaEntity]]
The entity built.

### stack
- **Type:** [[LuaItemStack]]
The item used to do the building.

### tags
- **Type:** [[Tags]]
- **Optional**
The tags associated with this entity if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
