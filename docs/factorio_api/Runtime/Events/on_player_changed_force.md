---
title: on_player_changed_force
tags: [factorio-api, runtime, event]
---
# on_player_changed_force

Called after a player changes forces.

## Data

### player_index
- **Type:** [[uint32]]
The player who changed forces.

### force
- **Type:** [[LuaForce]]
The old force.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
