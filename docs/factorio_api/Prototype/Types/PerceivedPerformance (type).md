---
title: PerceivedPerformance
tags: [factorio-api, prototype, type]
---
# PerceivedPerformance

*Note: `PerceivedPerformance (type)`.*

Not all prototypes that use this type are affected by all properties.

## Properties

### minimum
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Affects animation speed.

Must be less than or equal to `maximum`.

### maximum
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Max double
Affects animation speed.

### performance_to_activity_rate
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Affects [[MainSound]] if [[MainSound#match_progress_to_activity|MainSound::match_progress_to_activity]], [[MainSound#match_volume_to_activity|MainSound::match_volume_to_activity]] or [[MainSound#match_speed_to_activity|MainSound::match_speed_to_activity]] is `true`.
