---
title: on_next_day_started
tags: [factorio-api, runtime, event]
---
# on_next_day_started

Called when value of [[LuaSurface#daytime|LuaSurface::daytime]] wraps around to be in `[0, 1)` range.

## Data

### surface
- **Type:** [[LuaSurface]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
