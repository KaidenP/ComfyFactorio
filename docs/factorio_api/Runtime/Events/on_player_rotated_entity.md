---
title: on_player_rotated_entity
tags: [factorio-api, runtime, event]
---
# on_player_rotated_entity

Called when the player rotates an entity. This event is only fired when the entity actually changes its orientation -- pressing the rotate key on an entity that can't be rotated won't fire this event.

Entities being flipped will not fire this event, even if the flip involves rotating. See [[on_player_flipped_entity]].

## Data

### entity
- **Type:** [[LuaEntity]]
The rotated entity.

### previous_direction
- **Type:** [[defines.direction]]
The previous direction

### previous_mirroring
- **Type:** [[boolean]]

### player_index
- **Type:** [[uint32]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
