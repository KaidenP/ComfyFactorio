---
title: ShootAchievementPrototype
tags: [factorio-api, prototype]
---
# ShootAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `shoot-achievement`

This prototype is used for receiving an achievement when the player shoots certain ammo.

## Properties

### ammo_type
- **Type:** [[ItemID (type)]]
- **Optional**
This will trigger the achievement, if this ammo is shot.
**Examples:**

```
ammo_type = "atomic-bomb"
```

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How much of the ammo needs to be shot.
