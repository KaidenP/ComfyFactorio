---
title: on_equipment_inserted
tags: [factorio-api, runtime, event]
---
# on_equipment_inserted

Called after equipment is inserted into an equipment grid.

## Data

### grid
- **Type:** [[LuaEquipmentGrid]]
The equipment grid inserted into.

### equipment
- **Type:** [[LuaEquipment]]
The equipment inserted.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
