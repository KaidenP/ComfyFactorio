---
title: on_space_platform_mined_item
tags: [factorio-api, runtime, event]
---
# on_space_platform_mined_item

Called when a platform mines an entity.

## Data

### platform
- **Type:** [[LuaSpacePlatform]]
The platform that did the mining.

### item_stack
- **Type:** [[ItemWithQualityCount]]
The entity the platform just picked up.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
