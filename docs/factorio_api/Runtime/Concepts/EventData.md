---
title: EventData
tags: [factorio-api, runtime, concept]
---
# EventData

Information about the event that has been raised. The table can also contain other fields depending on the type of event. See [[Events|the list of Factorio events]] for more information on these.

## Fields

### name
- **Type:** [[defines.events]]
The identifier of the event this handler was registered to.

### tick
- **Type:** [[MapTick]]
The tick during which the event happened.

### mod_name
- **Type:** [[string]]
- **Optional**
The name of the mod that raised the event if it was raised using [[LuaBootstrap#raise_event|LuaBootstrap::raise_event]].
