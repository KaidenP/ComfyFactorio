---
title: on_segmented_unit_created
tags: [factorio-api, runtime, event]
---
# on_segmented_unit_created

Called when a segmented unit is created for any reason.

## Filter

- **Type:** [[LuaSegmentedUnitCreatedEventFilter]]

## Data

### cause
- **Type:** [[defines.segmented_unit_created_cause]]
The reason that the segmented unit was created.

### segmented_unit
- **Type:** [[LuaSegmentedUnit]]
The segmented unit that was created.

### clone_source
- **Type:** [[LuaSegmentedUnit]]
- **Optional**
If the new segmented unit was cloned, the segmented unit from which the new unit was cloned.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
