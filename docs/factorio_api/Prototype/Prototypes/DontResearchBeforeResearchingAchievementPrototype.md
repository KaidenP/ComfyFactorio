---
title: DontResearchBeforeResearchingAchievementPrototype
tags: [factorio-api, prototype]
---
# DontResearchBeforeResearchingAchievementPrototype

> **Parent:** [[AchievementPrototypeWithCondition]] · **Type name:** `dont-research-before-researching-achievement`

This prototype is used for receiving an achievement when the player researches with a specific science pack before unlocking another.

## Properties

### dont_research
- **Type:** [[ItemID (type)]] | array<[[ItemID (type)]]>
This will disable the achievement, if technology unlocking this item is researched before meeting requirements.
**Examples:**

```
dont_research = {"production-science-pack", "utility-science-pack"}
```

### research_with
- **Type:** [[ItemID (type)]] | array<[[ItemID (type)]]>
If you research technology using one of specified items, you receive the achievement.
**Examples:**

```
research_with = {"metallurgic-science-pack", "electromagnetic-science-pack", "agricultural-science-pack"}
```
