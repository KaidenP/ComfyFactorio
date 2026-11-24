---
title: CustomEventPrototype
tags: [factorio-api, prototype]
---
# CustomEventPrototype

> **Parent:** [[Prototype]] · **Type name:** `custom-event`

Defines a custom event with an unique name. During runtime, mods can use the event name to [[LuaBootstrap#raise_event|raise]] and [[LuaBootstrap#on_event|subscribe to]] the custom event.

Custom events share the same namespace as custom inputs and built-in events for subscribing to and raising them.

## Example

```
{
  type = "custom-event",
  name = "potato-custom-event"
}
```
