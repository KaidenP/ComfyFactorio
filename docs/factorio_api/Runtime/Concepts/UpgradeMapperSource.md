---
title: UpgradeMapperSource
tags: [factorio-api, runtime, concept]
---
# UpgradeMapperSource

## Fields

### type
- **Type:** `"item"` | `"entity"`

### name
- **Type:** [[string]]
- **Optional**
Name of the item or entity.

### quality
- **Type:** [[string]]
- **Optional**
Name of the quality prototype.

### comparator
- **Type:** [[ComparatorString]]
- **Optional**
The quality comparison type.

### module_filter
- **Type:** [[EntityIDFilter]]
- **Optional**
When upgrading modules, this defines the specific entities to apply the upgrade to. `nil` applies it to all entities.
