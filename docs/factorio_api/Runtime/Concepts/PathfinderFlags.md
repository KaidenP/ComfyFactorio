---
title: PathfinderFlags
tags: [factorio-api, runtime, concept]
---
# PathfinderFlags

## Fields

### allow_destroy_friendly_entities
- **Type:** [[boolean]]
- **Optional**
Allows pathing through friendly entities. Defaults to `false`.

### allow_paths_through_own_entities
- **Type:** [[boolean]]
- **Optional**
Allows the pathfinder to path through entities of the same force. Defaults to `false`.

### cache
- **Type:** [[boolean]]
- **Optional**
Enables path caching. This can be more efficient, but might fail to respond to changes in the environment. Defaults to `true`.

### prefer_straight_paths
- **Type:** [[boolean]]
- **Optional**
Makes the pathfinder try to path in straight lines. Defaults to `false`.

### low_priority
- **Type:** [[boolean]]
- **Optional**
Sets lower priority on the path request, meaning it might take longer to find a path at the expense of speeding up others. Defaults to `false`.

### no_break
- **Type:** [[boolean]]
- **Optional**
Makes the pathfinder not break in the middle of processing this pathfind, no matter how much work is needed. Defaults to `false`.
