---
title: ProducePerHourAchievementPrototype
tags: [factorio-api, prototype]
---
# ProducePerHourAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `produce-per-hour-achievement`

This prototype is used for receiving an achievement when the player crafts a specified item a certain amount, in an hour.

## Properties

### amount
- **Type:** [[MaterialAmountType]]
This is how much the player has to craft in an hour, to receive the achievement.
**Examples:**

```
amount = 1000
```

### item_product
- **Type:** [[ItemIDFilter (type)]]
- **Optional**
Mandatory if `fluid_product` is not defined.

This will tell the achievement what item the player needs to craft, to get the achievement.
**Examples:**

```
item_product = "landfill"
```

### fluid_product
- **Type:** [[FluidID (type)]]
- **Optional**
Mandatory if `item_product` is not defined.

This will tell the achievement what fluid the player needs to craft, to get the achievement.
**Examples:**

```
fluid_product = "light-oil"
```
