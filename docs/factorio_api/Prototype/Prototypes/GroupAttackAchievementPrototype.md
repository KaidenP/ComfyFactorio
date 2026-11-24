---
title: GroupAttackAchievementPrototype
tags: [factorio-api, prototype]
---
# GroupAttackAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `group-attack-achievement`

This prototype is used for receiving an achievement when the player gets attacked due to pollution.

## Properties

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
This will trigger the achievement, if the player receives this amount of attacks. **Note**: The default achievement "it stinks and they don't like it" uses the amount of 1. (As in getting attacked once.)
**Examples:**

```
amount = 10
```

### entities
- **Type:** array<[[EntityID (type)]]>
- **Optional**
The achievement is only triggered if the attacking group of enemies contains at least one of the entities listed here.

### attack_type
- **Type:** `"autonomous"` | `"distraction"` | `"scripted"`
- **Optional**
The type of attack that triggers this achievement. "autonomous" attacks are triggered in response to pollution or a territory disturbance. "distraction" attacks are in response to taking damage or seeing a nearby enemy. "scripted" attacks are triggered from mods.
