---
title: ModuleTransferAchievementPrototype
tags: [factorio-api, prototype]
---
# ModuleTransferAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `module-transfer-achievement`

This prototype is used for receiving an achievement when the player moves a module with the cursor.

## Properties

### module
- **Type:** [[ItemID (type)]] | array<[[ItemID (type)]]>
This will trigger the achievement, if this module is transferred.
**Examples:**

```
module = "quality-module"
```

### amount
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
How many modules need to be transferred.

### limited_to_one_game
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is false, the player carries over their statistics from this achievement through all their saves.
