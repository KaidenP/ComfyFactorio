---
title: on_cutscene_finished
tags: [factorio-api, runtime, event]
---
# on_cutscene_finished

Called when a cutscene finishes naturally (was not cancelled).

## Data

### player_index
- **Type:** [[uint32]]
The player the cutscene was shown to.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
