---
title: LuaNotificationQueue
tags: [factorio-api, runtime, class]
---
# LuaNotificationQueue

Object that keeps track of objects invalidation and queues notifications for when object becomes invalid.

This object is an alternative mechanism to [[LuaBootstrap#register_on_object_destroyed|LuaBootstrap::register_on_object_destroyed]] where instead of raising lua events, this object only queues notifications and makes them available to use later by calls to [[LuaNotificationQueue#poll|LuaNotificationQueue::poll]] or [[LuaNotificationQueue#poll_all|LuaNotificationQueue::poll_all]].

New instances of this object can be obtained from [[LuaBootstrap#new_notification_queue|LuaBootstrap::new_notification_queue]].

Each instance of this object is unique, always valid and cannot be copied. This object lives entirely in script state and if its no longer referenced by script, it will be destroyed by garbage collector.

## Attributes

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### add
Registers an object so that after it's destroyed, a notification is queued.

If this object is already registered within this notification queue, an existing registration number will be provided without creating new registration.

**Parameters:**
- **`object`** — [[RegistrationTarget]]: The object to register.

**Returns:**
- [[uint64]]: The registration number.

### find
Checks if provided object is already registered and returns existing registration number for it. If object is not registered, it is not registered and nil is returned instead.

**Parameters:**
- **`object`** — [[RegistrationTarget]]: The object to check.

**Returns:**
- [[uint64]] *(optional)*: The registration number if object is registered.

### remove
Removes a registration based on registration number.

**Parameters:**
- **`registration_id`** — [[uint64]]: Registration to be removed.

### clear
Removes all registrations.

### poll
Gets at most 1 registration id for which an object was destroyed.

**Returns:**
- [[uint64]] *(optional)*

### poll_all
Gets all registration ids for which object were destroyed.

**Returns:**
- array<[[uint64]]>
