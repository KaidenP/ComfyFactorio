---
title: on_post_segmented_unit_died
tags: [factorio-api, runtime, event]
---
# on_post_segmented_unit_died

Called after a segmented unit dies.

## Filter

- **Type:** [[LuaPostSegmentedUnitDiedEventFilter]]

## Data

### force
- **Type:** [[LuaForce]]
- **Optional**
The force that did the killing if any.

### segments
- **Type:** [[PostSegmentDiedData]]
Information about each of the unit's individual segments when it died.

### prototype
- **Type:** [[LuaEntityPrototype]]
The prototype of the unit that died.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of the unit that died.

### damage_type
- **Type:** [[LuaDamagePrototype]]
- **Optional**
The damage type that did the killing if any.

### surface_index
- **Type:** [[uint32]]
The surface the entity was on.

### unit_number
- **Type:** [[uint32]]
The unit number of the unit that died.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
