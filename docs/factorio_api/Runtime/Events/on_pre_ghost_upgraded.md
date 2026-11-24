---
title: on_pre_ghost_upgraded
tags: [factorio-api, runtime, event]
---
# on_pre_ghost_upgraded

Called before a ghost entity is upgraded.

## Filter

- **Type:** [[LuaPreGhostUpgradedEventFilter]]

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that did the upgrade if any.

### ghost
- **Type:** [[LuaEntity]]

### target
- **Type:** [[LuaEntityPrototype]]

### quality
- **Type:** [[LuaQualityPrototype]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
