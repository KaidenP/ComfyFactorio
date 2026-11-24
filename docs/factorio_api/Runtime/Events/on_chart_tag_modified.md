---
title: on_chart_tag_modified
tags: [factorio-api, runtime, event]
---
# on_chart_tag_modified

Called when a chart tag is modified by a player or by script.

## Data

### tag
- **Type:** [[LuaCustomChartTag]]

### player_index
- **Type:** [[uint32]]
- **Optional**

### force
- **Type:** [[LuaForce]]

### old_text
- **Type:** [[string]]

### old_icon
- **Type:** [[SignalID]]

### old_position
- **Type:** [[MapPosition]]

### old_surface
- **Type:** [[LuaSurface]]

### old_player_index
- **Type:** [[uint32]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
