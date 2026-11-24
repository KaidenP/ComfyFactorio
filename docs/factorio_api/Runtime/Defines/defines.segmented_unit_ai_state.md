---
title: segmented_unit_ai_state
tags: [factorio-api, define]
---
# segmented_unit_ai_state

*Note: `defines.segmented_unit_ai_state`.*

## Values

### patrolling
The segmented unit is navigating its territory's patrol path. If the unit is not assigned to a territory, then it is patrolling around the position it was created.

### investigating
The segmented unit is investigating a location where it detected a disturbance.

### attacking
The segmented unit is attacking an entity that is trespassing on its territory, but the segmented unit is not using its full strength.

### enraged_at_target
The segmented unit is angry because it was attacked and is aggressively attacking an entity with its full strength.

### enraged_at_nothing
The segmented unit is angry because it was attacked but it does not have a valid attack target, so it is wandering around trying to find a valid attack target.
