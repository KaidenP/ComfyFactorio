---
title: NeighbourConnectableConnection
tags: [factorio-api, runtime, concept]
---
# NeighbourConnectableConnection

## Fields

### position
- **Type:** [[MapPosition]]

### direction
- **Type:** [[defines.direction]]

### target
- **Type:** [[LuaEntity]]
- **Optional**
Entity to which this connection is connected to, if any.

### target_real
- **Type:** [[boolean]]
- **Optional**
Whether connected entity is real or ghost.

### first
- **Type:** [[boolean]]
- **Optional**
If multiple connections are connected to the same target, only one connection is marked as first and provides neighbour bonuses.
