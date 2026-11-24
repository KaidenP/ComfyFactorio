---
title: DamageEntityTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# DamageEntityTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"damage"`

### damage
- **Type:** [[DamageParameters (type)]]

### apply_damage_to_trees
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### vaporize
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, no corpse for killed entities will be created.

### use_substitute
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### lower_distance_threshold
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** MAX_UINT16

### upper_distance_threshold
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** MAX_UINT16

### lower_damage_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### upper_damage_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
