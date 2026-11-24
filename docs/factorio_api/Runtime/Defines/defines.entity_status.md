---
title: entity_status
tags: [factorio-api, define]
---
# entity_status

*Note: `defines.entity_status`.*

## Values

### working

### normal

### ghost
Used by ghosts.

### broken
Only used if set through [[ContainerPrototype#default_status|ContainerPrototype::default_status]].

### no_power

### low_power

### no_fuel

### frozen

### disabled_by_control_behavior

### opened_by_circuit_network

### closed_by_circuit_network

### disabled_by_script

### marked_for_deconstruction

### paused
Used by space platform hubs.

### not_plugged_in_electric_network
Used by generators and solar panels.

### networks_connected
Used by power switches.

### networks_disconnected
Used by power switches.

### charging
Used by accumulators.

### discharging
Used by accumulators.

### fully_charged
Used by accumulators.

### out_of_logistic_network
Used by logistic containers.

### no_recipe
Used by assembling machines.

### no_ingredients
Used by furnaces.

### no_input_fluid
Used by boilers, fluid turrets, and fluid energy sources: Boiler has no fluid to work with.

### input_fluid_too_cold
Used by entities that consume fluids or have a fluid energy source.

### input_fluid_too_hot
Used by entities that consume fluids or have a fluid energy source.

### no_research_in_progress
Used by labs.

### no_minable_resources
Used by mining drills.

### hatches_blocked_by_elevated_rail
Used by cargo bays.

### not_connected_to_hub_or_pad
Used by cargo bays.

### too_far_from_pad_to_unload
Used by some cargo bays.

### low_input_fluid
Used by boilers and fluid turrets: Boiler still has some fluid but is about to run out.

### fluid_ingredient_shortage
Used by crafting machines.

### full_output
Used by crafting machines, boilers, burner energy sources, and reactors: Reactor/burner has full burnt result inventory, boiler has full output fluidbox.

### not_enough_space_in_output
Used by agricultural towers.

### full_burnt_result_output
Used by burner energy sources.

### item_ingredient_shortage
Used by crafting machines.

### missing_required_fluid
Used by mining drills when the mining fluid is missing.

### missing_science_packs
Used by labs.

### waiting_for_source_items
Used by inserters.

### waiting_for_more_items
Used by inserters when wait_for_full_hand is set.

### waiting_for_space_in_destination
Used by inserters, mining drills, and crafting machines using vector_to_place_result.

### preparing_rocket_for_launch
Used by the rocket silo.

### waiting_to_launch_rocket
Used by the rocket silo.

### waiting_for_space_in_platform_hub
Used by the rocket silo.

### launching_rocket
Used by the rocket silo.

### thrust_not_required
Used by thrusters.

### on_the_way
Used by space platform hubs.

### waiting_in_orbit
Used by space platform hubs.

### waiting_at_stop
Used by trains.

### waiting_for_upgrade
Used by trains.

### waiting_for_rockets_to_arrive
Used by space platform hubs.

### waiting_to_clear_drop_slots
Used by space platform hubs.

### not_enough_thrust
Used by space platform hubs.

### destination_stop_full
Used by trains.

### no_path
Used by trains and space platform hubs.

### no_modules_to_transmit
Used by beacons.

### recharging_after_power_outage
Used by roboports.

### waiting_for_target_to_be_built
Used by inserters targeting entity ghosts.

### waiting_for_train
Used by inserters targeting rails.

### no_ammo
Used by ammo turrets.

### low_temperature
Used by heat energy sources.

### disabled
Used by constant combinators: Combinator is turned off via switch in GUI. Also used by inserters.

### turned_off_during_daytime
Used by lamps.

### not_connected_to_rail
Used by rail signals.

### cant_divide_segments
Used by rail signals.

### no_filter
Used by filter inserters.

### no_spot_seedable_by_inputs
Used by agricultural towers.

### waiting_for_plants_to_grow
Used by agricultural towers.

### computing_navigation
Used by asteroid collectors.

### pipeline_overextended
Used by pipes, pipes to ground, and storage tanks.

### recipe_not_researched
Used by assembling machines.

### recipe_is_parameter
Used by assembling machines.

### armed
Used by land mines.
