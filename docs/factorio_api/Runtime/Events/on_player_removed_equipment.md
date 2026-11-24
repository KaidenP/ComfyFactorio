---
title: on_player_removed_equipment
tags: [factorio-api, runtime, event]
---
# on_player_removed_equipment

Called after the player removes equipment from an equipment grid

## Data

### player_index
- **Type:** [[uint32]]

### grid
- **Type:** [[LuaEquipmentGrid]]
The equipment grid removed from.

### equipment
- **Type:** [[string]]
The equipment removed.

### quality
- **Type:** [[string]]
The equipment quality.

### count
- **Type:** [[uint32]]
The count of equipment removed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
