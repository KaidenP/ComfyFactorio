---
title: MapSettings
tags: [factorio-api, runtime, concept]
---
# MapSettings

Various game-related settings. Updating any of the attributes will immediately take effect in the game engine.

## Fields

### pollution
- **Type:** [[PollutionMapSettings]]
- **Writable:** [[PollutionMapSettings]]

### enemy_evolution
- **Type:** [[EnemyEvolutionMapSettings]]
- **Writable:** [[EnemyEvolutionMapSettings]]

### enemy_expansion
- **Type:** [[EnemyExpansionMapSettings]]
- **Writable:** [[EnemyExpansionMapSettings]]

### unit_group
- **Type:** [[UnitGroupMapSettings]]
- **Writable:** [[UnitGroupMapSettings]]

### path_finder
- **Type:** [[PathFinderMapSettings]]
- **Writable:** [[PathFinderMapSettings]]

### asteroids
- **Type:** [[AsteroidMapSettings]]
- **Writable:** [[AsteroidMapSettings]]

### max_failed_behavior_count
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
If a behavior fails this many times, the enemy (or enemy group) is destroyed. This solves biters getting stuck within their own base.

## Examples

```
-- Increase the number of short paths the pathfinder can cache.
game.map_settings.path_finder.short_cache_size = 15
```
