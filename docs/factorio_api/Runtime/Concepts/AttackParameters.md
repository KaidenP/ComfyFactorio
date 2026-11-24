---
title: AttackParameters
tags: [factorio-api, runtime, concept]
---
# AttackParameters

## Fields

### type
- **Type:** `"projectile"` | `"stream"` | `"beam"`
The type of AttackParameter.

### range
- **Type:** [[float]]
Maximum range of attack.

### min_range
- **Type:** [[float]]
Minimum range of attack. Used with flamethrower turrets to prevent self-immolation.

### range_mode
- **Type:** [[RangeMode]]
Defines how the range is determined.

### fire_penalty
- **Type:** [[float]]
When searching for the nearest enemy to attack, `fire_penalty` is added to the enemy's distance if they are on fire.

### rotate_penalty
- **Type:** [[float]]
When searching for an enemy to attack, a higher `rotate_penalty` will discourage targeting enemies that would take longer to turn to face.

### health_penalty
- **Type:** [[float]]
When searching for an enemy to attack, a higher `health_penalty` will discourage targeting enemies with high health ratio. A negative penalty will do the opposite.

### threatening_asteroid_penalty
- **Type:** [[float]]
When searching for an enemy to attack, a higher `threatening_asteroid_penalty` will discourage targeting asteroids that pose a threat. A negative penalty will do the opposite.

### min_attack_distance
- **Type:** [[float]]
If less than `range`, the entity will choose a random distance between `range` and `min_attack_distance` and attack from that distance. Used for spitters.

### turn_range
- **Type:** [[float]]
The arc that the entity can attack in as a fraction of a circle. A value of `1` means the full 360 degrees.

### damage_modifier
- **Type:** [[float]]
Multiplier applied to the damage of an attack.

### ammo_consumption_modifier
- **Type:** [[float]]
Multiplier applied to the ammo consumption of an attack.

### cooldown
- **Type:** [[float]]
Minimum amount of ticks between shots. If this is less than `1`, multiple shots can be performed per tick.

### warmup
- **Type:** [[uint32]]
Number of ticks it takes for the weapon to actually shoot after it has been ordered to do so.

### movement_slow_down_factor
- **Type:** [[double]]

### movement_slow_down_cooldown
- **Type:** [[float]]

### ammo_type
- **Type:** [[AmmoType]]
- **Optional**

### ammo_categories
- **Type:** array<[[string]]>
- **Optional**
List of the names of compatible [[LuaAmmoCategoryPrototype|LuaAmmoCategoryPrototypes]].
