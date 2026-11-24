---
title: PlayerDamagedAchievementPrototype
tags: [factorio-api, prototype]
---
# PlayerDamagedAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `player-damaged-achievement`

This prototype is used for receiving an achievement when the player receives damage.

## Properties

### minimum_damage
- **Type:** [[float (type)]]
This will trigger the achievement, if the amount of damage taken by the dealer, is more than this.
**Examples:**

```
minimum_damage = 500
```

### should_survive
- **Type:** [[boolean (type)]]
This sets the achievement to only trigger, if you survive the minimum amount of damage. If you don't need to survive, false.
**Examples:**

```
should_survive = true
```

### type_of_dealer
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
This will trigger the achievement, if the player takes damage from this specific entity type.
**Examples:**

```
type_of_dealer = "locomotive"
```
