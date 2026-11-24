---
title: UseItemAchievementPrototype
tags: [factorio-api, prototype]
---
# UseItemAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `use-item-achievement`

This prototype is used for receiving an achievement when the player uses a capsule.

## Properties

### to_use
- **Type:** [[ItemID (type)]]
This will trigger the achievement, if this capsule is used.
**Examples:**

```
to_use = "raw-fish"
```

### limit_quality
- **Type:** [[QualityID (type)]]

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many capsules need to be used.

### limited_to_one_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false, the player carries over their statistics from this achievement through all their saves.
