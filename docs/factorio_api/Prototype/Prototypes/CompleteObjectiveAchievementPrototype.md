---
title: CompleteObjectiveAchievementPrototype
tags: [factorio-api, prototype]
---
# CompleteObjectiveAchievementPrototype

> **Parent:** [[AchievementPrototypeWithCondition]] · **Type name:** `complete-objective-achievement`

## Properties

### within
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `math.huge`
The achievement must be completed within this time limit.
**Examples:**

```
within = 60 * 60 * 60 * 8 -- 8 hours
```
