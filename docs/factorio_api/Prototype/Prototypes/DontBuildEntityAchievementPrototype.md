---
title: DontBuildEntityAchievementPrototype
tags: [factorio-api, prototype]
---
# DontBuildEntityAchievementPrototype

> **Parent:** [[AchievementPrototypeWithCondition]] · **Type name:** `dont-build-entity-achievement`

This prototype is used for receiving an achievement when the player finishes the game without building a specific entity.

## Properties

### dont_build
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
This will disable the achievement, if this entity is placed. If you finish the game without building this entity, you receive the achievement.
**Examples:**

```
dont_build = {"bulk-inserter", "fluid-wagon"}
```

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### research_with
- **Type:** [[ItemID (type)]] | array<[[ItemID (type)]]>
- **Optional**
If you research technology using one of specified items before building entity, you receive the achievement.
