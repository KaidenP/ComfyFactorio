---
title: BeaconPrototype
tags: [factorio-api, prototype]
---
# BeaconPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `beacon`

Entity with the ability to transfer [[ModulePrototype|module]] effects to its neighboring entities.

## Properties

### energy_usage
- **Type:** [[Energy]]
The constant power usage of this beacon.
**Examples:**

```
energy_usage = "480kW"
```

### energy_source
- **Type:** [[ElectricEnergySource]] | [[VoidEnergySource]]

### supply_area_distance
- **Type:** [[uint32 (type)]]
The maximum distance that this beacon can supply its neighbors with its module's effects. Max distance is 64.

### distribution_effectivity
- **Type:** [[double (type)]]
The multiplier of the module's effects, when shared between neighbors.

### distribution_effectivity_bonus_per_quality_level
- **Type:** [[double (type)]]
- **Optional**
Must be 0 or positive.

### module_slots
- **Type:** [[ItemStackIndex (type)]]
The number of module slots in this beacon.

### quality_affects_module_slots
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#beacon_module_slots_bonus|QualityPrototype::beacon_module_slots_bonus]] will be added to module slots count.

### quality_affects_supply_area_distance
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#beacon_supply_area_distance_bonus|QualityPrototype::beacon_supply_area_distance_bonus]] will be added to supply_area_distance. Total value will be clamped to be within range `[0, 64]`.

### graphics_set
- **Type:** [[BeaconGraphicsSet]]
- **Optional**
The graphics for the beacon.

### animation
- **Type:** [[Animation]]
- **Optional**
Only loaded if `graphics_set` is not defined.

The animation for the beacon, when in use.

### base_picture
- **Type:** [[Animation]]
- **Optional**
Only loaded if `graphics_set` is not defined.

The picture of the beacon when it is not on.

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed.

### radius_visualisation_picture
- **Type:** [[Sprite]]
- **Optional**

### allowed_effects
- **Type:** [[EffectTypeLimitation]]
- **Optional**
- **Default:** No effects are allowed
The types of [[ModulePrototype|modules]] that a player can place inside of the beacon.

### allowed_module_categories
- **Type:** array<[[ModuleCategoryID]]>
- **Optional**
- **Default:** All module categories are allowed
Sets the [[ModuleCategory|module categories]] that are allowed to be inserted into this machine.

### profile
- **Type:** array<[[double (type)]]>
- **Optional**
Extra multiplier applied to the effects received from beacon by the effect receiver based on amount of beacons that are in range of that effect receiver.

If there are more beacons that reach the effect receiver than there are entries in this array, then the last entry in the array is used for the multiplier.

If this is not defined, then an implicit profile of `{1}` will be used.
**Examples:**

```
profile = {1, 0} -- entities do not receive any effects when they are in range of more than one beacon
```

### beacon_counter
- **Type:** `"total"` | `"same_type"`
- **Optional**
- **Default:** `"total"`
The beacon counter used by effect receiver when deciding which sample to take from `profile`.
