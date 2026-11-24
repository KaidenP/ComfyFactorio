---
title: script_raised_destroy
tags: [factorio-api, runtime, event]
---
# script_raised_destroy

A static event mods can use to tell other mods they destroyed something by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]] or [[LuaBootstrap#raise_script_destroy|LuaBootstrap::raise_script_destroy]], or when `raise_destroy` is passed to [[LuaEntity#destroy|LuaEntity::destroy]].

## Filter

- **Type:** [[LuaScriptRaisedDestroyEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was destroyed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
