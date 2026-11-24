---
title: on_research_queued
tags: [factorio-api, runtime, event]
---
# on_research_queued

Called when research is queued.

## Data

### research
- **Type:** [[LuaTechnology]]
The technology queued

### force
- **Type:** [[LuaForce]]
The force whose research was queued.

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who queued the research if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
