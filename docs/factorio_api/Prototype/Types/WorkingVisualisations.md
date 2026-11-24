---
title: WorkingVisualisations
tags: [factorio-api, prototype, type]
---
# WorkingVisualisations

> **Abstract**

## Properties

### animation
- **Type:** [[Animation4Way]]
- **Optional**

### idle_animation
- **Type:** [[Animation4Way]]
- **Optional**
Idle animation must have the same frame count as animation.

### always_draw_idle_animation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only loaded if `idle_animation` is defined.

### default_recipe_tint
- **Type:** [[GlobalRecipeTints]]
- **Optional**

### recipe_not_set_tint
- **Type:** [[GlobalRecipeTints]]
- **Optional**

### states
- **Type:** array<[[VisualState]]>
- **Optional**
At least 2 visual states must be defined or no states at all. At most 32 states may be defined.

### working_visualisations
- **Type:** array<[[WorkingVisualisation]]>
- **Optional**
Used to display different animations when the machine is running, for example tinted based on the current recipe.

### shift_animation_waypoints
- **Type:** [[ShiftAnimationWaypoints]]
- **Optional**
Only loaded if one of `shift_animation_waypoint_stop_duration` or `shift_animation_transition_duration` is not 0.

### shift_animation_waypoint_stop_duration
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `shift_animation_waypoints` is defined.

### shift_animation_transition_duration
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `shift_animation_waypoints` is defined.

### status_colors
- **Type:** [[StatusColors]]
- **Optional**
Used by [[WorkingVisualisation#apply_tint|WorkingVisualisation::apply_tint]].
