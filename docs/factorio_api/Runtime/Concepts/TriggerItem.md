---
title: TriggerItem
tags: [factorio-api, runtime, concept]
---
# TriggerItem

## Fields

### type
- **Type:** `"direct"` | `"area"` | `"line"` | `"cluster"`

### action_delivery
- **Type:** array<[[TriggerDelivery]]>
- **Optional**

### entity_flags
- **Type:** [[EntityPrototypeFlags]]
- **Optional**
The trigger will only affect entities that contain any of these flags.

### ignore_collision_condition
- **Type:** [[boolean]]

### collision_mask
- **Type:** [[CollisionMask]]
The trigger will only affect entities that would collide with given collision mask.

### trigger_target_mask
- **Type:** [[TriggerTargetMask]]

### force
- **Type:** [[ForceCondition]]
If `"enemy"`, the trigger will only affect entities whose force is different from the attacker's and for which there is no cease-fire set. `"ally"` is the opposite of `"enemy"`.

### repeat_count
- **Type:** [[uint32]]

### probability
- **Type:** [[float]]
