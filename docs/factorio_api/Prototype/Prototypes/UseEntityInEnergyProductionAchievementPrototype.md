---
title: UseEntityInEnergyProductionAchievementPrototype
tags: [factorio-api, prototype]
---
# UseEntityInEnergyProductionAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `use-entity-in-energy-production-achievement`

This prototype is used for receiving an achievement when the player produces energy by entity.

## Properties

### entity
- **Type:** [[EntityID (type)]]
This entity is needed to produce energy, for the player to complete the achievement.
**Examples:**

```
entity = "steam-engine"
```

### consumed_condition
- **Type:** [[ItemIDFilter (type)]]
- **Optional**
This item need to be consumed before gaining the achievement.
**Examples:**

```
consumed_condition = "uranium-fuel-cell"
```

### produced_condition
- **Type:** [[ItemIDFilter (type)]]
- **Optional**
This item needs to be produced before gaining the achievement.

### required_to_build
- **Type:** [[EntityID (type)]]
- **Optional**
This item need to be built before gaining the achievement.
**Examples:**

```
required_to_build = "nuclear-reactor"
```
