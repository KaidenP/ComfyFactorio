---
title: DepleteResourceAchievementPrototype
tags: [factorio-api, prototype]
---
# DepleteResourceAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `deplete-resource-achievement`

This prototype is used for receiving an achievement when a resource entity is depleted.

## Properties

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many resource entities need to be depleted.

### limited_to_one_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false, the player carries over their statistics from this achievement through all their saves.
