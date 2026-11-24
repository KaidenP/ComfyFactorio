---
title: SpiderLegPrototype
tags: [factorio-api, prototype]
---
# SpiderLegPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `spider-leg`

Used by [[SpiderLegSpecification (type)|SpiderLegSpecification]] for [[SpiderVehiclePrototype]], also known as [spidertron](https://wiki.factorio.com/Spidertron).

## Properties

### stretch_force_scalar
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.715`
A scalar that controls the amount of influence this leg has over the position of the torso. Must be greater than 0.

### hip_flexibility
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
The flexibility of hip. Must be between 0 and 1 inclusive. 0 means the hip doesn't flex at all, and 1 means the hip can bend the entire range, from straight up to straight down. Values less than one will dampen the hip flexibility and cause the upper and lower leg parts to stretch and squish more to compensate. Does not affect movement, only graphics.

### knee_height
- **Type:** [[double (type)]]
The resting height of the knee from the ground. Used to derive leg part length and size. If set too low, this could cause the knee to invert, bending inwards underneath the spider.

### knee_distance_factor
- **Type:** [[double (type)]]
The placement of the knee relative to the torso of the spider and the end of the foot when at rest. Used to calculate the shape of the leg and the length of the individual parts. Values between 0 and 1 place the knee between the torso and the leg. Values closer to 0 will place the knee closer to the torso.

### ankle_height
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The height of the foot from the ground when at rest.

### initial_movement_speed
- **Type:** [[double (type)]]

### movement_acceleration
- **Type:** [[double (type)]]

### target_position_randomisation_distance
- **Type:** [[double (type)]]

### minimal_step_size
- **Type:** [[double (type)]]

### base_position_selection_distance
- **Type:** [[double (type)]]

### movement_based_position_selection_distance
- **Type:** [[double (type)]]

### graphics_set
- **Type:** [[SpiderLegGraphicsSet]]
- **Optional**

### walking_sound_volume_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Cannot be negative.

### walking_sound_speed_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be larger than 0.

### upper_leg_dying_trigger_effects
- **Type:** array<[[SpiderLegTriggerEffect]]>
- **Optional**

### lower_leg_dying_trigger_effects
- **Type:** array<[[SpiderLegTriggerEffect]]>
- **Optional**

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
