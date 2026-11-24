---
title: on_player_placed_equipment
tags: [factorio-api, runtime, event]
---
# on_player_placed_equipment

Called after the player puts equipment in an equipment grid

## Data

### player_index
- **Type:** [[uint32]]

### equipment
- **Type:** [[LuaEquipment]]
The equipment put in the equipment grid.

### grid
- **Type:** [[LuaEquipmentGrid]]
The equipment grid the equipment was put in.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
