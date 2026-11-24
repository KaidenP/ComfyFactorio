---
title: script_raised_built
tags: [factorio-api, runtime, event]
---
# script_raised_built

A static event mods can use to tell other mods they built something by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]] or [[LuaBootstrap#raise_script_built|LuaBootstrap::raise_script_built]], or when `raise_built` is passed to [[LuaSurface#create_entity|LuaSurface::create_entity]].

## Filter

- **Type:** [[LuaScriptRaisedBuiltEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that has been built.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
