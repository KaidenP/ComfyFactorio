---
title: ModChangeData
tags: [factorio-api, runtime, concept]
---
# ModChangeData

## Fields

### old_version
- **Type:** [[string]]
- **Optional**
Old version of the mod. `nil` if the mod wasn't previously present (i.e. it was just added).

### new_version
- **Type:** [[string]]
- **Optional**
New version of the mod. `nil` if the mod is no longer present (i.e. it was just removed).
