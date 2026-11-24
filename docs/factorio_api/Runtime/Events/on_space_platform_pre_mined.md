---
title: on_space_platform_pre_mined
tags: [factorio-api, runtime, event]
---
# on_space_platform_pre_mined

Called before a platform mines an entity.

## Filter

- **Type:** [[LuaPrePlatformMinedEntityEventFilter]]

## Data

### platform
- **Type:** [[LuaSpacePlatform]]
The platform that's about to do the mining.

### entity
- **Type:** [[LuaEntity]]
The entity which is about to be mined.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
