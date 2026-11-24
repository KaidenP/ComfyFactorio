---
title: TerritorySettings
tags: [factorio-api, prototype, type]
---
# TerritorySettings

*Note: `TerritorySettings (type)`.*

## Properties

### units
- **Type:** array<[[EntityID (type)]]>
- **Optional**
Names of the [[SegmentedUnitPrototype]].

### territory_index_expression
- **Type:** [[string (type)]]
- **Optional**
Mandatory if `units` is not empty.

### territory_variation_expression
- **Type:** [[string (type)]]
- **Optional**
- **Default:** 0
The result will be converted to integer, clamped and used as an index for `units` array. Negative values will result in empty spawn location.

### minimum_territory_size
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Minimum number of chunks a territory must have. Below this, it will get deleted.
