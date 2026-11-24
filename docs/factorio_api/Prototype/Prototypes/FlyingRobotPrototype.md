---
title: FlyingRobotPrototype
tags: [factorio-api, prototype]
---
# FlyingRobotPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

Abstract base for construction/logistics and combat robots.

## Properties

### speed
- **Type:** [[double (type)]]
The flying speed of the robot, in tiles/tick.

### max_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** max double
The maximum flying speed of the robot, including bonuses, in tiles/tick. Useful to limit the impact of [[WorkerRobotSpeedModifier|worker robot speed research]].

Must be >= speed.

### max_energy
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
How much energy can be stored in the batteries.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].
**Examples:**

```
max_energy = "1.5MJ"
```

### energy_per_move
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
How much energy does it cost to move 1 tile.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].
**Examples:**

```
energy_per_move = "5kJ"
```

### energy_per_tick
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
How much energy does it cost to fly for 1 tick.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].
**Examples:**

```
energy_per_tick = "0.05kJ"
```

### min_to_charge
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.2`
The robot will go to charge when its battery fill ratio is less than this.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].

### max_to_charge
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.95`
If the robot's battery fill ratio is more than this, it does not need to charge before stationing.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].

### speed_multiplier_when_out_of_energy
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Some robots simply crash, some slowdown but keep going. 0 means crash.

Used only by [[RobotWithLogisticInterfacePrototype|robots with logistic interface]].
**Examples:**

```
speed_multiplier_when_out_of_energy = 0.2
```

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `35`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
