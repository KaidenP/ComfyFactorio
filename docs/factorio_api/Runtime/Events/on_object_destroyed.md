---
title: on_object_destroyed
tags: [factorio-api, runtime, event]
---
# on_object_destroyed

Called after an object is destroyed which was registered with [[LuaBootstrap#register_on_object_destroyed|LuaBootstrap::register_on_object_destroyed]] previously.

Depending on when a given object is destroyed, this event will be fired at the end of the current tick or at the end of the next tick. The event's timing is independent of the in-world object being destroyed.

## Data

### registration_number
- **Type:** [[uint64]]
The number returned by [[LuaBootstrap#register_on_object_destroyed|register_on_object_destroyed]] to uniquely identify this object during this event.

### useful_id
- **Type:** [[uint64]]
The [[RegistrationTarget|useful identifier]] of the object or `0` if the object does not have a useful id. Same as second value returned by [[LuaBootstrap#register_on_object_destroyed|LuaBootstrap::register_on_object_destroyed]].

### type
- **Type:** [[defines.target_type]]
Type of the object that was destroyed. Same as third value returned by [[LuaBootstrap#register_on_object_destroyed|LuaBootstrap::register_on_object_destroyed]].

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
