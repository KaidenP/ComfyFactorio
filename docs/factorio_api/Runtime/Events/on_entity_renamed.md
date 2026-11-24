---
title: on_entity_renamed
tags: [factorio-api, runtime, event]
---
# on_entity_renamed

Called after an entity has been renamed either by the player or through script.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
If by_script is true this will not be included.

### by_script
- **Type:** [[boolean]]

### entity
- **Type:** [[LuaEntity]]

### old_name
- **Type:** [[string]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
