---
title: script_raised_revive
tags: [factorio-api, runtime, event]
---
# script_raised_revive

A static event mods can use to tell other mods they revived something by script. This event is only raised if a mod does so with [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]] or [[LuaBootstrap#raise_script_revive|LuaBootstrap::raise_script_revive]], or when `raise_revive` is passed to [[LuaEntity#revive|LuaEntity::revive]].

## Filter

- **Type:** [[LuaScriptRaisedReviveEventFilter]]

## Data

### entity
- **Type:** [[LuaEntity]]
The entity that was revived.

### tags
- **Type:** [[Tags]]
- **Optional**
The tags associated with this entity, if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
