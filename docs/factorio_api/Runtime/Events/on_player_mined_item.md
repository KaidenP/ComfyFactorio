---
title: on_player_mined_item
tags: [factorio-api, runtime, event]
---
# on_player_mined_item

Called when the player mines something.

## Data

### item_stack
- **Type:** [[ItemWithQualityCount]]
The item given to the player

### player_index
- **Type:** [[uint32]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
