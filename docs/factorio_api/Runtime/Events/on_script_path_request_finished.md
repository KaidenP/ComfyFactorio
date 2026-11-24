---
title: on_script_path_request_finished
tags: [factorio-api, runtime, event]
---
# on_script_path_request_finished

Called when a [[LuaSurface#request_path|LuaSurface::request_path]] call completes.

## Data

### path
- **Type:** array<[[PathfinderWaypoint]]>
- **Optional**
The actual path that the pathfinder has determined. `nil` if pathfinding failed.

### id
- **Type:** [[uint32]]
Handle to associate the callback with a particular call to [[LuaSurface#request_path|LuaSurface::request_path]].

### try_again_later
- **Type:** [[boolean]]
Indicates that the pathfinder failed because it is too busy, and that you can retry later.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
