---
title: PuddleTileEffectParameters
tags: [factorio-api, prototype, type]
---
# PuddleTileEffectParameters

## Properties

### puddle_noise_texture
- **Type:** [[EffectTexture]]

### water_effect_parameters
- **Type:** [[WaterTileEffectParameters]]
- **Optional**

### water_effect
- **Type:** [[TileEffectDefinitionID]]
- **Optional**
Only loaded, and mandatory if `water_effect_parameters` is not defined. Must be name of a [[TileEffectDefinition]] which has `shader` set to `"water"`.
