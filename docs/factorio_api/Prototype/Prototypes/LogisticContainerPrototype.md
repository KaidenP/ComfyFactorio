---
title: LogisticContainerPrototype
tags: [factorio-api, prototype]
---
# LogisticContainerPrototype

> **Parent:** [[ContainerPrototype]] · **Type name:** `logistic-container`

A generic container, such as a chest, that interacts with the logistics network.

## Properties

### logistic_mode
- **Type:** [[LogisticMode (type)]]
The way this chest interacts with the logistic network.

### max_logistic_slots
- **Type:** [[uint16 (type)]]
- **Optional**
The number of request slots this logistics container has. Requester-type containers must have > 0 slots and can have a maximum of [[UtilityConstants (prototype)#max_logistic_filter_count|UtilityConstants::max_logistic_filter_count]] slots. Storage-type containers must have <= 1 slot.

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

### render_not_in_network_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the "no network" icon should be rendered on this entity if the entity is not within a logistics network.

![[too-far-from-roboport-icon.png]]

### robot_door
- **Type:** [[RobotDoorSpecification]]
- **Optional**

### use_exact_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether logistic robots have to deliver the exact amount of items requested to this logistic container instead of over-delivering (within their cargo size).
