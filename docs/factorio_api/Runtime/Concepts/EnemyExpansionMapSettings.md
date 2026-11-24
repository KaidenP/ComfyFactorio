---
title: EnemyExpansionMapSettings
tags: [factorio-api, runtime, concept]
---
# EnemyExpansionMapSettings

Candidate chunks are given scores to determine which one of them should be expanded into. This score takes into account various settings noted below. The iteration is over a square region centered around the chunk for which the calculation is done, and includes the central chunk as well. Distances are calculated as [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance).

The pseudocode algorithm to determine a chunk's score is as follows:

```
player = 0
for neighbour in all chunks within enemy_building_influence_radius from chunk :
  if neighbour has player buildings :
    player += neighbouring_chunk_coefficient ^ distance(chunk, neighbour)
      * building_coefficient
base = 0
for neighbour in all chunks within friendly_base_influence_radius from chunk :
  if neighbour has enemy bases :
    base += neighbouring_base_chunk_coefficient ^ distance(chunk, neighbour)
      * other_base_coefficient
score(chunk) = 1 / (1 + player + base)
```

## Fields

### enabled
- **Type:** [[boolean]]
Whether enemy expansion is enabled at all.

### max_expansion_distance
- **Type:** [[uint32]]
Distance in chunks from the furthest base around to prevent expansions from reaching too far into the player's territory. Defaults to `5`.

### min_expansion_distance
- **Type:** [[uint32]]
Distance in chunks from the furthest base around to prevent expansions from being too close to existing bases. Defaults to `3`.

### friendly_base_influence_radius
- **Type:** [[uint32]]
Defaults to `6`.

### enemy_building_influence_radius
- **Type:** [[uint32]]
Defaults to `3`.

### building_coefficient
- **Type:** [[double]]
Defaults to `0.5`.

### other_base_coefficient
- **Type:** [[double]]
Defaults to `3.0`.

### neighbouring_chunk_coefficient
- **Type:** [[double]]
Defaults to `0.5`.

### neighbouring_base_chunk_coefficient
- **Type:** [[double]]
Defaults to `0.5`.

### max_colliding_tiles_coefficient
- **Type:** [[double]]
A chunk has to have at most this high of a percentage of unbuildable tiles for it to be considered a candidate to avoid chunks full of water as candidates. Defaults to `0.8`, or 80%.

### settler_group_min_size
- **Type:** [[uint32]]
The minimum size of a biter group that goes to build a new base. This is multiplied by the evolution factor. Defaults to `5`.

### settler_group_max_size
- **Type:** [[uint32]]
The maximum size of a biter group that goes to build a new base. This is multiplied by the evolution factor. Defaults to `10`.

### min_expansion_cooldown
- **Type:** [[uint32]]
The minimum time between expansions in ticks. The actual cooldown is adjusted to the current evolution levels. Defaults to `10*3 600=36 000` ticks.

### max_expansion_cooldown
- **Type:** [[uint32]]
The maximum time between expansions in ticks. The actual cooldown is adjusted to the current evolution levels. Defaults to `60*3 600=216 000` ticks.

### build_base_unit_dispatch_cooldown
- **Type:** [[uint32]]
Cooldown in ticks for dispatching units when building bases. Defaults to `60*30=1 800` ticks.
