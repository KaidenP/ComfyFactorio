---
title: UpgradeMapperDestination
tags: [factorio-api, runtime, concept]
---
# UpgradeMapperDestination

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

### module_limit
- **Type:** [[uint16]]
- **Optional**
When upgrading modules, this defines the maximum number of this module to be installed in the destination entity. `0` or `nil` means no limit.

### module_slots
- **Type:** array<[[BlueprintItemIDAndQualityIDPair]]>
- **Optional**
When upgrading entities, this defines explicit modules to be installed in the destination entity. Lists empty slots as `{}`.
