---
title: GatePrototype
tags: [factorio-api, prototype]
---
# GatePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `gate`

A [gate](https://wiki.factorio.com/Gate).

## Properties

### vertical_animation
- **Type:** [[Animation]]
- **Optional**

### horizontal_animation
- **Type:** [[Animation]]
- **Optional**

### vertical_rail_animation_left
- **Type:** [[Animation]]
- **Optional**

### vertical_rail_animation_right
- **Type:** [[Animation]]
- **Optional**

### horizontal_rail_animation_left
- **Type:** [[Animation]]
- **Optional**

### horizontal_rail_animation_right
- **Type:** [[Animation]]
- **Optional**

### vertical_rail_base
- **Type:** [[Animation]]
- **Optional**

### horizontal_rail_base
- **Type:** [[Animation]]
- **Optional**

### wall_patch
- **Type:** [[Animation]]
- **Optional**

### opening_speed
- **Type:** [[float (type)]]

### activation_distance
- **Type:** [[double (type)]]

### timeout_to_close
- **Type:** [[uint32 (type)]]

### opening_sound
- **Type:** [[Sound]]
- **Optional**
Played when the gate opens.

### closing_sound
- **Type:** [[Sound]]
- **Optional**
Played when the gate closes.

### fadeout_interval
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### opened_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
This collision mask is used when the gate is open.

Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"gate/opened"`.
