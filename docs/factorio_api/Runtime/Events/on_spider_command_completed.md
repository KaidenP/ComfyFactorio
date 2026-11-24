---
title: on_spider_command_completed
tags: [factorio-api, runtime, event]
---
# on_spider_command_completed

Called when a spider finishes moving to its autopilot position.

## Data

### vehicle
- **Type:** [[LuaEntity]]
Spider vehicle which was requested to move.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
