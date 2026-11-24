---
title: ProduceAchievementPrototype
tags: [factorio-api, prototype]
---
# ProduceAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `produce-achievement`

This prototype is used for receiving an achievement when the player produces more than the specified amount of items.

## Properties

### amount
- **Type:** [[MaterialAmountType]]
This will set the amount of items or fluids needed to craft, for the player to complete the achievement.
**Examples:**

```
amount = 100
```

### limited_to_one_game
- **Type:** [[boolean (type)]]
If this is false, the player carries over their statistics from this achievement through all their saves.

### item_product
- **Type:** [[ItemIDFilter (type)]]
- **Optional**
Mandatory if `fluid_product` is not defined.

This will tell the achievement what item the player needs to craft, to get the achievement.
**Examples:**

```
item_product = "pistol"
```

### fluid_product
- **Type:** [[FluidID (type)]]
- **Optional**
Mandatory if `item_product` is not defined.

This will tell the achievement what fluid the player needs to craft, to get the achievement.
**Examples:**

```
fluid_product = "heavy-oil"
```
