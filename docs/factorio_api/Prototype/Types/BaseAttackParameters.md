---
title: BaseAttackParameters
tags: [factorio-api, prototype, type]
---
# BaseAttackParameters

> **Abstract**

The abstract base of all [[AttackParameters (type)|AttackParameters]].

## Properties

### range
- **Type:** [[float (type)]]
Before an entity can attack, the distance (in tiles) between the entity and target must be less than or equal to this.

### cooldown
- **Type:** [[float (type)]]
Number of ticks in which it will be possible to shoot again. If < 1, multiple shots can be performed in one tick.

### min_range
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The minimum distance (in tiles) between an entity and target. If a unit's target is less than this, the unit will attempt to move away before attacking. A [flamethrower turret](https://wiki.factorio.com/Flamethrower_turret) does not move, but has a minimum range. Less than this, it is unable to target an enemy.

### turn_range
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
If this is <= 0, it is set to 1. Arc from 0 to 1, so for example 0.25 is 90°. Used by the [flamethrower turret](https://wiki.factorio.com/Flamethrower_turret) in the base game. Arcs greater than 0.5 but less than 1 will be clamped to 0.5 as targeting in arcs larger than half circle is [not implemented](https://forums.factorio.com/94654).

### fire_penalty
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Used when searching for the nearest enemy, when this is > 0, enemies that aren't burning are preferred over burning enemies. Definition of "burning" for this: Entity has sticker attached to it, and the sticker has a [[StickerPrototype#spread_fire_entity|spread_fire_entity]] set.

### rotate_penalty
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
A higher penalty will discourage turrets from targeting units that would take longer to turn to face.

### health_penalty
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
A higher penalty will discourage turrets from targeting units with higher health ratio. A negative penalty will encourage turrets to target units with higher health ratio.

### threatening_asteroid_penalty
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
A higher penalty will discourage turrets from targeting asteroids that are threatening. A negative penalty will encourage turrets to target threatening asteroids.

### range_mode
- **Type:** [[RangeMode (type)]]
- **Optional**
- **Default:** `"center-to-center"`

### min_attack_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** equal to `range` property
If less than `range`, the entity will choose a random distance between `range` and `min_attack_distance` and attack from that distance.

### damage_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### ammo_consumption_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Must be greater than or equal to `0`.

### cooldown_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Must be between `0` and `1`.

### warmup
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Number of ticks it takes for the weapon to actually shoot after the order for shooting has been made. This also allows to "adjust" the shooting animation to the effect of shooting.

[[CapsuleAction (type)|CapsuleActions]] cannot have attack parameters with non-zero warmup.

### lead_target_for_projectile_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Setting this to anything but zero causes homing projectiles to aim for the predicted location based on enemy movement instead of the current enemy location. If set, this property specifies the distance travelled per tick of the fired projectile.
**Examples:**

```
-- this is same as particle horizontal speed of flamethrower fire stream
lead_target_for_projectile_speed = 0.2* 0.75 * 1.5
```

### lead_target_for_projectile_delay
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
Setting this to anything but zero causes projectiles to aim for the predicted location based on enemy movement instead of the current enemy location. If set, this property adds a flat number of ticks atop `lead_target_for_projectile_speed` that the shooter must lead.

### movement_slow_down_cooldown
- **Type:** [[float (type)]]
- **Optional**
- **Default:** equal to `cooldown` property

### movement_slow_down_factor
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### ammo_type
- **Type:** [[AmmoType (type)]]
- **Optional**
Can be mandatory.

### activation_type
- **Type:** `"shoot"` | `"throw"` | `"consume"` | `"activate"`
- **Optional**
- **Default:** `"shoot"`
Used in tooltips to set the tooltip category. It is also used to get the locale keys for activation instructions and speed of the action for the tooltip.

For example, an activation_type of "throw" will result in the tooltip category "thrown" and the tooltip locale keys "gui.instruction-to-throw" and "description.throwing-speed".

### sound
- **Type:** [[LayeredSound]]
- **Optional**
Played once at the start of the attack if these are [[ProjectileAttackParameters]].

### animation
- **Type:** [[RotatedAnimation]]
- **Optional**

### cyclic_sound
- **Type:** [[CyclicSound]]
- **Optional**
Played during the attack.

### use_shooter_direction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### ammo_categories
- **Type:** array<[[AmmoCategoryID (type)]]>
- **Optional**
Mandatory if `ammo_category` is not defined.

### ammo_category
- **Type:** [[AmmoCategoryID (type)]]
- **Optional**
Mandatory if `ammo_categories` is not defined.

### true_collinear_ejection
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Projectile will be creation position and orientation will be collinear with shooter and target (unless offset projectile center is specified). Used for railgun turrets to avoid unexpected friendly fire incidents.
