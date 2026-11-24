---
title: LuaElectricSubNetwork
tags: [factorio-api, runtime, class]
---
# LuaElectricSubNetwork

A LuaElectricSubNetwork represents an electricity supply group.

When a supply group is related to electric poles, it spans over all poles that are connected with real (non ghost) wires and connects entities with an electric energy source in range of those poles.

When a supply group is related to a global electric network, it connects entities with an electric energy source on the same surface.

Implicit connections (when a power switch is closed, or when an electric pole is built on a surface with global network) do not cause supply groups to merge since they are not copper wire connections. Those connections will cause sub networks to have the same parent electric network causing electricity to be allowed to flow freely between multiple sub networks (electricity produced inside of one sub network that is connected through a power switch to a second sub network will be able to flow into a consumer connected to the second sub network).

The electric sub network keeps track of connected entities. It does *not* perform electricity flow as that's the responsibility of the electric network.

## Attributes

### id
- **Type:** [[uint32]]
Unique identifier of this electric sub network.

### parent_network
- **Type:** [[LuaElectricNetwork]]
Parent network to this sub network.

### neighbours
- **Type:** array<[[LuaElectricSubNetwork]]>
List of sub networks that are directly connected to this sub network through power switches or because they span over electric poles placed on a surface with global network (all poles on a surface with global network are implicitly connected to global network making their networks neighbour of a global network).

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_accumulators_energy
Gets total energy stored inside of accumulators connected to the electric sub network.

Takes a table with the following fields:
- **`name`** — [[EntityID]] *(optional)*: When given, only accumulators of this prototype will be considered.
- **`quality`** — [[QualityID]] *(optional)*: When given, only accumulators of this quality will be considered.

**Returns:**
- [[EnergyAndCapacityPair]]

### set_accumulators_energy
Changes energy stored inside of accumulators connected to the electric sub network.

Takes a table with the following fields:
- **`name`** — [[EntityID]] *(optional)*: When given, only accumulators of this prototype will be considered.
- **`quality`** — [[QualityID]] *(optional)*: When given, only accumulators of this quality will be considered.
- **`energy`** — [[double]]: New total energy to be set onto matching accumulators.
- **`equalize`** — [[boolean]] *(optional)*: Whether all accumulators should have the same charge ratio, regardless of whether that means discharging some of them. Defaults to `false`.
