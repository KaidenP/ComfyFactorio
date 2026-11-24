---
title: on_research_moved
tags: [factorio-api, runtime, event]
---
# on_research_moved

Called when research is moved forwards or backwards in the research queue.

## Data

### force
- **Type:** [[LuaForce]]
The force whose research was re-arranged.

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who did the re-arranging if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
