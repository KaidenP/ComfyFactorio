---
title: CutsceneWaypoint
tags: [factorio-api, runtime, concept]
---
# CutsceneWaypoint

## Fields

### position
- **Type:** [[MapPosition]]
- **Optional**
Position to pan the camera to.

### target
- **Type:** [[LuaEntity]] | [[LuaCommandable]]
- **Optional**
Entity or unit group to pan the camera to.

### transition_time
- **Type:** [[uint32]]
How many ticks it will take to reach this waypoint from the previous one.

### time_to_wait
- **Type:** [[uint32]]
Time in ticks to wait before moving to the next waypoint.

### zoom
- **Type:** [[double]]
- **Optional**
Zoom level to be set when the waypoint is reached. When not specified, the previous waypoint's zoom is used.
