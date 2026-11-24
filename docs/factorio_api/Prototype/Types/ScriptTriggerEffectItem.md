---
title: ScriptTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# ScriptTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"script"`

### effect_id
- **Type:** [[string (type)]]
The effect ID that will be provided in [[on_script_trigger_effect]].

### custom_event
- **Type:** [[CustomEventID]]
- **Optional**
Event to be raised. When set, that event will be raised instead of [[on_script_trigger_effect]].
