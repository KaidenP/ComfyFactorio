---
title: ResearchAchievementPrototype
tags: [factorio-api, prototype]
---
# ResearchAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `research-achievement`

This prototype is used for receiving an achievement when the player completes a specific research.

## Properties

### technology
- **Type:** [[TechnologyID (type)]]
- **Optional**
Mandatory if `research_all` is not defined.

Researching this technology will trigger the achievement.
**Examples:**

```
technology = "oil-processing"
```

### research_all
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Mandatory if `technology` is not defined.

This will only trigger if the player has learned every research in the game.
**Examples:**

```
research_all = true
```
