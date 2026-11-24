---
title: MapSettings
tags: [factorio-api, prototype]
---
# MapSettings

*Note: `MapSettings (prototype)`.*

> **Type name:** `map-settings` · **Instance limit:** 1

The default map settings.

## Properties

### type
- **Type:** `"map-settings"`

### name
- **Type:** [[string (type)]]
Name of the map-settings. Base game uses "map-settings".

### pollution
- **Type:** [[PollutionSettings]]

### enemy_evolution
- **Type:** [[EnemyEvolutionSettings]]

### enemy_expansion
- **Type:** [[EnemyExpansionSettings]]

### unit_group
- **Type:** [[UnitGroupSettings]]

### path_finder
- **Type:** [[PathFinderSettings]]

### max_failed_behavior_count
- **Type:** [[uint32 (type)]]
If a behavior fails this many times, the enemy (or enemy group) is destroyed. This solves biters stuck within their own base.

### difficulty_settings
- **Type:** [[DifficultySettings (type)]]

### asteroids
- **Type:** [[AsteroidSettings]]
