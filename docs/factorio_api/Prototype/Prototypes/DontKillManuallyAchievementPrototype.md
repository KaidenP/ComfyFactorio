---
title: DontKillManuallyAchievementPrototype
tags: [factorio-api, prototype]
---
# DontKillManuallyAchievementPrototype

> **Parent:** [[AchievementPrototypeWithCondition]] · **Type name:** `dont-kill-manually-achievement`

This prototype is used for receiving an achievement when the player kill first entity using artillery.

## Properties

### to_kill
- **Type:** [[EntityID (type)]]
- **Optional**
This will disable the achievement, if this entity is killed manually. If you kill this entity with artillery first, you receive the achievement.

### type_not_to_kill
- **Type:** [[string (type)]]
- **Optional**
This will disable the achievement, if this entity type is killed manually. If you kill this entity type with artillery first, you receive the achievement.
**Examples:**

```
type_not_to_kill = "unit-spawner"
```
