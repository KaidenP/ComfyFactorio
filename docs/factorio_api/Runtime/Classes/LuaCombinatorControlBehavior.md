---
title: LuaCombinatorControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaCombinatorControlBehavior

> **Abstract class** — not directly instantiable.

> **Extends:** [[LuaControlBehavior]]

## Attributes

### signals_last_tick
- **Type:** array<[[Signal]]>
The circuit network signals sent by this combinator last tick.

## Methods

### get_signal_last_tick
Gets the value of a specific signal sent by this combinator behavior last tick or `nil` if the signal didn't exist.

**Parameters:**
- **`signal`** — [[SignalID]]: The signal to get

**Returns:**
- [[int32]] *(optional)*
