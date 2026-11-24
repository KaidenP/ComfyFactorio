---
title: ProjectileAttackParameters
tags: [factorio-api, prototype, type]
---
# ProjectileAttackParameters

> **Parent:** [[BaseAttackParameters]]

## Properties

### type
- **Type:** `"projectile"`

### apply_projection_to_projectile_creation_position
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### projectile_center
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
When used with `projectile_creation_parameters`, this offsets what the turret's sprite looks at. Setting to `{0,1}` will cause the turret to aim one tile up from the target but the projectile will still aim for the entity. Can be used to give the illusion of height but can also confuse aim logic when set too high.

When used without `projectile_creation_parameters`, this sets the turret's rotation axis.

### projectile_creation_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### shell_particle
- **Type:** [[CircularParticleCreationSpecification (type)]]
- **Optional**
Used to show bullet shells/casings being ejected from the gun, see [artillery shell casings](https://factorio.com/blog/post/fff-345).

### projectile_creation_parameters
- **Type:** [[CircularProjectileCreationSpecification (type)]]
- **Optional**
Used to shoot projectiles from arbitrary points. Used by worms. If not set then the launch positions are calculated using `projectile_center` and `projectile_creation_distance`.

### projectile_orientation_offset
- **Type:** [[RealOrientation (type)]]
- **Optional**
- **Default:** `0`
Used to shoot from different sides of the turret. Setting to `0.25` shoots from the right side, `0.5` shoots from the back, and `0.75` shoots from the left. The turret will look at the enemy as normal but the bullet will spawn from the offset position. Can be used to create right-handed weapons.

### projectile_creation_offsets
- **Type:** array<[[Vector (type)]]>
- **Optional**
Used to shoot from multiple points. The turret will look at the enemy as normal but the bullet will spawn from a random offset position. Can be used to create multi-barreled weapons.
