---
title: AggregationSpecification
tags: [factorio-api, prototype, type]
---
# AggregationSpecification

## Properties

### max_count
- **Type:** [[uint32 (type)]]

### progress_threshold
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
If `count_already_playing` is `true`, this will determine maximum progress when instance is counted toward playing sounds.

### volume_reduction_rate
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2.0`
Has to be greater than or equal to 0.0.

### remove
- **Type:** [[boolean (type)]]
If `false`, the volume of sound instances above `max_count` is calculated according to the formula `volume = (x + 1) ^ (-volume_reduction_rate)`, where `x` is the order number of an instance above the threshold.

If `true`, sound instances above `max_count` are removed.

### count_already_playing
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, already playing sounds are taken into account when checking `max_count`.

### priority
- **Type:** `"closest"` | `"farthest"` | `"newest"` | `"oldest"`
- **Optional**
- **Default:** `"closest"`
