---
title: on_entity_logistic_slot_changed
tags: [factorio-api, runtime, event]
---
# on_entity_logistic_slot_changed

Called when one of an entity's logistic slots changes.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who changed the slot, or `nil` if changed by script.

### entity
- **Type:** [[LuaEntity]]
The entity for whom a logistic slot was changed.

### section
- **Type:** [[LuaLogisticSection]]
The section changed.

### slot_index
- **Type:** [[uint32]]
The slot index that was changed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
