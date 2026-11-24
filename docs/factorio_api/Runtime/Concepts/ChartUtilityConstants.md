---
title: ChartUtilityConstants
tags: [factorio-api, runtime, concept]
---
# ChartUtilityConstants

## Fields

### copper_wire_color
- **Type:** [[Color]]

### electric_power_pole_color
- **Type:** [[Color]]

### enabled_switch_color
- **Type:** [[Color]]

### disabled_switch_color
- **Type:** [[Color]]

### electric_line_width
- **Type:** [[float]]

### electric_line_minimum_absolute_width
- **Type:** [[float]]

### red_wire_color
- **Type:** [[Color]]

### green_wire_color
- **Type:** [[Color]]

### circuit_network_member_color
- **Type:** [[Color]]

### turret_range_color
- **Type:** [[Color]]

### artillery_range_color
- **Type:** [[Color]]

### default_friendly_color
- **Type:** [[Color]]

### default_enemy_color
- **Type:** [[Color]]

### default_enemy_territory_color
- **Type:** [[Color]]

### rail_color
- **Type:** [[Color]]

### elevated_rail_color
- **Type:** [[Color]]

### rail_ramp_color
- **Type:** [[Color]]

### entity_ghost_color
- **Type:** [[Color]]

### tile_ghost_color
- **Type:** [[Color]]

### vehicle_outer_color
- **Type:** [[Color]]

### vehicle_outer_color_selected
- **Type:** [[Color]]

### vehicle_inner_color
- **Type:** [[Color]]

### vehicle_wagon_connection_color
- **Type:** [[Color]]

### resource_outline_selection_color
- **Type:** [[Color]]

### chart_train_stop_text_color
- **Type:** [[Color]]

### chart_train_stop_disabled_text_color
- **Type:** [[Color]]

### chart_train_stop_full_text_color
- **Type:** [[Color]]

### red_signal_color
- **Type:** [[Color]]

### green_signal_color
- **Type:** [[Color]]

### blue_signal_color
- **Type:** [[Color]]

### yellow_signal_color
- **Type:** [[Color]]

### chart_deconstruct_tint
- **Type:** [[Color]]

### chart_deconstruct_active_color
- **Type:** [[Color]]

### default_friendly_color_by_type
- **Type:** dictionary<[[string]] → [[Color]]>
- **Optional**
The strings are entity types.

### default_color_by_type
- **Type:** dictionary<[[string]] → [[Color]]>
- **Optional**
The strings are entity types.

### explosion_visualization_duration
- **Type:** [[MapTick]]

### train_path_color
- **Type:** [[Color]]

### train_preview_path_outline_color
- **Type:** [[Color]]

### train_current_path_outline_color
- **Type:** [[Color]]

### chart_logistic_robot_color
- **Type:** [[Color]]

### chart_construction_robot_color
- **Type:** [[Color]]

### chart_mobile_construction_robot_color
- **Type:** [[Color]]

### chart_personal_construction_robot_color
- **Type:** [[Color]]

### chart_delivery_to_me_logistic_robot_color
- **Type:** [[Color]]

### zoom_threshold_to_draw_spider_path
- **Type:** [[double]]

### chart_player_circle_size
- **Type:** [[float]]

### custom_tag_scale
- **Type:** [[float]]
- **Optional**
Defaults to `1.0`.

### custom_tag_max_scale
- **Type:** [[float]]
- **Optional**
Defaults to `1.0`.

### custom_tag_selected_overlay_tint
- **Type:** [[Color]]
- **Optional**

### recipe_icon_scale
- **Type:** [[float]]
Must be larger than 0. This number is multiplied by the crafting machine's [[LuaEntityPrototype#radius|radius]] to get the final recipe icon scale for the chart.
