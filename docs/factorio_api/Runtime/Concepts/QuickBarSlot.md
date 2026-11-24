---
title: QuickBarSlot
tags: [factorio-api, runtime, concept]
---
# QuickBarSlot

## Fields

### type
- **Type:** `"record"` | `"remote"` | `"filter"` | `"item"`
Type of slot content

### record
- **Type:** [[LuaRecord]]
- **Optional**
Only present and mandatory when `type` is `record`.

### filter
- **Type:** [[ItemFilter]]
- **Optional**
Only present and mandatory when `type` is `remote` or `filter`. Name must be present (cannot be a quality only item filter).

### selection
- **Type:** array<[[LuaEntity]]>
- **Optional**
Only present and mandatory  when `type` is `remote`. Entities must be spider-vehicles.

### item
- **Type:** [[LuaItem]]
- **Optional**
Only present and mandatory when `type` is `item`.
