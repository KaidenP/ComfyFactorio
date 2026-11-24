---
title: on_tick
tags: [factorio-api, runtime, event]
---
# on_tick

It is fired once every tick. Since this event is fired every tick, its handler shouldn't include performance heavy code.

## Data

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
