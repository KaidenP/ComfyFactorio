---
title: ProjectilePrototype
tags: [factorio-api, prototype]
---
# ProjectilePrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `projectile`

Entity with limited lifetime that can hit other entities and has triggers when this happens.

## Properties

### acceleration
- **Type:** [[double (type)]]
Must be != 0 if `turning_speed_increases_exponentially_with_projectile_speed` is true.

### animation
- **Type:** [[RotatedAnimationVariations]]
- **Optional**

### rotatable
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the animation of the projectile is rotated to match the direction of travel.

### enable_drawing_with_mask
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### direction_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Setting this to true can be used to disable projectile homing behaviour.

### hit_at_collision_position
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When true the entity is hit at the position on its collision box the projectile first collides with. When false the entity is hit at its own position.

### force_condition
- **Type:** [[ForceCondition (type)]]
- **Optional**
- **Default:** `"all"`

### piercing_damage
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Whenever an entity is hit by the projectile, this number gets reduced by the health of the entity. If the number is then below 0, the `final_action` is applied and the projectile destroyed. Otherwise, the projectile simply continues to its destination.

### max_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** MAX_DOUBLE
Must be greater than or equal to 0.

### turn_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be greater than or equal to 0.

### speed_modifier
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{1, 1}`

### height
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### action
- **Type:** [[Trigger]]
- **Optional**
Executed when the projectile hits something.

### final_action
- **Type:** [[Trigger]]
- **Optional**
Executed when the projectile hits something, after `action` and only if the entity that was hit was destroyed. The projectile is destroyed right after the final_action.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**

### hit_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"projectile/hit"`.

### turning_speed_increases_exponentially_with_projectile_speed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### shadow
- **Type:** [[RotatedAnimationVariations]]
- **Optional**

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
