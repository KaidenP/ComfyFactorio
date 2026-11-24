---
title: on_blueprint_settings_pasted
tags: [factorio-api, runtime, event]
---
# on_blueprint_settings_pasted

Called when a blueprint entity is pasted over an existing entity or entity ghost.

The entity's settings, rotation, mirroring, wire connections, etc. may have been updated. This event is raised even if no settings actually changed.

Note this event is not raised when an entity is upgraded or marked for upgrade, when a new entity is created, or when an entity ghost is instantly revived. [[on_built_entity]] is raised instead in those cases.

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was updated. Can be either an entity or an entity ghost.

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who pasted the blueprint, if any. `nil` if pasted by script.

### tags
- **Type:** [[Tags]]
- **Optional**
Tags from the source blueprint, if any. Only provided for non-ghost entities. For ghost entities, access tags via `entity.tags`.

### previous_direction
- **Type:** [[defines.direction]]
- **Optional**
If the blueprint rotated the entity, provides the entity's direction before the rotation. Note: not provided for rotations due to superforce printing.

### mirrored
- **Type:** [[boolean]]
Whether the blueprint changed the entity's mirroring.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
