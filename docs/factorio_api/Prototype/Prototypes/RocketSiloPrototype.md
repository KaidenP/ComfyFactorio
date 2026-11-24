---
title: RocketSiloPrototype
tags: [factorio-api, prototype]
---
# RocketSiloPrototype

> **Parent:** [[AssemblingMachinePrototype]] · **Type name:** `rocket-silo`

A [rocket silo](https://wiki.factorio.com/Rocket_silo).

## Properties

### active_energy_usage
- **Type:** [[Energy]]
Additional energy used during the following parts of the [[defines.rocket_silo_status|launch sequence]]: doors_opening, rocket_rising, arms_advance, engine_starting, arms_retract, doors_closing.

### lamp_energy_usage
- **Type:** [[Energy]]
May be 0.

Additional energy used during the night, that is when [[LuaSurface#darkness|LuaSurface::darkness]] is larger than 0.3.

### rocket_entity
- **Type:** [[EntityID (type)]]
Name of a [[RocketSiloRocketPrototype]].

### arm_02_right_animation
- **Type:** [[Animation]]
- **Optional**

### arm_01_back_animation
- **Type:** [[Animation]]
- **Optional**

### arm_03_front_animation
- **Type:** [[Animation]]
- **Optional**

### shadow_sprite
- **Type:** [[Sprite]]
- **Optional**

### hole_sprite
- **Type:** [[Sprite]]
- **Optional**

### hole_light_sprite
- **Type:** [[Sprite]]
- **Optional**

### rocket_shadow_overlay_sprite
- **Type:** [[Sprite]]
- **Optional**

### rocket_glow_overlay_sprite
- **Type:** [[Sprite]]
- **Optional**

### door_back_sprite
- **Type:** [[Sprite]]
- **Optional**

### door_front_sprite
- **Type:** [[Sprite]]
- **Optional**

### base_day_sprite
- **Type:** [[Sprite]]
- **Optional**

### base_front_sprite
- **Type:** [[Sprite]]
- **Optional**

### red_lights_back_sprites
- **Type:** [[Sprite]]
- **Optional**
Drawn from the start of the [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] state until the end of the [[defines.rocket_silo_status#lights_blinking_close|lights_blinking_close]] state.

### red_lights_front_sprites
- **Type:** [[Sprite]]
- **Optional**
Drawn from the start of the [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] state until the end of the [[defines.rocket_silo_status#lights_blinking_close|lights_blinking_close]] state.

### base_frozen
- **Type:** [[Sprite]]
- **Optional**

### base_front_frozen
- **Type:** [[Sprite]]
- **Optional**

### hole_frozen
- **Type:** [[Sprite]]
- **Optional**

### door_back_frozen
- **Type:** [[Sprite]]
- **Optional**

### door_front_frozen
- **Type:** [[Sprite]]
- **Optional**

### hole_clipping_box
- **Type:** [[BoundingBox (type)]]

### door_back_open_offset
- **Type:** [[Vector (type)]]

### door_front_open_offset
- **Type:** [[Vector (type)]]

### silo_fade_out_start_distance
- **Type:** [[double (type)]]

### silo_fade_out_end_distance
- **Type:** [[double (type)]]

### times_to_blink
- **Type:** [[uint8 (type)]]
How many times the `red_lights_back_sprites` and `red_lights_front_sprites` should blink during [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] and [[defines.rocket_silo_status#lights_blinking_close|lights_blinking_close]].

Does not affect the duration of the launch sequence.

### light_blinking_speed
- **Type:** [[double (type)]]
The inverse of the duration in ticks of [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] and [[defines.rocket_silo_status#lights_blinking_close|lights_blinking_close]].
**Examples:**

```
light_blinking_speed = 1 / (2 * 60) -- lights blinking takes 120 ticks
```

### door_opening_speed
- **Type:** [[double (type)]]
The inverse of the duration in ticks of [[defines.rocket_silo_status#doors_opening|doors_opening]] and [[defines.rocket_silo_status#doors_closing|closing]].
**Examples:**

```
door_opening_speed = 1 / (4 * 60) -- doors opening and closing takes 4 seconds
```

### rocket_parts_required
- **Type:** [[uint32 (type)]]
The number of crafts that must complete to produce a rocket. This includes bonus crafts from productivity. Recipe products are ignored.

### rocket_quick_relaunch_start_offset
- **Type:** [[double (type)]]

### rocket_rising_speed_modifier_per_quality_level
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Must be >= 0.

### rocket_engine_starting_speed_modifier_per_quality_level
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Must be >= 0.

### arms_speed_modifier_per_quality_level
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Must be >= 0.

### satellite_animation
- **Type:** [[Animation]]
- **Optional**

### satellite_shadow_animation
- **Type:** [[Animation]]
- **Optional**

### base_night_sprite
- **Type:** [[Sprite]]
- **Optional**
Drawn instead of `base_day_sprite` during the night, that is when [[LuaSurface#darkness|LuaSurface::darkness]] is larger than 0.3.

### base_light
- **Type:** [[LightDefinition]]
- **Optional**

### base_engine_light
- **Type:** [[LightDefinition]]
- **Optional**

### rocket_rising_delay
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `30`
The time to wait in the [[defines.rocket_silo_status#doors_opened|doors_opened]] state before switching to [[defines.rocket_silo_status#rocket_rising|rocket_rising]].

### launch_wait_time
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `120`
The time to wait in the [[defines.rocket_silo_status#launch_started|launch_started]] state before switching to [[defines.rocket_silo_status#engine_starting|engine_starting]].

### render_not_in_network_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the "no network" icon should be rendered on this entity if the entity is not within a logistics network.

![[too-far-from-roboport-icon.png]]

### rocket_parts_storage_cap
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `rocket_parts_required`
All values down to 0 are allowed, however it is suggested to avoid values from 1 up to `rocket_parts_required - 1` to avoid second progress bar stopping before reaching 100%. When set to 0, second progress bar is hidden.

### alarm_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Applied when switching into the [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] state.

### clamps_on_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Applied when switching into the [[defines.rocket_silo_status#arms_advance|arms_advance]] state.

### clamps_off_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Applied when switching into the [[defines.rocket_silo_status#arms_retract|arms_retract]] state.

### doors_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Applied when switching into the [[defines.rocket_silo_status#doors_opening|doors_opening]] and [[defines.rocket_silo_status#doors_closing|doors_closing]] states.

### raise_rocket_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Applied when switching into the [[defines.rocket_silo_status#rocket_rising|rocket_rising]] state.

### alarm_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching into the [[defines.rocket_silo_status#lights_blinking_open|lights_blinking_open]] state.

### quick_alarm_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching from [[defines.rocket_silo_status#rocket_flying|rocket_flying]] into the [[defines.rocket_silo_status#doors_opened|doors_opened]] state when a quick follow-up rocket is ready.

### clamps_on_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching into the [[defines.rocket_silo_status#arms_advance|arms_advance]] state.

### clamps_off_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching into the [[defines.rocket_silo_status#arms_retract|arms_retract]] state.

### doors_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching into the [[defines.rocket_silo_status#doors_opening|doors_opening]] and [[defines.rocket_silo_status#doors_closing|doors_closing]] states.

### raise_rocket_sound
- **Type:** [[Sound]]
- **Optional**
Played when switching into the [[defines.rocket_silo_status#rocket_rising|rocket_rising]] state.

### to_be_inserted_to_rocket_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`
When `launch_to_space_platforms` is true, the inventory has dynamic size and is weight-restricted, so this value is ignored.

### logistic_trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

### lift_weight
- **Type:** [[Weight (type)]]
- **Optional**
- **Default:** `1000000`
When `launch_to_space_platforms` is false, the inventory has no weight restrictions, so this value is ignored.

### cargo_station_parameters
- **Type:** [[CargoStationParameters (type)]]
Must have exactly one entry in [[CargoStationParameters (type)#hatch_definitions|CargoStationParameters::hatch_definitions]].

### launch_to_space_platforms
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Requires:** `space_age`
Enables 'Space Age' functionality for this rocket silo, allowing it to supply space platforms.

### can_launch_without_landing_pads
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### default_launched_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### robot_door
- **Type:** [[RobotDoorSpecification]]
- **Optional**
