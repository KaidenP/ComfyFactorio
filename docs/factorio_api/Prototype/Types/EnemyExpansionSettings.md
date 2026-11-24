---
title: EnemyExpansionSettings
tags: [factorio-api, prototype, type]
---
# EnemyExpansionSettings

## Properties

### enabled
- **Type:** [[boolean (type)]]

### max_expansion_distance
- **Type:** [[uint32 (type)]]
Distance in chunks from the furthest base around. This prevents expansions from reaching too far into the player's territory.

### min_expansion_distance
- **Type:** [[uint32 (type)]]
Distance in chunks from the furthest base around to prevent expansions from being too close to existing bases.

### friendly_base_influence_radius
- **Type:** [[uint32 (type)]]

### enemy_building_influence_radius
- **Type:** [[uint32 (type)]]

### building_coefficient
- **Type:** [[double (type)]]

### other_base_coefficient
- **Type:** [[double (type)]]

### neighbouring_chunk_coefficient
- **Type:** [[double (type)]]

### neighbouring_base_chunk_coefficient
- **Type:** [[double (type)]]

### max_colliding_tiles_coefficient
- **Type:** [[double (type)]]
A chunk has to have at most this much percent unbuildable tiles for it to be considered a candidate. This is to avoid chunks full of water to be marked as candidates.

### settler_group_min_size
- **Type:** [[uint32 (type)]]
Size of the group that goes to build new base.

### settler_group_max_size
- **Type:** [[uint32 (type)]]

### evolution_group_size_factor
- **Type:** [[double (type)]]
Exponential factor used to determine the size of the settler group based on the evolution factor. The size is calculated as: `size = random(min_size, max_size) * (evolution_group_size_factor ^ evolution_factor)`

### min_expansion_cooldown
- **Type:** [[uint32 (type)]]
Ticks to expand to a single position for a base is used. Cooldown is calculated as follows: `cooldown = lerp(max_expansion_cooldown, min_expansion_cooldown, -e^2 + 2 * e)` where `lerp` is the linear interpolation function, and e is the current evolution factor.

### max_expansion_cooldown
- **Type:** [[uint32 (type)]]
In ticks.

### build_base_unit_dispatch_cooldown
- **Type:** [[uint32 (type)]]
Cooldown in ticks for dispatching units when building bases.
