---
title: on_territory_created
tags: [factorio-api, runtime, event]
---
# on_territory_created

Called when a territory is created for any reason.

## Data

### cause
- **Type:** [[defines.territory_created_cause]]
The reason the territory was created.

### territory
- **Type:** [[LuaTerritory]]
The territory that was created.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
