---
title: on_research_cancelled
tags: [factorio-api, runtime, event]
---
# on_research_cancelled

Called when research is cancelled.

## Data

### research
- **Type:** dictionary<[[string]] → [[uint32]]>
A mapping of technology name to how many times it was cancelled.

### force
- **Type:** [[LuaForce]]
The force whose research was cancelled.

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who cancelled the research if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
