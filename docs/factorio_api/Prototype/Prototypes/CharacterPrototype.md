---
title: CharacterPrototype
tags: [factorio-api, prototype]
---
# CharacterPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `character`

Entity that you move around on the screen during the campaign and freeplay.

## Properties

### crafting_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### mining_speed
- **Type:** [[double (type)]]

### running_speed
- **Type:** [[double (type)]]

### distance_per_frame
- **Type:** [[double (type)]]

### maximum_corner_sliding_distance
- **Type:** [[double (type)]]

### heartbeat
- **Type:** [[Sound]]
- **Optional**
The sound played when the character's health is low.

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
Number of slots in the main inventory. May be 0.

### guns_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `3`
Must be between 1 and 15.

### build_distance
- **Type:** [[uint32 (type)]]

### drop_item_distance
- **Type:** [[uint32 (type)]]

### reach_distance
- **Type:** [[uint32 (type)]]

### reach_resource_distance
- **Type:** [[double (type)]]

### item_pickup_distance
- **Type:** [[double (type)]]

### loot_pickup_distance
- **Type:** [[double (type)]]

### ticks_to_keep_gun
- **Type:** [[uint32 (type)]]

### ticks_to_keep_aiming_direction
- **Type:** [[uint32 (type)]]

### ticks_to_stay_in_combat
- **Type:** [[uint32 (type)]]

### damage_hit_tint
- **Type:** [[Color (type)]]

### mining_with_tool_particles_animation_positions
- **Type:** array<[[float (type)]]>
List of positions in the mining with tool animation when the mining sound and mining particles are created.
**Examples:**

```
mining_with_tool_particles_animation_positions = {28}
```

### running_sound_animation_positions
- **Type:** array<[[float (type)]]>
List of positions in the running animation when the walking sound is played.
**Examples:**

```
running_sound_animation_positions = {14, 29}
```

### moving_sound_animation_positions
- **Type:** array<[[float (type)]]>
List of positions in the running animation when the moving sound is played.

### animations
- **Type:** array<[[CharacterArmorAnimation]]>

### crafting_categories
- **Type:** array<[[RecipeCategoryID (type)]]>
- **Optional**
Names of the crafting categories the character can craft recipes from. The built-in categories can be found [here](https://wiki.factorio.com/Data.raw#recipe-category). See also [[RecipeCategory]].

### mining_categories
- **Type:** array<[[ResourceCategoryID]]>
- **Optional**
Names of the resource categories the character can mine resources from.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### flying_bob_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### grounded_landing_search_radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The search radius for a non-colliding position to move the player to if they are grounded mid-flight. Must be >= 0.

### enter_vehicle_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `3.0`
Must be >= 0.

### tool_attack_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.5`

### respawn_time
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`
Time in seconds. Must be positive

### has_belt_immunity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this character is moved by belts when standing on them.

### character_corpse
- **Type:** [[EntityID (type)]]
- **Optional**
Name of the character corpse that is spawned when this character dies.

### flying_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
This collision mask is used when the character is flying.

Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"character/flying"`.

### tool_attack_result
- **Type:** [[Trigger]]
- **Optional**

### footstep_particle_triggers
- **Type:** [[FootstepTriggerEffectList]]
- **Optional**
Triggered every tick of the running animation.

### synced_footstep_particle_triggers
- **Type:** [[FootstepTriggerEffectList]]
- **Optional**
Triggered when the running animation (`animations`) rolls over the frames defined in `right_footprint_frames` and `left_footprint_frames`.

### footprint_particles
- **Type:** array<[[FootprintParticle]]>
- **Optional**
Triggered when the running animation (`animations`) rolls over the frames defined in `right_footprint_frames` and `left_footprint_frames`.

### left_footprint_offset
- **Type:** [[Vector (type)]]
- **Optional**
Offset from the center of the entity for the left footprint. Used by `footprint_particles`.

### right_footprint_offset
- **Type:** [[Vector (type)]]
- **Optional**
Offset from the center of the entity for the right footprint. Used by `footprint_particles`.

### right_footprint_frames
- **Type:** array<[[float (type)]]>
- **Optional**
The frames in the running animation (`animations`) where the right foot touches the ground.

### left_footprint_frames
- **Type:** array<[[float (type)]]>
- **Optional**
The frames in the running animation (`animations`) where the left foot touches the ground.

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).
