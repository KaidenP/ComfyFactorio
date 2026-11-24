---
title: ConstructWithRobotsAchievementPrototype
tags: [factorio-api, prototype]
---
# ConstructWithRobotsAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `construct-with-robots-achievement`

This prototype is used for receiving an achievement when the player constructs enough entities with construction robots.

## Properties

### limited_to_one_game
- **Type:** [[boolean (type)]]
If this is false, the player carries over their statistics from this achievement through all their saves.

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
This will trigger the achievement, if enough entities were placed using construction robots.
**Examples:**

```
amount = 100
```

### more_than_manually
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
