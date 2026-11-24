---
title: MapAndDifficultySettings
tags: [factorio-api, runtime, concept]
---
# MapAndDifficultySettings

A standard table containing all [[MapSettings]] attributes plus an additional table that contains all [[DifficultySettings]] properties.

## Fields

### pollution
- **Type:** [[PollutionMapSettings]]

### enemy_evolution
- **Type:** [[EnemyEvolutionMapSettings]]

### enemy_expansion
- **Type:** [[EnemyExpansionMapSettings]]

### unit_group
- **Type:** [[UnitGroupMapSettings]]

### path_finder
- **Type:** [[PathFinderMapSettings]]

### asteroids
- **Type:** [[AsteroidMapSettings]]

### max_failed_behavior_count
- **Type:** [[uint32]]
If a behavior fails this many times, the enemy (or enemy group) is destroyed. This solves biters getting stuck within their own base.

### difficulty_settings
- **Type:** [[MapDifficultySettings]]
