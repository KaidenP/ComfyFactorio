---
title: TriggerEffectItem
tags: [factorio-api, prototype, type]
---
# TriggerEffectItem

*Note: `TriggerEffectItem (type)`.*

> **Abstract**

The abstract base of all [[TriggerEffect|TriggerEffects]].

## Properties

### repeat_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `1`

### repeat_count_deviation
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be greater than `0` and less than or equal to `1`.

### affects_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### show_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### damage_type_filters
- **Type:** [[DamageTypeFilters (type)]]
- **Optional**
Guaranteed to work with [[EntityWithHealthPrototype#damaged_trigger_effect|EntityWithHealthPrototype::damaged_trigger_effect]] and [[EntityWithHealthPrototype#dying_trigger_effect|EntityWithHealthPrototype::dying_trigger_effect]]. Unknown if it works with other properties that use [[TriggerEffect]].
