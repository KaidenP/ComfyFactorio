---
title: AchievementPrototypeWithCondition
tags: [factorio-api, prototype]
---
# AchievementPrototypeWithCondition

> **Parent:** [[AchievementPrototype]] · **Abstract**

## Properties

### objective_condition
- **Type:** `"game-finished"` | `"rocket-launched"` | `"late-research"`
- **Optional**
The condition that needs to be met to receive the achievement. Required for `"complete-objective-achievement"`, `"dont-build-entity-achievement"`, and `"dont-craft-manually-achievement"`. Not allowed for `"dont-kill-manually-achievement"` and `"dont-research-before-researching-achievement"`. Only allowed for `"dont-use-entity-in-energy-production-achievement"` if `"last_hour_only"` is `false`.
