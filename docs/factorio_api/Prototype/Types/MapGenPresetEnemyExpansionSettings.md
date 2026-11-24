---
title: MapGenPresetEnemyExpansionSettings
tags: [factorio-api, prototype, type]
---
# MapGenPresetEnemyExpansionSettings

## Properties

### enabled
- **Type:** [[boolean (type)]]
- **Optional**

### min_expansion_distance
- **Type:** [[uint32 (type)]]
- **Optional**
Distance in chunks from the furthest base around to prevent expansions from being too close to existing bases.

### max_expansion_distance
- **Type:** [[uint32 (type)]]
- **Optional**
Distance in chunks from the furthest base around. This prevents expansions from reaching too far into the player's territory.

### settler_group_min_size
- **Type:** [[uint32 (type)]]
- **Optional**
Size of the group that goes to build new base (the game interpolates between min size and max size based on evolution factor).

### settler_group_max_size
- **Type:** [[uint32 (type)]]
- **Optional**

### evolution_group_size_factor
- **Type:** [[double (type)]]
- **Optional**
Factor by which the evolution factor influences the size of the settler group

### min_expansion_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
Ticks to expand to a single position for a base is used. Cooldown is calculated as follows: `cooldown = lerp(max_expansion_cooldown, min_expansion_cooldown, -e^2 + 2 * e)` where `lerp` is the linear interpolation function, and e is the current evolution factor.

### max_expansion_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
In ticks.

### build_base_unit_dispatch_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
Cooldown in ticks for dispatching units when building bases.
