---
title: InfinityInventoryFilter
tags: [factorio-api, runtime, concept]
---
# InfinityInventoryFilter

A single filter used by an infinity-filters instance.

## Fields

### name
- **Type:** [[ItemID]]
Name of the item. When reading a filter, this is a string.

### quality
- **Type:** [[QualityID]]
- **Optional**
Quality of the item. Defaults to `"normal"`. When reading a filter, this is a string.

### count
- **Type:** [[ItemCountType]]
- **Optional**
The count of the filter. Defaults to 0.

### mode
- **Type:** `"at-least"` | `"at-most"` | `"exactly"`
- **Optional**
Defaults to `"at-least"`.

### index
- **Type:** [[uint32]]
- **Optional**
The index of this filter in the filters list. Not required when writing a filter.
