---
title: TrainStopGoal
tags: [factorio-api, runtime, concept]
---
# TrainStopGoal

## Fields

### train_stop
- **Type:** [[LuaEntity]]
Train stop target. Must be connected to rail ([[LuaEntity#connected_rail|LuaEntity::connected_rail]] returns valid LuaEntity).

### priority
- **Type:** [[uint8]]
- **Optional**
Goal priority. If not provided, defaults to [[LuaEntity#train_stop_priority|LuaEntity::train_stop_priority]] of provided train_stop.
