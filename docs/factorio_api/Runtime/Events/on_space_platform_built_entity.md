---
title: on_space_platform_built_entity
tags: [factorio-api, runtime, event]
---
# on_space_platform_built_entity

Called when a space platform builds an entity.

## Filter

- **Type:** [[LuaPlatformBuiltEntityEventFilter]]

## Data

### platform
- **Type:** [[LuaSpacePlatform]]
The platform that did the building.

### entity
- **Type:** [[LuaEntity]]
The entity built.

### stack
- **Type:** [[LuaItemStack]]
The item used to do the building.

### tags
- **Type:** [[Tags]]
- **Optional**
The tags associated with this entity if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
