---
title: SpaceConnectionAsteroidSpawnDefinition
tags: [factorio-api, prototype, type]
---
# SpaceConnectionAsteroidSpawnDefinition

*Note: `SpaceConnectionAsteroidSpawnDefinition (type)`.*

## Type

struct | ([[EntityID (type)]], array<[[SpaceConnectionAsteroidSpawnPoint (type)]]>)

## Properties

### type
- **Type:** `"entity"` | `"asteroid-chunk"`
- **Optional**
- **Default:** `"entity"`

### asteroid
- **Type:** [[EntityID (type)]] | [[AsteroidChunkID (type)]]
The type this is loaded as depends on `type`.

### spawn_points
- **Type:** array<[[SpaceConnectionAsteroidSpawnPoint (type)]]>
