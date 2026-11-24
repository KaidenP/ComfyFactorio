---
title: UtilityConstants
tags: [factorio-api, prototype]
---
# UtilityConstants

*Note: `UtilityConstants (prototype)`.*

> **Parent:** [[PrototypeBase]] · **Type name:** `utility-constants` · **Instance limit:** 1

Constants used by the game that are not specific to certain prototypes. See [utility-constants.lua](https://github.com/wube/factorio-data/blob/master/core/prototypes/utility-constants.lua) for the values used by the base game.

## Properties

### chart
- **Type:** [[ChartUtilityConstants (type)]]
Chart means map and minimap.

### bonus_gui_ordering
- **Type:** [[BonusUtilityConstants (type)]]
The base game uses more entries here that are applied via the `ammo-category.lua` file.

### map_editor
- **Type:** [[EditorUtilityConstants (type)]]

### entity_button_background_color
- **Type:** [[Color (type)]]

### build_preview_tints
- **Type:** [[BuildPreviewTints (type)]]

### building_no_tint
- **Type:** [[Color (type)]]

### tall_entity_tint
- **Type:** [[Color (type)]]
Tall entities will be tinted with this value when "Hide tall entities" mode is active.

### tall_entity_smoke_tint
- **Type:** [[Color (type)]]
All trivial smoke will be tinted with this value when "Hide tall entities" mode is active.

### underground_belt_max_distance_tint
- **Type:** [[Color (type)]]

### underground_pipe_max_distance_tint
- **Type:** [[Color (type)]]

### ghost_shader_tint
- **Type:** [[GhostTintSet (type)]]

### ghost_shaderless_tint
- **Type:** [[GhostTintSet (type)]]

### ghost_shimmer_settings
- **Type:** [[GhostShimmerConfig (type)]]

### probability_product_count_tint
- **Type:** [[Color (type)]]

### ghost_product_count_tint
- **Type:** [[Color (type)]]

### zero_count_value_tint
- **Type:** [[Color (type)]]

### equipment_default_background_color
- **Type:** [[Color (type)]]

### equipment_default_background_border_color
- **Type:** [[Color (type)]]

### equipment_default_grabbed_background_color
- **Type:** [[Color (type)]]

### equipment_disabled_background_tint
- **Type:** [[Color (type)]]

### equipment_disabled_tint
- **Type:** [[Color (type)]]

### turret_range_visualization_color
- **Type:** [[Color (type)]]

### capsule_range_visualization_color
- **Type:** [[Color (type)]]

### agricultural_range_visualization_color
- **Type:** [[Color (type)]]

### artillery_range_visualization_color
- **Type:** [[Color (type)]]

### gui_remark_color
- **Type:** [[Color (type)]]

### gui_search_match_foreground_color
- **Type:** [[Color (type)]]

### gui_search_match_background_color
- **Type:** [[Color (type)]]

### default_player_force_color
- **Type:** [[Color (type)]]

### default_enemy_force_color
- **Type:** [[Color (type)]]

### default_other_force_color
- **Type:** [[Color (type)]]

### deconstruct_mark_tint
- **Type:** [[Color (type)]]

### rail_planner_count_button_color
- **Type:** [[Color (type)]]

### count_button_size
- **Type:** [[int32 (type)]]

### logistic_gui_unselected_network_highlight_tint
- **Type:** [[Color (type)]]

### logistic_gui_selected_network_highlight_tint
- **Type:** [[Color (type)]]

### chart_search_highlight
- **Type:** [[Color (type)]]

### selected_chart_search_highlight
- **Type:** [[Color (type)]]

### max_logistic_filter_count
- **Type:** [[LogisticFilterIndex (type)]]

### select_group_row_count
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### select_slot_row_count
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### logistic_slots_per_row
- **Type:** [[uint8 (type)]]
Will be clamped to the range [2, 100].

### crafting_queue_slots_per_row
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### blueprint_big_slots_per_row
- **Type:** [[uint8 (type)]]
Will be clamped to the range [2, 100].

### blueprint_small_slots_per_row
- **Type:** [[uint8 (type)]]
Will be clamped to the range [2, 100].

### inventory_width
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### module_inventory_width
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### trash_inventory_width
- **Type:** [[uint8 (type)]]
Will be clamped to the range [1, 100].

### max_terrain_building_size
- **Type:** [[uint8 (type)]]

### small_area_size
- **Type:** [[float (type)]]

### medium_area_size
- **Type:** [[float (type)]]

### large_area_size
- **Type:** [[float (type)]]

### huge_area_size
- **Type:** [[float (type)]]

### huge_platform_animation_sound_area
- **Type:** [[float (type)]]

### small_blueprint_area_size
- **Type:** [[float (type)]]

### medium_blueprint_area_size
- **Type:** [[float (type)]]

### large_blueprint_area_size
- **Type:** [[float (type)]]

### enabled_recipe_slot_tint
- **Type:** [[Color (type)]]

### disabled_recipe_slot_tint
- **Type:** [[Color (type)]]

### disabled_recipe_slot_background_tint
- **Type:** [[Color (type)]]

### forced_enabled_recipe_slot_background_tint
- **Type:** [[Color (type)]]

### rail_segment_colors
- **Type:** array<[[Color (type)]]>

### player_colors
- **Type:** array<[[PlayerColorData (type)]]>
The table with `name = "default"` must exist and be the first member of the array.

### server_command_console_chat_color
- **Type:** [[Color (type)]]

### script_command_console_chat_color
- **Type:** [[Color (type)]]

### default_alert_icon_scale
- **Type:** [[float (type)]]

### default_alert_icon_shift_by_type
- **Type:** dictionary<[[string (type)]] → [[Vector (type)]]>
- **Optional**

### default_alert_icon_scale_by_type
- **Type:** dictionary<[[string (type)]] → [[float (type)]]>
- **Optional**

### merge_bonus_gui_production_bonuses
- **Type:** [[boolean (type)]]
- **Optional**
If not set, defaults to `true` when modded and `false` when vanilla.

### daytime_color_lookup
- **Type:** [[DaytimeColorLookupTable (type)]]

### frozen_color_lookup
- **Type:** [[ColorLookupTable (type)]]

### default_platform_surface_render_parameters
- **Type:** [[SurfaceRenderParameters (type)]]

### drop_item_radius
- **Type:** [[double (type)]]

### checkerboard_white
- **Type:** [[Color (type)]]

### checkerboard_black
- **Type:** [[Color (type)]]

### item_outline_color
- **Type:** [[Color (type)]]

### item_outline_radius
- **Type:** [[float (type)]]

### item_outline_inset
- **Type:** [[float (type)]]

### item_outline_sharpness
- **Type:** [[float (type)]]

### item_default_random_tint_strength
- **Type:** [[Color (type)]]

### spawner_evolution_factor_health_modifier
- **Type:** [[float (type)]]

### item_health_bar_colors
- **Type:** array<[[ItemHealthColorData (type)]]>
There must be one array item with a threshold of `0`.

### item_ammo_magazine_left_bar_color
- **Type:** [[Color (type)]]

### item_tool_durability_bar_color
- **Type:** [[Color (type)]]

### filter_outline_color
- **Type:** [[Color (type)]]

### icon_shadow_radius
- **Type:** [[float (type)]]

### icon_shadow_inset
- **Type:** [[float (type)]]

### icon_shadow_sharpness
- **Type:** [[float (type)]]

### icon_shadow_color
- **Type:** [[Color (type)]]

### clipboard_history_size
- **Type:** [[uint32 (type)]]

### recipe_step_limit
- **Type:** [[uint32 (type)]]

### manual_rail_building_reach_modifier
- **Type:** [[double (type)]]

### train_temporary_stop_wait_time
- **Type:** [[uint32 (type)]]

### train_time_wait_condition_default
- **Type:** [[uint32 (type)]]

### train_inactivity_wait_condition_default
- **Type:** [[uint32 (type)]]

### default_trigger_target_mask_by_type
- **Type:** dictionary<[[string (type)]] → [[TriggerTargetMask (type)]]>
- **Optional**
The strings are entity types.

### unit_group_pathfind_resolution
- **Type:** [[int8 (type)]]

### unit_group_max_pursue_distance
- **Type:** [[double (type)]]

### dynamic_recipe_overload_factor
- **Type:** [[double (type)]]

### minimum_recipe_overload_multiplier
- **Type:** [[uint32 (type)]]

### maximum_recipe_overload_multiplier
- **Type:** [[uint32 (type)]]

### entity_renderer_search_box_limits
- **Type:** [[EntityRendererSearchBoxLimits (type)]]

### light_renderer_search_distance_limit
- **Type:** [[uint8 (type)]]
Can be set to anything from range 0 to 255, but larger values will be clamped to 160. Setting it to larger values can have performance impact (growing geometrically).

### far_away_chunk_generation_radius
- **Type:** [[uint8 (type)]]

### tree_leaf_distortion_strength_far
- **Type:** [[Vector (type)]]

### tree_leaf_distortion_distortion_far
- **Type:** [[Vector (type)]]

### tree_leaf_distortion_speed_far
- **Type:** [[Vector (type)]]

### tree_leaf_distortion_strength_near
- **Type:** [[Vector (type)]]

### tree_leaf_distortion_distortion_near
- **Type:** [[Vector (type)]]

### tree_leaf_distortion_speed_near
- **Type:** [[Vector (type)]]

### tree_shadow_roughness
- **Type:** [[float (type)]]

### tree_shadow_speed
- **Type:** [[float (type)]]

### missing_preview_sprite_location
- **Type:** [[FileName]]

### main_menu_background_image_location
- **Type:** [[FileName]]

### main_menu_simulations
- **Type:** dictionary<[[string (type)]] → [[SimulationDefinition (type)]]>
- **Optional**
The strings represent the names of the simulations.

### main_menu_background_vignette_intensity
- **Type:** [[float (type)]]

### main_menu_background_vignette_sharpness
- **Type:** [[float (type)]]

### feedback_screenshot_subfolder_name
- **Type:** [[string (type)]]

### feedback_screenshot_file_name
- **Type:** [[string (type)]]

### default_scorch_mark_color
- **Type:** [[Color (type)]]

### color_filters
- **Type:** array<[[ColorFilterData (type)]]>
- **Optional**

### clear_cursor_volume_modifier
- **Type:** [[float (type)]]

### weapons_in_simulation_volume_modifier
- **Type:** [[float (type)]]

### explosions_in_simulation_volume_modifier
- **Type:** [[float (type)]]

### enemies_in_simulation_volume_modifier
- **Type:** [[float (type)]]

### low_energy_robot_estimate_multiplier
- **Type:** [[double (type)]]

### asteroid_spawning_offset
- **Type:** [[SimpleBoundingBox (type)]]

### asteroid_fading_range
- **Type:** [[float (type)]]

### asteroid_min_damage_modifier
- **Type:** [[float (type)]]
Asteroid damage will be multiplied by this value when space platform speed is zero and will linearly increase until asteroid_spawning_with_random_orientation_max_speed is reached.

### asteroid_spawning_with_random_orientation_max_speed
- **Type:** [[double (type)]]
In km per tick.

### asteroid_position_offset_to_speed_coefficient
- **Type:** [[double (type)]]

### asteroid_collector_navmesh_refresh_tick_interval
- **Type:** [[uint32 (type)]]

### asteroid_collector_blockage_update_tile_distance
- **Type:** [[uint32 (type)]]

### asteroid_collector_max_nurbs_control_point_separation
- **Type:** [[double (type)]]

### asteroid_collector_static_head_swing_strength_scale
- **Type:** [[float (type)]]

### asteroid_collector_static_head_swing_segment_count
- **Type:** [[uint32 (type)]]

### space_platform_acceleration_expression
- **Type:** [[MathExpression (type)]]
Variables: `speed, thrust, weight, width, height`

### space_platform_relative_speed_factor
- **Type:** [[double (type)]]

### space_platform_starfield_movement_vector
- **Type:** [[Vector (type)]]

### space_platform_max_size
- **Type:** [[SimpleBoundingBox (type)]]

### space_platform_dump_cooldown
- **Type:** [[uint32 (type)]]
Determines how fast space platforms will send items in drop slots to the surface. Each item type has its own cooldown.

### space_platform_manual_dump_cooldown
- **Type:** [[uint32 (type)]]
Delay after manual transfer until space platform sends items in drop slots to the surface. Overrides remaining space_platform_dump_cooldown in this instance.

### space_platform_max_relative_speed_deviation_for_asteroid_chunks_update
- **Type:** [[float (type)]]
Space platform remembers relative speed range which asteroids use while it moves. When the range is larger than the specified deviation, the platform will start updating cached trajectories of all asteroid chunks over multiple ticks.

### space_platform_asteroid_chunk_trajectory_updates_per_tick
- **Type:** [[uint32 (type)]]
How many asteroid chunks should be processed per tick, see [[UtilityConstants (prototype)#space_platform_max_relative_speed_deviation_for_asteroid_chunks_update|space_platform_max_relative_speed_deviation_for_asteroid_chunks_update]].

### default_item_weight
- **Type:** [[Weight (type)]]

### default_rocket_lift_weight
- **Type:** [[Weight (type)]]
Used for "Rocket capacity" item tooltip and for comparing rocket silo lift weight in GUI to this value.

### factoriopedia_recycling_recipe_categories
- **Type:** array<[[RecipeCategoryID (type)]]>

### default_pipeline_extent
- **Type:** [[double (type)]]
The default value of [[FluidBox#max_pipeline_extent|FluidBox::max_pipeline_extent]].

### default_platform_procession_set
- **Type:** [[ProcessionSet (type)]]
Must contain arrival and departure with [[ProcessionPrototype#procession_style|procession_style]] containing 0.

### default_planet_procession_set
- **Type:** [[ProcessionSet (type)]]
Must contain arrival and departure with [[ProcessionPrototype#procession_style|procession_style]] containing 0.

### landing_area_clear_zone_radius
- **Type:** [[float (type)]]
Radius of area where cargo pods won't land.

### landing_area_max_radius
- **Type:** [[float (type)]]
Max radius where cargo pods will land.

### lightning_attractor_collection_range_color
- **Type:** [[Color (type)]]

### lightning_attractor_protection_range_color
- **Type:** [[Color (type)]]

### landing_squash_immunity
- **Type:** [[MapTick (type)]]

### ejected_item_lifetime
- **Type:** [[MapTick (type)]]
Silently clamped to be between 1 tick and 5 minutes (`5 * 60 * 60` ticks).

### ejected_item_speed
- **Type:** [[double (type)]]
Silently clamped to be between 0 and 1/60.

### ejected_item_direction_variation
- **Type:** [[double (type)]]
Silently clamped to be between 0 and 0.99.

### ejected_item_friction
- **Type:** [[double (type)]]
Silently clamped to be between 0 and 1.

### train_visualization
- **Type:** [[TrainVisualizationConstants (type)]]

### default_collision_masks
- **Type:** dictionary<[[string (type)]] → [[CollisionMaskConnector]]>
The strings can be entity types or custom strings.

### show_chunk_components_collision_mask
- **Type:** [[CollisionMaskConnector]]

### building_collision_mask
- **Type:** [[CollisionMaskConnector]]

### water_collision_mask
- **Type:** [[TileCollisionMaskConnector]]

### ghost_layer
- **Type:** [[CollisionLayerID (type)]]

### train_pushed_by_player_max_speed
- **Type:** [[double (type)]]

### train_pushed_by_player_max_acceleration
- **Type:** [[double (type)]]

### train_pushed_by_player_ignores_friction
- **Type:** [[boolean (type)]]

### tooltip_monitor_edge_border
- **Type:** [[int32 (type)]]
Must be >= 1.

### flying_text_ttl
- **Type:** [[int32 (type)]]
Must be >= 1.

### train_path_finding
- **Type:** [[TrainPathFinderConstants (type)]]

### freezing_temperature
- **Type:** [[double (type)]]
Will be clamped to a positive number, starting at 0.

### train_on_elevated_rail_shadow_shift_multiplier
- **Type:** [[Vector (type)]]

### max_belt_stack_size
- **Type:** [[uint8 (type)]]
Must be >= 1.

### inserter_hand_stack_items_per_sprite
- **Type:** [[ItemCountType (type)]]
Must be >= 1.

### inserter_hand_stack_max_sprites
- **Type:** [[ItemCountType (type)]]
Must be >= 1.

### remote_view_LPF_min_cutoff_frequency
- **Type:** [[float (type)]]

### remote_view_LPF_max_cutoff_frequency
- **Type:** [[float (type)]]

### space_LPF_min_cutoff_frequency
- **Type:** [[float (type)]]

### space_LPF_max_cutoff_frequency
- **Type:** [[float (type)]]

### walking_sound_count_reduction_rate
- **Type:** [[float (type)]]
Silently clamped to be between 0 and 1.

### moving_sound_count_reduction_rate
- **Type:** [[float (type)]]
Silently clamped to be between 0 and 1.

### environment_sounds_transition_fade_in_ticks
- **Type:** [[uint32 (type)]]

### sound_fade_ticks
- **Type:** [[uint32 (type)]]

### starmap_orbit_default_color
- **Type:** [[Color (type)]]

### starmap_orbit_hovered_color
- **Type:** [[Color (type)]]

### starmap_orbit_clicked_color
- **Type:** [[Color (type)]]

### starmap_orbit_disabled_color
- **Type:** [[Color (type)]]

### time_to_show_full_health_bar
- **Type:** [[MapTick (type)]]
The number of ticks to show a segmented unit's health bar after fully regenerating.

### capture_water_mask_at_layer
- **Type:** [[uint8 (type)]]
Layer within `ground-natural` [[TileRenderLayer|tile render layer]] group, before which terrain lightmap alpha channel is copied into water mask. Decals, which need to be masked by water should have their [[DecorativePrototype#tile_layer|DecorativePrototype::tile_layer]] set to only slightly larger value than `capture_water_mask_at_layer`, to avoid risk of undefined behavior caused by rendering tiles into layers between `capture_water_mask_at_layer` and decal's `tile_layer`.

### logistic_robots_use_busy_robots_queue
- **Type:** [[boolean (type)]]

### construction_robots_use_busy_robots_queue
- **Type:** [[boolean (type)]]

### quality_selector_dropdown_threshold
- **Type:** [[uint8 (type)]]

### maximum_quality_jump
- **Type:** [[uint8 (type)]]
Cap for how many steps of quality the output of something (miner/crafter) may be higher than the input (resource/ingredients). Must be >= 1.
