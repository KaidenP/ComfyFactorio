---
title: LandMinePrototype
tags: [factorio-api, prototype]
---
# LandMinePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `land-mine`

A [land mine](https://wiki.factorio.com/Land_mine).

## Properties

### picture_safe
- **Type:** [[Sprite]]
- **Optional**
The sprite of the landmine before it is armed (just after placing).

### picture_set
- **Type:** [[Sprite]]
- **Optional**
The sprite of the landmine of a friendly force when it is armed.

### trigger_radius
- **Type:** [[double (type)]]

### picture_set_enemy
- **Type:** [[Sprite]]
- **Optional**
The sprite of the landmine of an enemy force when it is armed.

### timeout
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `120`
Time between placing and the landmine being armed, in ticks.

### trigger_interval
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`
Time between checks to detonate due to nearby enemies, in ticks. A larger time will be more performant.

### action
- **Type:** [[Trigger]]
- **Optional**

### ammo_category
- **Type:** [[AmmoCategoryID (type)]]
- **Optional**

### force_die_on_attack
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Force the landmine to kill itself when exploding.

### trigger_force
- **Type:** [[ForceCondition (type)]]
- **Optional**
- **Default:** `"enemy"`

### trigger_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
- **Default:** Value of UtilityConstants::building_collision_mask
Collision mask that another entity must collide with to make this landmine blow up.

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `45`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**
