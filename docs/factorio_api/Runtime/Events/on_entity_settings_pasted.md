---
title: on_entity_settings_pasted
tags: [factorio-api, runtime, event]
---
# on_entity_settings_pasted

Called after entity copy-paste is done.

## Data

### player_index
- **Type:** [[uint32]]

### source
- **Type:** [[LuaEntity]]
The source entity settings were copied from.

### destination
- **Type:** [[LuaEntity]]
The destination entity settings were copied to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
