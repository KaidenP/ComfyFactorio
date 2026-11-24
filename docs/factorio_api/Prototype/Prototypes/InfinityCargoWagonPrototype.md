---
title: InfinityCargoWagonPrototype
tags: [factorio-api, prototype]
---
# InfinityCargoWagonPrototype

> **Parent:** [[CargoWagonPrototype]] · **Type name:** `infinity-cargo-wagon`

A cargo wagon that can spawn or void items at will.

## Properties

### erase_contents_when_mined
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### preserve_contents_when_created
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When true, items created inside the infinity cargo wagon will not start to spoil until they have been removed from the wagon.

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**
- **Default:** `"all"`
Controls which players can control what the chest spawns.
