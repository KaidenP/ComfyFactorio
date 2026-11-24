---
title: AddRecordData
tags: [factorio-api, runtime, concept]
---
# AddRecordData

## Fields

### station
- **Type:** [[string]]
- **Optional**
One of station or rail must be given.

### rail
- **Type:** [[LuaEntity]]
- **Optional**

### rail_direction
- **Type:** [[defines.rail_direction]]
- **Optional**
When `rail` is given, this can be provided to further narrow down direction from which that rail should be approached.

### temporary
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### created_by_interrupt
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### allows_unloading
- **Type:** [[boolean]]
- **Optional**
Defaults to `true`.

### wait_conditions
- **Type:** array<[[WaitCondition]]>
- **Optional**

### index
- **Type:** [[ScheduleRecordPosition]]
- **Optional**
If record position is not given, the record is appended.
