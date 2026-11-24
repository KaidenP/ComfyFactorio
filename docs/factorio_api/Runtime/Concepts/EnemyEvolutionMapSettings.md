---
title: EnemyEvolutionMapSettings
tags: [factorio-api, runtime, concept]
---
# EnemyEvolutionMapSettings

These values represent a percentual increase in evolution. This means a value of `0.1` would increase evolution by 10%.

## Fields

### enabled
- **Type:** [[boolean]]
Whether enemy evolution is enabled at all.

### time_factor
- **Type:** [[double]]
The amount evolution naturally progresses by every second. Defaults to `0.000004`.

### destroy_factor
- **Type:** [[double]]
The amount evolution progresses for every destroyed spawner. Defaults to `0.002`.

### pollution_factor
- **Type:** [[double]]
The amount evolution progresses for every unit of pollution. Defaults to `0.0000009`.
