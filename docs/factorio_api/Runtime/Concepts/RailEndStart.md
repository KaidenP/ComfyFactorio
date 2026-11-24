---
title: RailEndStart
tags: [factorio-api, runtime, concept]
---
# RailEndStart

## Fields

### rail
- **Type:** [[LuaEntity]]

### direction
- **Type:** [[defines.rail_direction]]

### allow_path_within_segment
- **Type:** [[boolean]]
- **Optional**
Defaults to `true`. Providing false will cause the pathfinder to reject a path that starts here and ends in the same segment as the path would be too short to provide correct alignment with a goal.

### is_front
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.

### priority
- **Type:** [[uint8]]
- **Optional**
Start priority. Defaults to `50`.
