---
title: DelayedActiveTriggerPrototype
tags: [factorio-api, prototype]
---
# DelayedActiveTriggerPrototype

> **Parent:** [[ActiveTriggerPrototype]] · **Type name:** `delayed-active-trigger`

Delays the delivery of triggered effect by some number of ticks.

## Properties

### action
- **Type:** [[Trigger]]
The trigger to apply after `delay` has elapsed.

### delay
- **Type:** [[uint32 (type)]]
The number of ticks to delay the delivery of the triggered effect. Must be greater than 0.

### repeat_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
The number of times to repeat the delayed trigger.

### repeat_delay
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `delay`
The number of ticks between repeat deliveries of the triggered effect. Must be greater than 0.

### cancel_when_source_is_destroyed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, the delayed trigger is cancelled if the source entity is destroyed.
