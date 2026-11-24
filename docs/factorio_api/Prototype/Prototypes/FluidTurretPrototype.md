---
title: FluidTurretPrototype
tags: [factorio-api, prototype]
---
# FluidTurretPrototype

> **Parent:** [[TurretPrototype]] · **Type name:** `fluid-turret`

A turret that uses [[FluidPrototype|fluid]] as ammunition.

## Properties

### fluid_buffer_size
- **Type:** [[FluidAmount (type)]]

### fluid_buffer_input_flow
- **Type:** [[FluidAmount (type)]]

### activation_buffer_ratio
- **Type:** [[FluidAmount (type)]]
Before an turret that was out of fluid ammunition is able to fire again, the `fluid_buffer_size` must fill to this proportion.

### fluid_box
- **Type:** [[FluidBox]]

### muzzle_light
- **Type:** [[LightDefinition]]
- **Optional**

### enough_fuel_indicator_light
- **Type:** [[LightDefinition]]
- **Optional**

### not_enough_fuel_indicator_light
- **Type:** [[LightDefinition]]
- **Optional**

### muzzle_animation
- **Type:** [[Animation]]
- **Optional**

### folded_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### preparing_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### prepared_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### starting_attack_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### attacking_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### ending_attack_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### folding_muzzle_animation_shift
- **Type:** [[AnimatedVector]]
- **Optional**

### enough_fuel_indicator_picture
- **Type:** [[Sprite8Way]]
- **Optional**

### not_enough_fuel_indicator_picture
- **Type:** [[Sprite8Way]]
- **Optional**

### out_of_ammo_alert_icon
- **Type:** [[Sprite]]
- **Optional**
The sprite will be drawn on top of fluid turrets that are out of fluid ammunition. If the `out_of_ammo_alert_icon` is not set, [[UtilitySprites#fluid_icon|UtilitySprites::fluid_icon]] will be used instead.

### turret_base_has_direction
- **Type:** `true`
- **Overrides parent**
Always `true`, forcing the turret's collision box to be affected by its rotation.

### attack_parameters
- **Type:** [[StreamAttackParameters]]
- **Overrides parent**
Requires ammo_type in attack_parameters.
