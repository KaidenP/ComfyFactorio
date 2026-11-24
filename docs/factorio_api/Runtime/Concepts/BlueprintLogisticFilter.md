---
title: BlueprintLogisticFilter
tags: [factorio-api, runtime, concept]
---
# BlueprintLogisticFilter

## Fields

### index
- **Type:** [[LogisticFilterIndex]]

### type
- **Type:** [[SignalIDType]]
- **Optional**
The type of the logistic filter.

### name
- **Type:** [[string]]
- **Optional**
Name of the logistic filter.

### quality
- **Type:** [[string]]
- **Optional**
The prototype name of the quality. `nil` for any quality.

### comparator
- **Type:** [[ComparatorString]]
- **Optional**
The comparator for quality. `nil` if any quality.

### count
- **Type:** [[int32]]

### max_count
- **Type:** [[ItemCountType]]
- **Optional**

### minimum_delivery_count
- **Type:** [[ItemCountType]]
- **Optional**
Defaults to `0`.

### import_from
- **Type:** [[string]]
- **Optional**

### request_from
- **Type:** [[RequestFromLocation]]
- **Optional**
From which sources items should be requested for space platforms. Defaults to `"planet"`.
