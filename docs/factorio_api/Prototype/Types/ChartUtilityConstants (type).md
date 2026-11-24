---
title: ChartUtilityConstants
tags: [factorio-api, prototype, type]
---
# ChartUtilityConstants

*Note: `ChartUtilityConstants (type)`.*

## Properties

### copper_wire_color
- **Type:** [[Color (type)]]

### electric_power_pole_color
- **Type:** [[Color (type)]]

### enabled_switch_color
- **Type:** [[Color (type)]]

### disabled_switch_color
- **Type:** [[Color (type)]]

### electric_line_width
- **Type:** [[float (type)]]

### electric_line_minimum_absolute_width
- **Type:** [[float (type)]]

### red_wire_color
- **Type:** [[Color (type)]]

### green_wire_color
- **Type:** [[Color (type)]]

### circuit_network_member_color
- **Type:** [[Color (type)]]

### turret_range_color
- **Type:** [[Color (type)]]

### artillery_range_color
- **Type:** [[Color (type)]]

### default_friendly_color
- **Type:** [[Color (type)]]

### default_enemy_color
- **Type:** [[Color (type)]]

### default_enemy_territory_color
- **Type:** [[Color (type)]]

### rail_color
- **Type:** [[Color (type)]]

### elevated_rail_color
- **Type:** [[Color (type)]]

### rail_ramp_color
- **Type:** [[Color (type)]]

### entity_ghost_color
- **Type:** [[Color (type)]]

### tile_ghost_color
- **Type:** [[Color (type)]]

### vehicle_outer_color
- **Type:** [[Color (type)]]

### vehicle_outer_color_selected
- **Type:** [[Color (type)]]

### vehicle_inner_color
- **Type:** [[Color (type)]]

### vehicle_wagon_connection_color
- **Type:** [[Color (type)]]

### resource_outline_selection_color
- **Type:** [[Color (type)]]

### chart_train_stop_text_color
- **Type:** [[Color (type)]]

### chart_train_stop_disabled_text_color
- **Type:** [[Color (type)]]

### chart_train_stop_full_text_color
- **Type:** [[Color (type)]]

### red_signal_color
- **Type:** [[Color (type)]]

### green_signal_color
- **Type:** [[Color (type)]]

### blue_signal_color
- **Type:** [[Color (type)]]

### yellow_signal_color
- **Type:** [[Color (type)]]

### chart_deconstruct_tint
- **Type:** [[Color (type)]]

### chart_deconstruct_active_color
- **Type:** [[Color (type)]]

### default_friendly_color_by_type
- **Type:** dictionary<[[string (type)]] → [[Color (type)]]>
- **Optional**
The strings are entity types.

### default_color_by_type
- **Type:** dictionary<[[string (type)]] → [[Color (type)]]>
- **Optional**
The strings are entity types.

### explosion_visualization_duration
- **Type:** [[MapTick (type)]]

### train_path_color
- **Type:** [[Color (type)]]

### train_preview_path_outline_color
- **Type:** [[Color (type)]]

### train_current_path_outline_color
- **Type:** [[Color (type)]]

### chart_logistic_robot_color
- **Type:** [[Color (type)]]

### chart_construction_robot_color
- **Type:** [[Color (type)]]

### chart_mobile_construction_robot_color
- **Type:** [[Color (type)]]

### chart_personal_construction_robot_color
- **Type:** [[Color (type)]]

### chart_delivery_to_me_logistic_robot_color
- **Type:** [[Color (type)]]

### zoom_threshold_to_draw_spider_path
- **Type:** [[double (type)]]

### chart_player_circle_size
- **Type:** [[float (type)]]

### custom_tag_scale
- **Type:** [[float (type)]]
- **Optional**
Defaults to `1.0`.

### custom_tag_max_scale
- **Type:** [[float (type)]]
- **Optional**
Defaults to `1.0`.

### custom_tag_selected_overlay_tint
- **Type:** [[Color (type)]]
- **Optional**

### recipe_icon_scale
- **Type:** [[float (type)]]
Must be larger than 0. This number is multiplied by the crafting machine's [[LuaEntityPrototype#radius|radius]] to get the final recipe icon scale for the chart.
