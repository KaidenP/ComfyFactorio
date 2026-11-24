---
title: script_raised_destroy_segmented_unit
tags: [factorio-api, runtime, event]
---
# script_raised_destroy_segmented_unit

A static event that mods can use to tell other mods they destroyed a segmented unit by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]], or [[LuaBootstrap#raise_script_destroy_segmented_unit|LuaBootstrap::raise_script_destroy_segmented_unit]], or when `raise_destroy` is passed to [[LuaSegmentedUnit#destroy|LuaSegmentedUnit::destroy]].

## Filter

- **Type:** [[LuaScriptRaisedDestroySegmentedUnitEventFilter]]

## Data

### segmented_unit
- **Type:** [[LuaSegmentedUnit]]
The segmented unit that was destroyed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
