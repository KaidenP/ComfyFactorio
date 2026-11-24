---
title: LogisticFilter
tags: [factorio-api, runtime, concept]
---
# LogisticFilter

## Fields

### value
- **Type:** [[SignalFilter]]
- **Optional**
The item filter to put into the slot.

### min
- **Type:** [[int32]]
- **Optional**
The minimum amount to satisfy. If `min` is non-zero, and `value` is present, then the quality condition inside `value` does not allow quality ranges.

### max
- **Type:** [[ItemCountType]]
- **Optional**
The maximum amount to keep in inventory. `nil` for infinite.

### minimum_delivery_count
- **Type:** [[ItemCountType]]
- **Optional**
The minimum count that will be delivered to a space platform. `nil` if unchanged from the default.

### import_from
- **Type:** [[SpaceLocationID]]
- **Optional**
The space location to import from.

### request_from
- **Type:** [[RequestFromLocation]]
- **Optional**
From which sources items should be requested for space platforms. Defaults to `"planet"`.
