---
title: on_marked_for_upgrade
tags: [factorio-api, runtime, event]
---
# on_marked_for_upgrade

Called when an entity is marked for upgrade with the upgrade planner or via script.

## Filter

- **Type:** [[LuaEntityMarkedForUpgradeEventFilter]]

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**

### entity
- **Type:** [[LuaEntity]]

### target
- **Type:** [[LuaEntityPrototype]]

### quality
- **Type:** [[LuaQualityPrototype]]
The target quality.

### previous_target
- **Type:** [[LuaEntityPrototype]]
- **Optional**
Previous upgrade target of the entity, if entity was already marked for upgrade.

### previous_quality
- **Type:** [[LuaQualityPrototype]]
- **Optional**
Previous upgrade target quality, if entity was already marked for upgrade.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
