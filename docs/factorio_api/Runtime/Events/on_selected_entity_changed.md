---
title: on_selected_entity_changed
tags: [factorio-api, runtime, event]
---
# on_selected_entity_changed

Called after the selected entity changes for a given player.

## Data

### player_index
- **Type:** [[uint32]]
The player whose selected entity changed.

### last_entity
- **Type:** [[LuaEntity]]
- **Optional**
The last selected entity if it still exists and there was one.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
