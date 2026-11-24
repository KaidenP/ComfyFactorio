---
title: on_chart_tag_removed
tags: [factorio-api, runtime, event]
---
# on_chart_tag_removed

Called just before a chart tag is deleted.

## Data

### tag
- **Type:** [[LuaCustomChartTag]]

### force
- **Type:** [[LuaForce]]

### player_index
- **Type:** [[uint32]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
