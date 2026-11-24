---
title: on_equipment_removed
tags: [factorio-api, runtime, event]
---
# on_equipment_removed

Called after equipment is removed from an equipment grid.

## Data

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
