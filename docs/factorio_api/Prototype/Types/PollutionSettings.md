---
title: PollutionSettings
tags: [factorio-api, prototype, type]
---
# PollutionSettings

The pollution settings, the values are for 60 ticks (1 second).

## Properties

### enabled
- **Type:** [[boolean (type)]]

### diffusion_ratio
- **Type:** [[double (type)]]
Amount that is diffused to neighboring chunks.

### min_to_diffuse
- **Type:** [[double (type)]]
This much pollution units must be on the chunk to start diffusing.

### ageing
- **Type:** [[double (type)]]
Constant modifier a percentage of 1; the pollution eaten by a chunks tiles. Also known as absorption modifier.

### expected_max_per_chunk
- **Type:** [[double (type)]]
Anything bigger than this is visualized as this value.

### min_to_show_per_chunk
- **Type:** [[double (type)]]
Anything lower than this (but > 0) is visualized as this value.

### min_pollution_to_damage_trees
- **Type:** [[double (type)]]

### pollution_with_max_forest_damage
- **Type:** [[double (type)]]

### pollution_restored_per_tree_damage
- **Type:** [[double (type)]]

### pollution_per_tree_damage
- **Type:** [[double (type)]]

### enemy_attack_pollution_consumption_modifier
- **Type:** [[double (type)]]
