---
title: CreatePollutionTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# CreatePollutionTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"create-pollution"`

### amount
- **Type:** [[double (type)]]
This may be negative which will reduce pollution when run.

### entity
- **Type:** [[EntityID (type)]]
- **Optional**
If not defined, and use_entity_from_trigger is false, the pollution does not show in statistics.

### use_entity_from_trigger
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If not set, and entity is not set, the pollution does not show in statistics.
