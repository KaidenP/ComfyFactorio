---
title: on_territory_destroyed
tags: [factorio-api, runtime, event]
---
# on_territory_destroyed

Called when a territory is destroyed from a surface.

## Data

### territory
- **Type:** [[LuaTerritory]]
The territory that will be destroyed. This object will be valid so that you can still read and modify its properties before it is finally destroyed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
