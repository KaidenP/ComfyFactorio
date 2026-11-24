---
title: on_achievement_gained
tags: [factorio-api, runtime, event]
---
# on_achievement_gained

Called when an achievement is gained.

## Data

### player_index
- **Type:** [[uint32]]
The player who gained the achievement.

### achievement
- **Type:** [[LuaAchievementPrototype]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
