---
title: FluidStreamPrototype
tags: [factorio-api, prototype]
---
# FluidStreamPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `stream`

Used for example for the handheld flamethrower.

## Properties

### particle_spawn_interval
- **Type:** [[uint16 (type)]]
The stream will spawn one particle every `particle_spawn_interval` ticks until the `particle_spawn_timeout` is reached. The first particle will trigger an `initial_action` upon landing. Each particle triggers an `action` upon landing. Particles spawned within a single `particle_spawn_timeout` interval will be connected by a stretched `spine_animation`.

### particle_horizontal_speed
- **Type:** [[float (type)]]
Must be larger than 0. `particle_horizontal_speed` has to be greater than `particle_horizontal_speed_deviation`.

### particle_horizontal_speed_deviation
- **Type:** [[float (type)]]

### particle_vertical_acceleration
- **Type:** [[float (type)]]

### initial_action
- **Type:** [[Trigger]]
- **Optional**
Action that is triggered when the first particle lands.

### action
- **Type:** [[Trigger]]
- **Optional**
Action that is triggered every time a particle lands. Not triggered for the first particle if `initial_action` is non-empty.

### special_neutral_target_damage
- **Type:** [[DamageParameters (type)]]
- **Optional**

### width
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### particle_buffer_size
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `20`
Number of spawned child particles of the stream. Must be greater than 0 and less than 256.

### particle_spawn_timeout
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** 4 * `particle_spawn_interval`

### particle_start_alpha
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_end_alpha
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_start_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_alpha_per_part
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_scale_per_part
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### particle_fade_out_threshold
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Value between 0 and 1.

### particle_loop_exit_threshold
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Value between 0 and 1.

### particle_loop_frame_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `1`
Will be set to 1 by the game if less than 1.

### particle_fade_out_duration
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `65535`
Will be set to 1 by the game if less than 1.

### spine_animation
- **Type:** [[Animation]]
- **Optional**

### particle
- **Type:** [[Animation]]
- **Optional**

### shadow
- **Type:** [[Animation]]
- **Optional**

### smoke_sources
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**
Smoke spawning is controlled by `progress_to_create_smoke`.

### progress_to_create_smoke
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
The point in the particles projectile arc to start spawning smoke. 0.5 (the default) starts spawning smoke at the halfway point between the source and target.

### stream_light
- **Type:** [[LightDefinition]]
- **Optional**

### ground_light
- **Type:** [[LightDefinition]]
- **Optional**

### target_position_deviation
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### oriented_particle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### shadow_scale_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### target_initial_position_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
