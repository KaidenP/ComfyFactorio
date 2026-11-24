---
title: script_raised_set_tiles
tags: [factorio-api, runtime, event]
---
# script_raised_set_tiles

A static event mods can use to tell other mods they changed tiles on a surface by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]] or [[LuaBootstrap#raise_script_set_tiles|LuaBootstrap::raise_script_set_tiles]], or when `raise_event` is passed to [[LuaSurface#set_tiles|LuaSurface::set_tiles]].

## Data

### surface_index
- **Type:** [[uint32]]
The surface whose tiles were changed.

### tiles
- **Type:** array<[[Tile]]>
The tiles that were changed.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
