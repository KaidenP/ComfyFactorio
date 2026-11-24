---
title: LuaLogisticCell
tags: [factorio-api, runtime, class]
---
# LuaLogisticCell

Logistic cell of a particular [[LuaEntity]]. A "Logistic Cell" is the given name for settings and properties used by what would normally be seen as a "Roboport". A logistic cell however doesn't have to be attached to the roboport entity (the character has one for the personal roboport).

## Attributes

### logistic_radius
- **Type:** [[float]]
Logistic radius of this cell.

### logistics_connection_distance
- **Type:** [[float]]
Logistic connection distance of this cell.

### construction_radius
- **Type:** [[float]]
Construction radius of this cell.

### stationed_logistic_robot_count
- **Type:** [[uint32]]
Number of stationed logistic robots in this cell.

### stationed_construction_robot_count
- **Type:** [[uint32]]
Number of stationed construction robots in this cell.

### mobile
- **Type:** [[boolean]]
`true` if this is a mobile cell. The logistic cell created by roboport equipment considered is mobile.

### transmitting
- **Type:** [[boolean]]
`true` if this cell is active.

### charge_approach_distance
- **Type:** [[float]]
Radius at which the robots hover when waiting to be charged.

### charging_robot_count
- **Type:** [[uint32]]
Number of robots currently charging.

### to_charge_robot_count
- **Type:** [[uint32]]
Number of robots waiting to charge.

### owner
- **Type:** [[LuaEntity]]
This cell's owner.

### logistic_network
- **Type:** [[LuaLogisticNetwork]]
- **Optional**
The network that owns this cell, if any.

### neighbours
- **Type:** array<[[LuaLogisticCell]]>
Neighbouring cells.

### charging_robots
- **Type:** array<[[LuaEntity]]>
Robots currently being charged.

### to_charge_robots
- **Type:** array<[[LuaEntity]]>
Robots waiting to charge.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### is_in_logistic_range
Is a given position within the logistic range of this cell?

**Parameters:**
- **`position`** — [[MapPosition]]

**Returns:**
- [[boolean]]

### is_in_construction_range
Is a given position within the construction range of this cell?

**Parameters:**
- **`position`** — [[MapPosition]]

**Returns:**
- [[boolean]]

### is_neighbour_with
Are two cells neighbours?

**Parameters:**
- **`other`** — [[LuaLogisticCell]]

**Returns:**
- [[boolean]]
