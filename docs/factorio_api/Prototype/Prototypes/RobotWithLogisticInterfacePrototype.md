---
title: RobotWithLogisticInterfacePrototype
tags: [factorio-api, prototype]
---
# RobotWithLogisticInterfacePrototype

> **Parent:** [[FlyingRobotPrototype]] · **Abstract**

The common properties of logistic and construction robots represented by an abstract prototype.

## Properties

### max_payload_size
- **Type:** [[ItemCountType (type)]]
The robot's cargo carrying capacity. Can be increased by [[WorkerRobotStorageModifier|worker robot cargo size research]].

### max_payload_size_after_bonus
- **Type:** [[ItemCountType (type)]]
- **Optional**
- **Default:** max ItemCountType
The robot's maximum possible cargo carrying capacity, including bonuses. Useful to limit the impact of [[WorkerRobotStorageModifier|worker robot cargo size research]].

Must be >= max_payload_size.

### idle
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the idle state cannot be animated.

### in_motion
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the in_motion state cannot be animated.

### shadow_idle
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the idle state cannot be animated.

### shadow_in_motion
- **Type:** [[RotatedAnimation]]
- **Optional**
Only the first frame of the animation is drawn. This means that the graphics for the in_motion state cannot be animated.

### destroy_action
- **Type:** [[Trigger]]
- **Optional**
Applied when the robot expires (runs out of energy and [[FlyingRobotPrototype#speed_multiplier_when_out_of_energy|FlyingRobotPrototype::speed_multiplier_when_out_of_energy]] is 0).

### draw_cargo
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### require_charge_to_mine
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, this can't be mined unless it has more than [[FlyingRobotPrototype#max_to_charge|FlyingRobotPrototype::max_to_charge]] energy, or the players personal roboports have enough energy to charge it.

### charging_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
