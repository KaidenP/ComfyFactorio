---
title: on_forces_merged
tags: [factorio-api, runtime, event]
---
# on_forces_merged

Called after two forces have been merged using `game.merge_forces()`.

The source force is invalidated before this event is called and the name can be re-used in this event if desired.

## Data

### source_name
- **Type:** [[string]]
The force destroyed.

### source_index
- **Type:** [[uint32]]
The index of the destroyed force.

### destination
- **Type:** [[LuaForce]]
The force entities where reassigned to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
