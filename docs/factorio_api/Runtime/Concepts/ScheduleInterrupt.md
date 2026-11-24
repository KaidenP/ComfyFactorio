---
title: ScheduleInterrupt
tags: [factorio-api, runtime, concept]
---
# ScheduleInterrupt

## Fields

### name
- **Type:** [[string]]
- **Optional**
Defaults to an empty string.

### conditions
- **Type:** array<[[WaitCondition]]>
- **Optional**

### targets
- **Type:** array<[[ScheduleRecord]]>
- **Optional**

### inside_interrupt
- **Type:** [[boolean]]
- **Optional**
Defaults to `false`.
