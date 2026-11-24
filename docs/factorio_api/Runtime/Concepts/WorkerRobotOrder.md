---
title: WorkerRobotOrder
tags: [factorio-api, runtime, concept]
---
# WorkerRobotOrder

## Fields

### type
- **Type:** [[defines.robot_order_type]]
The type of the order.

### target
- **Type:** [[LuaEntity]]
- **Optional**
The target of the order.

### item_to_place
- **Type:** [[ItemWithQualityCount]]
- **Optional**
The item to place if relevant.

### secondary_target
- **Type:** [[LuaEntity]]
- **Optional**
The secondary target of the upgrade order.

### cliff_explosive_id
- **Type:** [[LuaItemPrototype]]
- **Optional**
The cliff explosive for the cliff explode job.

### target_item
- **Type:** [[ItemIDAndQualityIDPair]]
- **Optional**
The target item of the pickup or deliver order.

### target_count
- **Type:** [[ItemCountType]]
- **Optional**
The target count of the pickup or deliver order.
