---
title: ScheduleRecord
tags: [factorio-api, runtime, concept]
---
# ScheduleRecord

## Fields

### station
- **Type:** [[string]]
- **Optional**
Name of the station.

### rail
- **Type:** [[LuaEntity]]
- **Optional**

### rail_direction
- **Type:** [[defines.rail_direction]]
- **Optional**
When a train is allowed to reach rail target from any direction it will be `nil`. If rail has to be reached from specific direction, this value allows to choose the direction. This value corresponds to [[LuaEntity#connected_rail_direction|LuaEntity::connected_rail_direction]] of a TrainStop.

### wait_conditions
- **Type:** array<[[WaitCondition]]>
- **Optional**
When reading this will always be present but may be an empty array.

### temporary
- **Type:** [[boolean]]
- **Optional**
When reading this will always be present. Defaults to `false` when writing.

### created_by_interrupt
- **Type:** [[boolean]]
- **Optional**
When reading this will always be present. Defaults to `false` when writing.

### allows_unloading
- **Type:** [[boolean]]
- **Optional**
When reading this will always be present. Defaults to `true` when writing.
