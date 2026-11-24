---
title: SpawnPoint
tags: [factorio-api, prototype, type]
---
# SpawnPoint

The definition of a evolution and probability weights for a [[UnitSpawnDefinition (type)|spawnable unit]] for a [[EnemySpawnerPrototype]].

It can be specified as a table with named or numbered keys, but not a mix of both. If this is specified as a table with numbered keys then the first value is the evolution factor and the second is the spawn weight.

## Type

struct | ([[double (type)]], [[double (type)]])

## Properties

### evolution_factor
- **Type:** [[double (type)]]

### spawn_weight
- **Type:** [[double (type)]]
Must be `>= 0`.
