---
title: on_build_base_arrived
tags: [factorio-api, runtime, event]
---
# on_build_base_arrived

Called when a [[defines.command#build_base|defines.command.build_base]] command reaches its destination, and before building starts.

## Data

### unit
- **Type:** [[LuaEntity]]
- **Optional**
The unit the command was assigned to.

### group
- **Type:** [[LuaCommandable]]
- **Optional**
The unit group the command was assigned to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
