---
title: on_cancelled_upgrade
tags: [factorio-api, runtime, event]
---
# on_cancelled_upgrade

Called when the upgrade of an entity is canceled.

## Filter

- **Type:** [[LuaUpgradeCancelledEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]

### player_index
- **Type:** [[uint32]]
- **Optional**

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
