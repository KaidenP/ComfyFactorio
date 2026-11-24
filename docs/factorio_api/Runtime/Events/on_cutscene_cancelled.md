---
title: on_cutscene_cancelled
tags: [factorio-api, runtime, event]
---
# on_cutscene_cancelled

Called when a cutscene is cancelled by the player or by script.

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
