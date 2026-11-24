---
title: PathFinderMapSettings
tags: [factorio-api, runtime, concept]
---
# PathFinderMapSettings

## Fields

### fwd2bwd_ratio
- **Type:** [[uint32]]
The pathfinder performs a step of the backward search every `fwd2bwd_ratio`'th step. The minimum allowed value is `2`, which means symmetric search. The default value is `5`.

### goal_pressure_ratio
- **Type:** [[double]]
When looking at which node to check next, their heuristic value is multiplied by this ratio. The higher it is, the more the search is directed straight at the goal. Defaults to `2`.

### use_path_cache
- **Type:** [[boolean]]
Whether to cache paths at all. Defaults to `true`.

### max_steps_worked_per_tick
- **Type:** [[double]]
The maximum number of nodes that are expanded per tick. Defaults to `1 000`.

### max_work_done_per_tick
- **Type:** [[uint32]]
The maximum amount of work each pathfinding job is allowed to do per tick. Defaults to `8 000`.

### short_cache_size
- **Type:** [[uint32]]
Number of elements in the short cache. Defaults to `5`.

### long_cache_size
- **Type:** [[uint32]]
Number of elements in the long cache. Defaults to `25`.

### short_cache_min_cacheable_distance
- **Type:** [[double]]
The minimal distance to the goal in tiles required to be searched in the short path cache. Defaults to `10`.

### short_cache_min_algo_steps_to_cache
- **Type:** [[uint32]]
The minimal number of nodes required to be searched in the short path cache. Defaults to `50`.

### long_cache_min_cacheable_distance
- **Type:** [[double]]
The minimal distance to the goal in tiles required to be searched in the long path cache. Defaults to `30`.

### cache_max_connect_to_cache_steps_multiplier
- **Type:** [[uint32]]
When looking for a connection to a cached path, search at most for this number of steps times the original estimate. Defaults to `100`.

### cache_accept_path_start_distance_ratio
- **Type:** [[double]]
When looking for a path from cache, make sure it doesn't start too far from the requested start in relative terms. Defaults to `0.2`.

### cache_accept_path_end_distance_ratio
- **Type:** [[double]]
When looking for a path from cache, make sure it doesn't end too far from the requested end in relative terms. This is typically more lenient than the start ratio since the end target could be moving. Defaults to `0.15`.

### negative_cache_accept_path_start_distance_ratio
- **Type:** [[double]]
Same principle as `cache_accept_path_start_distance_ratio`, but used for negative cache queries. Defaults to `0.3`.

### negative_cache_accept_path_end_distance_ratio
- **Type:** [[double]]
Same principle as `cache_accept_path_end_distance_ratio`, but used for negative cache queries. Defaults to `0.3`.

### cache_path_start_distance_rating_multiplier
- **Type:** [[double]]
When assigning a rating to the best path, this multiplier times start distances is considered. Defaults to `10`.

### cache_path_end_distance_rating_multiplier
- **Type:** [[double]]
When assigning a rating to the best path, this multiplier times end distances is considered. This value is typically higher than the start multiplier as this results in better end path quality. Defaults to `20`.

### stale_enemy_with_same_destination_collision_penalty
- **Type:** [[double]]
A penalty that is applied for another unit that is on the way to the goal. This is mainly relevant for situations where a group of units has arrived at the target they are supposed to attack, making units further back circle around to reach the target. Defaults to `30`.

### ignore_moving_enemy_collision_distance
- **Type:** [[double]]
The distance in tiles after which other moving units are not considered for pathfinding. Defaults to `5`.

### enemy_with_different_destination_collision_penalty
- **Type:** [[double]]
A penalty that is applied for another unit that is too close and either not moving or has a different goal. Defaults to `30`.

### general_entity_collision_penalty
- **Type:** [[double]]
The general collision penalty with other units. Defaults to `10`.

### general_entity_subsequent_collision_penalty
- **Type:** [[double]]
The collision penalty for positions that require the destruction of an entity to get to. Defaults to `3`.

### extended_collision_penalty
- **Type:** [[double]]
The collision penalty for collisions in the extended bounding box but outside the entity's actual bounding box. Defaults to `3`.

### max_clients_to_accept_any_new_request
- **Type:** [[uint32]]
The amount of path finder requests accepted per tick regardless of the requested path's length. Defaults to `10`.

### max_clients_to_accept_short_new_request
- **Type:** [[uint32]]
When the `max_clients_to_accept_any_new_request` amount is exhausted, only path finder requests with a short estimate will be accepted until this amount (per tick) is reached. Defaults to `100`.

### direct_distance_to_consider_short_request
- **Type:** [[uint32]]
The maximum direct distance in tiles before a request is no longer considered short. Defaults to `100`.

### short_request_max_steps
- **Type:** [[uint32]]
The maximum amount of nodes a short request will traverse before being rescheduled as a long request. Defaults to `1000`.

### short_request_ratio
- **Type:** [[double]]
The amount of steps that are allocated to short requests each tick, as a percentage of all available steps. Defaults to `0.5`, or 50%.

### min_steps_to_check_path_find_termination
- **Type:** [[uint32]]
The minimum amount of steps that are guaranteed to be performed for every request. Defaults to `2000`.

### start_to_goal_cost_multiplier_to_terminate_path_find
- **Type:** [[double]]
If the actual amount of steps is higher than the initial estimate by this factor, pathfinding is terminated. Defaults to `2000.0`.

### overload_levels
- **Type:** array<[[uint32]]>
The thresholds of waiting clients after each of which the per-tick work limit will be increased by the corresponding value in `overload_multipliers`. This is to avoid clients having to wait too long. Must have the same number of elements as `overload_multipliers`. Defaults to `{0, 100, 500}`.

### overload_multipliers
- **Type:** array<[[double]]>
The multipliers to the amount of per-tick work applied after the corresponding thresholds in `overload_levels` have been reached. Must have the same number of elements as `overload_multipliers`. Defaults to `{2, 3, 4}`.

### negative_path_cache_delay_interval
- **Type:** [[uint32]]
The delay in ticks between decrementing the score of all paths in the negative cache by one. Defaults to `20`.
