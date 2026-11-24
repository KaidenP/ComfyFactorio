---
title: script_raised_teleported
tags: [factorio-api, runtime, event]
---
# script_raised_teleported

A static event mods can use to tell other mods they teleported something by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]] or [[LuaBootstrap#raise_script_teleported|LuaBootstrap::raise_script_teleported]], or when `raise_teleported` is passed to [[LuaControl#teleport|LuaControl::teleport]].

## Filter

- **Type:** [[LuaScriptRaisedTeleportedEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was teleported.

### old_surface_index
- **Type:** [[uint8]]
The entity's surface before the teleportation.

### old_position
- **Type:** [[MapPosition]]
The entity's position before the teleportation.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
