---
title: CreateEntityTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# CreateEntityTriggerEffectItem

> **Parent:** [[TriggerEffectItem (type)]]

## Properties

### type
- **Type:** `"create-entity"`

### entity_name
- **Type:** [[EntityID (type)]]
The name of the entity that should be created.

### offset_deviation
- **Type:** [[BoundingBox (type)]]
- **Optional**

### trigger_created_entity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, the [[on_trigger_created_entity]] event will be raised.

### check_buildability
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### preserve_ghosts_and_corpses
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, colliding ghosts and corpses will not be removed by the creation of some entity types.

### show_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**

### show_details_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### only_when_visible
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Create the entity only when they are within a 200 tile range of any connected player.

### tile_collision_mask
- **Type:** [[TileCollisionMaskConnector]]
- **Optional**
Entity creation will not occur if any tile matches the collision condition. Defaults to no collisions.

### offsets
- **Type:** array<[[Vector (type)]]>
- **Optional**
If multiple offsets are specified, multiple entities are created. The projectile of the [Distractor capsule](https://wiki.factorio.com/Distractor_capsule) uses this property to spawn three Distractors.

### as_enemy
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, creates the entity as a member of the enemy force. If the surface.no_enemies_mode is true, the entity will not be created.

### ignore_no_enemies_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true and `as_enemy` is true, allows the entity to be created even if the current surface.no_enemies_mode is true.

### find_non_colliding_position
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### abort_if_over_space
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### non_colliding_search_radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `5`

### non_colliding_search_precision
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.2`

### non_colliding_fail_result
- **Type:** [[Trigger]]
- **Optional**
Only loaded if `find_non_colliding_position` is defined.

### protected
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
The result entity will be protected from automated attacks of enemies.
