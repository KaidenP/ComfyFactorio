---
title: InfinityContainerPrototype
tags: [factorio-api, prototype]
---
# InfinityContainerPrototype

> **Parent:** [[LogisticContainerPrototype]] · **Type name:** `infinity-container`

A generic container, such as a chest, that can spawn or void items and interact with the logistics network.

## Properties

### erase_contents_when_mined
- **Type:** [[boolean (type)]]

### preserve_contents_when_created
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When true, items created inside the infinity chest will not start to spoil until they have been removed from the chest.

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**
- **Default:** `"all"`
Controls which players can control what the chest spawns.

### logistic_mode
- **Type:** [[LogisticMode (type)]]
- **Optional**
- **Overrides parent**
The way this chest interacts with the logistic network.

### render_not_in_network_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Whether the "no network" icon should be rendered on this entity if the entity is not within a logistics network.

![[too-far-from-roboport-icon.png]]

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Overrides parent**
The number of slots in this container. May not be zero.
