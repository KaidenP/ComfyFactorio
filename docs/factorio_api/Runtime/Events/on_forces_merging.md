---
title: on_forces_merging
tags: [factorio-api, runtime, event]
---
# on_forces_merging

Called when two forces are about to be merged using `game.merge_forces()`.

## Data

### source
- **Type:** [[LuaForce]]
The force to be destroyed

### destination
- **Type:** [[LuaForce]]
The force to reassign entities to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
