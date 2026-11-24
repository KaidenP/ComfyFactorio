---
title: BuildEntityAchievementPrototype
tags: [factorio-api, prototype]
---
# BuildEntityAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `build-entity-achievement`

This prototype is used for receiving an achievement when the player builds an entity.

## Properties

### to_build
- **Type:** [[EntityID (type)]]
This will trigger the achievement, if this entity is placed.
**Examples:**

```
to_build = "locomotive"
```

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many entities need to be built.

### limited_to_one_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false, the player carries over their statistics from this achievement through all their saves.

### within
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `math.huge`
The achievement must be completed within this time limit.
**Examples:**

```
within = 60 * 60 * 60 * 8 -- 8 hours
```
