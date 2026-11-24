---
title: CombatRobotPrototype
tags: [factorio-api, prototype]
---
# CombatRobotPrototype

> **Parent:** [[FlyingRobotPrototype]] · **Type name:** `combat-robot`

A combat robot. Can attack enemies.

## Properties

### time_to_live
- **Type:** [[uint32 (type)]]

### attack_parameters
- **Type:** [[AttackParameters (type)]]

### idle
- **Type:** [[RotatedAnimation]]
- **Optional**

### shadow_idle
- **Type:** [[RotatedAnimation]]
- **Optional**

### in_motion
- **Type:** [[RotatedAnimation]]
- **Optional**

### shadow_in_motion
- **Type:** [[RotatedAnimation]]
- **Optional**

### range_from_player
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### friction
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### destroy_action
- **Type:** [[Trigger]]
- **Optional**
Applied when the combat robot expires (runs out of `time_to_live`).

### follows_player
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### light
- **Type:** [[LightDefinition]]
- **Optional**

### separation_range
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
The range within which the robot will try to separate itself from other friendly combat robots.

### max_separation_force
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
The maximum force that can be applied to separate from other friendly combat robots.

### separation_force_factor
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`
A factor determining how strongly the robot will try to separate from other friendly combat robots.

Higher values result in stronger separation forces.
