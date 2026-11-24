---
title: CorpsePrototype
tags: [factorio-api, prototype]
---
# CorpsePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `corpse`

Used for corpses, for example the remnants when destroying buildings.

## Properties

### dying_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Multiplier for `time_before_shading_off` and `time_before_removed`. Must be positive.

Controls the speed of the animation: `1 ÷ dying_speed = duration of the animation`

### splash_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Controls the speed of the splash animation: `1 ÷ splash_speed = duration of the splash animation`

### time_before_shading_off
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** 60 * 15 (15 seconds)
Controls how long the corpse takes to fade, as in how long it takes to get from no transparency to full transparency/removed. This time is *not* added to `time_before_removed`, it is instead subtracted from it. So by default, the corpse starts fading about 15 seconds before it gets removed.

### time_before_removed
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** 60 * 120 (120 seconds)
Time in ticks this corpse lasts. May not be 0.

### expires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### protected_from_tile_building
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**

### remove_on_entity_placement
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### remove_on_tile_placement
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### auto_setup_collision_box
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If true, and the collision box is unset, this will take the collision box of the first entity that uses this corpse.

### final_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"corpse"`

### ground_patch_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"ground-patch"`

### animation_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### splash_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### animation_overlay_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### animation_overlay_final_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"corpse"`

### shuffle_directions_at_frame
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
Defines after which frame in the `animation` the `direction_shuffle` should be applied. Can be set to `0`, frames are 1-indexed.

### use_tile_color_for_ground_patch_tint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### use_decay_layer
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### underwater_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `1`

### ground_patch_fade_in_delay
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### ground_patch_fade_in_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### ground_patch_fade_out_start
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### decay_frame_transition_duration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### animation
- **Type:** [[RotatedAnimationVariations]]
- **Optional**
The dying animation.

### animation_overlay
- **Type:** [[RotatedAnimationVariations]]
- **Optional**
Variation count must be the same as `animation` variation count. Direction count must be the same as `animation` direction count. Frame count must be the same as `animation` frame count.

### decay_animation
- **Type:** [[RotatedAnimationVariations]]
- **Optional**

### splash
- **Type:** [[AnimationVariations]]
- **Optional**

### ground_patch
- **Type:** [[AnimationVariations]]
- **Optional**

### ground_patch_higher
- **Type:** [[AnimationVariations]]
- **Optional**

### ground_patch_decay
- **Type:** [[AnimationVariations]]
- **Optional**

### underwater_patch
- **Type:** [[RotatedSprite]]
- **Optional**

### ground_patch_fade_out_duration
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### direction_shuffle
- **Type:** array<array<[[uint16 (type)]]>>
- **Optional**
- **Default:** No direction shuffle
May not be an empty array. May not be used if there is no `animation` defined.

The inner arrays are called "groups" and must all have the same size.

The indices map to the directions of `animation` and they are 1-indexed. After the `shuffle_directions_at_frame` frame of the `animation`, these indices are used as the direction when choosing which frame to render. The chosen shuffled direction can be any direction in the same group as the non-shuffled direction. Which direction is chosen from the group depends on the shuffle variation which is `dying_graphics_variation % group_size`.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
