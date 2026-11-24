---
title: PathFinderSettings
tags: [factorio-api, prototype, type]
---
# PathFinderSettings

## Properties

### fwd2bwd_ratio
- **Type:** [[uint32 (type)]]
The pathfinder performs a step of the backward search every `fwd2bwd_ratio`'th step. The minimum allowed value is 2, which means symmetric search.

### goal_pressure_ratio
- **Type:** [[double (type)]]
When comparing nodes in open which one to check next, heuristic value is multiplied by this ratio. The higher the number the more is the search directed directly towards the goal.

### use_path_cache
- **Type:** [[boolean (type)]]

### max_steps_worked_per_tick
- **Type:** [[double (type)]]
When this is exhausted no more requests are allowed, at the moment the first path to exhaust this will be finished (even if it is hundreds of steps).

### max_work_done_per_tick
- **Type:** [[uint32 (type)]]

### short_cache_size
- **Type:** [[uint32 (type)]]
Number of elements in the cache.

### long_cache_size
- **Type:** [[uint32 (type)]]

### short_cache_min_cacheable_distance
- **Type:** [[double (type)]]
Minimal distance to goal for path to be searched in short path cache.

### short_cache_min_algo_steps_to_cache
- **Type:** [[uint32 (type)]]
Minimal number of algorithm steps for path to be inserted into the short path cache.

### long_cache_min_cacheable_distance
- **Type:** [[double (type)]]
Minimal distance to goal for path to be searched in long path cache.

### cache_max_connect_to_cache_steps_multiplier
- **Type:** [[uint32 (type)]]
When searching for connection to path cache path, search at most for this number of steps times the initial estimate.

### cache_accept_path_start_distance_ratio
- **Type:** [[double (type)]]
When looking for path from cache make sure it doesn't start too far from requested start in relative distance terms.

### cache_accept_path_end_distance_ratio
- **Type:** [[double (type)]]
When looking for path from cache make sure it doesn't end too far from requested end. This is typically higher than accept value for the start because the end target can be moving.

### negative_cache_accept_path_start_distance_ratio
- **Type:** [[double (type)]]
Same as cache_accept_path_start_distance_ratio, but used for negative cache queries.

### negative_cache_accept_path_end_distance_ratio
- **Type:** [[double (type)]]
Same as cache_accept_path_end_distance_ratio, but used for negative cache queries.

### cache_path_start_distance_rating_multiplier
- **Type:** [[double (type)]]
When assigning rating to the best path this * start distances is considered.

### cache_path_end_distance_rating_multiplier
- **Type:** [[double (type)]]
When assigning rating to the best path this * end distances is considered. This is typically higher than value for the start to achieve better path end quality.

### stale_enemy_with_same_destination_collision_penalty
- **Type:** [[double (type)]]
Somewhere along the path is stuck enemy we need to avoid. This is mainly to handle situations when units have arrived and are attacking the target then units further in the back will use this and run around the target.

### ignore_moving_enemy_collision_distance
- **Type:** [[double (type)]]
If there is a moving unit further than this we don't really care.

### enemy_with_different_destination_collision_penalty
- **Type:** [[double (type)]]
Enemy is not moving/or is too close and has different destination.

### general_entity_collision_penalty
- **Type:** [[double (type)]]
Simplification for now; collision with everything else is this.

### general_entity_subsequent_collision_penalty
- **Type:** [[double (type)]]
Collision penalty for successors of positions that require destroy to reach.

### extended_collision_penalty
- **Type:** [[double (type)]]
Collision penalty for collisions in the extended bounding box but outside the entity's actual bounding box.

### max_clients_to_accept_any_new_request
- **Type:** [[uint32 (type)]]
Up until this amount any client will be served by the path finder (no estimate on the path length).

### max_clients_to_accept_short_new_request
- **Type:** [[uint32 (type)]]
From max_clients_to_accept_any_new_request till this one only those that have a short estimate will be served.

### direct_distance_to_consider_short_request
- **Type:** [[uint32 (type)]]
This is the "threshold" to decide what is short and what is not.

### short_request_max_steps
- **Type:** [[uint32 (type)]]
If a short request takes more than this many steps, it will be rescheduled as a long request.

### short_request_ratio
- **Type:** [[double (type)]]
How many steps will be allocated to short requests each tick, as a ratio of all available steps per tick.

### min_steps_to_check_path_find_termination
- **Type:** [[uint32 (type)]]
Absolute minimum of steps that will be performed for every path find request no matter what.

### start_to_goal_cost_multiplier_to_terminate_path_find
- **Type:** [[double (type)]]
If the current actual cost from start is higher than this times estimate of start to goal then path finding is terminated.

### overload_levels
- **Type:** array<[[uint32 (type)]]>

### overload_multipliers
- **Type:** array<[[double (type)]]>

### negative_path_cache_delay_interval
- **Type:** [[uint32 (type)]]
