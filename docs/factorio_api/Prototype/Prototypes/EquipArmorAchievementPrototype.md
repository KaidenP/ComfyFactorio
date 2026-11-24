---
title: EquipArmorAchievementPrototype
tags: [factorio-api, prototype]
---
# EquipArmorAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `equip-armor-achievement`

This prototype is used for receiving an achievement when the player equips armor.

## Properties

### armor
- **Type:** [[ItemID (type)]]
The achievement will trigger if this armor or the alternative armor is equipped.
**Examples:**

```
armor = "power-armor-mk2"
```

### alternative_armor
- **Type:** [[ItemID (type)]]
The achievement will trigger if this armor or the other armor is equipped.
**Examples:**

```
alternative_armor = "mech-armor"
```

### limit_quality
- **Type:** [[QualityID (type)]]

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many armors need to be equipped.

### limited_to_one_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false, the player carries over their statistics from this achievement through all their saves.
