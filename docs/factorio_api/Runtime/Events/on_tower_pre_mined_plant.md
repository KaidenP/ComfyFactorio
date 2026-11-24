---
title: on_tower_pre_mined_plant
tags: [factorio-api, runtime, event]
---
# on_tower_pre_mined_plant

Called before an agricultural tower mines a plant.

## Data

### tower
- **Type:** [[LuaEntity]]
The tower that is about to do the mining.

### plant
- **Type:** [[LuaEntity]]
The plant that is about to be mined.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
