---
title: TriggerItem
tags: [factorio-api, prototype, type]
---
# TriggerItem

*Note: `TriggerItem (type)`.*

> **Abstract**

The abstract base of all [[Trigger|Triggers]].

## Properties

### entity_flags
- **Type:** [[EntityPrototypeFlags (type)]]
- **Optional**
- **Default:** All flags
Only prototypes with these flags are affected by the trigger item.

### collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
- **Default:** All masks
Only prototypes with these collision masks are affected by the trigger item.

### ignore_collision_condition
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### trigger_target_mask
- **Type:** [[TriggerTargetMask (type)]]
- **Optional**
- **Default:** Everything
The trigger affects only prototypes with these masks.

### repeat_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`

### probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be greater than 0 and less than or equal to 1.

### action_delivery
- **Type:** [[TriggerDelivery (type)]] | array<[[TriggerDelivery (type)]]>
- **Optional**

### force
- **Type:** [[ForceCondition (type)]]
- **Optional**
- **Default:** All forces
Only entities meeting the force condition are affected by the trigger item.
