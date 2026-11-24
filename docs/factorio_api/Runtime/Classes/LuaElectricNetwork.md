---
title: LuaElectricNetwork
tags: [factorio-api, runtime, class]
---
# LuaElectricNetwork

A LuaElectricNetwork represents a group of [[LuaElectricSubNetwork|LuaElectricSubNetworks]] that are directly or indirectly connected to each other through implicit connections (closed power switches, surface connections) and during next electric network update will transfer electricity from producers and consumers.

Electric networks can be merged together when a power switch is closed and can be split into multiple networks when power switch opens. Similarly turning on or off a global network may merge or split electric networks in a way that follows the expected electricity flows - two sub networks that are not directly or indirectly connected will be put into separate electric networks.

The electric network is what performs electric flow between entities. It does *not* track connected entities as that's the responsibility of the electric sub network.

## Attributes

### sub_networks
- **Type:** array<[[LuaElectricSubNetwork]]>

### statistics
- **Type:** [[LuaFlowStatistics]]
Statistics for this electric network.

If the electric network becomes invalid, the flow statistics obtained from it will also become invalid.

### flow_last_tick
- **Type:** table
Energy amounts of satisfaction percents related to latest electric network update.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_accumulators_energy
Gets total energy stored inside of accumulators that are part of any electric sub network covered by this electric network.

Takes a table with the following fields:
- **`name`** — [[EntityID]] *(optional)*: When given, only accumulators of this prototype will be considered.
- **`quality`** — [[QualityID]] *(optional)*: When given, only accumulators of this quality will be considered.

**Returns:**
- [[EnergyAndCapacityPair]]

### set_accumulators_energy
Changes energy stored inside of accumulators that are part of any electric sub network covered by this electric network.

Takes a table with the following fields:
- **`name`** — [[EntityID]] *(optional)*: When given, only accumulators of this prototype will be considered.
- **`quality`** — [[QualityID]] *(optional)*: When given, only accumulators of this quality will be considered.
- **`energy`** — [[double]]: New total energy to be set onto matching accumulators.
- **`equalize`** — [[boolean]] *(optional)*: Whether all accumulators should have the same charge ratio, regardless of whether that means discharging some of them. Defaults to `false`.
