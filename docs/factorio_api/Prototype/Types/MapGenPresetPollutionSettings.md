---
title: MapGenPresetPollutionSettings
tags: [factorio-api, prototype, type]
---
# MapGenPresetPollutionSettings

The pollution settings, the values are for 60 ticks (1 second).

## Properties

### enabled
- **Type:** [[boolean (type)]]
- **Optional**

### diffusion_ratio
- **Type:** [[double (type)]]
- **Optional**
Must be <= 0.25. Amount that is diffused to neighboring chunks.

### ageing
- **Type:** [[double (type)]]
- **Optional**
Must be >= 0.1. Also known as absorption modifier.

### min_pollution_to_damage_trees
- **Type:** [[double (type)]]
- **Optional**

### enemy_attack_pollution_consumption_modifier
- **Type:** [[double (type)]]
- **Optional**
Must be >= 0.1.

### pollution_restored_per_tree_damage
- **Type:** [[double (type)]]
- **Optional**
