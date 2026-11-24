---
title: on_segmented_unit_died
tags: [factorio-api, runtime, event]
---
# on_segmented_unit_died

Called when a segmented unit dies.

## Filter

- **Type:** [[LuaSegmentedUnitDiedEventFilter]]

## Data

### segmented_unit
- **Type:** [[LuaSegmentedUnit]]
The unit that died.

### cause
- **Type:** [[LuaEntity]]
- **Optional**
The entity that did the killing if available.

### force
- **Type:** [[LuaForce]]
- **Optional**
The force that did the killing if any.

### damage_type
- **Type:** [[LuaDamagePrototype]]
- **Optional**
The damage type if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
