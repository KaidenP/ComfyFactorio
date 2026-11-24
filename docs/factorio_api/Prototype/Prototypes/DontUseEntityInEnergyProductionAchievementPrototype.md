---
title: DontUseEntityInEnergyProductionAchievementPrototype
tags: [factorio-api, prototype]
---
# DontUseEntityInEnergyProductionAchievementPrototype

> **Parent:** [[AchievementPrototypeWithCondition]] · **Type name:** `dont-use-entity-in-energy-production-achievement`

This prototype is used for receiving an achievement when the player finishes the game without receiving energy from a specific energy source.

## Properties

### excluded
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
This will **not** disable the achievement, if this entity is placed, and you have received any amount of power from it.
**Examples:**

```
excluded = {"steam-engine", "steam-turbine"}
```

### included
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**
This will disable the achievement, if this entity is placed, and you have received any amount of power from it. If you finish the game without receiving power from this entity, you receive the achievement.
**Examples:**

```
included = "solar-panel"
```

### last_hour_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the achievements will only be checked for the last hour of the game, independently of finishing the game.

### minimum_energy_produced
- **Type:** [[Energy]]
- **Optional**
- **Default:** `"0J"`
The minimum amount of energy that needs to be produced by the allowed entities to trigger the achievement.
