---
title: ElemID
tags: [factorio-api, runtime, concept]
---
# ElemID

## Fields

### type
- **Type:** [[ElemType]]

### name
- **Type:** [[string]]
Name of a prototype as defined by `type`.

### quality
- **Type:** [[string]]
- **Optional**
Name of a quality prototype if `type` uses quality.

### signal_type
- **Type:** [[SignalIDType]]
- **Optional**
Only loaded, and mandatory if `type` is `"signal"`.
