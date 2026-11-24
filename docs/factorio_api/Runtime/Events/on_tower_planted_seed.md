---
title: on_tower_planted_seed
tags: [factorio-api, runtime, event]
---
# on_tower_planted_seed

Called before an agricultural tower plants a seed.

## Data

### tower
- **Type:** [[LuaEntity]]
The tower that did the planting.

### plant
- **Type:** [[LuaEntity]]
The plant that was planted.

### seed
- **Type:** [[ItemIDAndQualityIDPair]]
The seed that was used.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
