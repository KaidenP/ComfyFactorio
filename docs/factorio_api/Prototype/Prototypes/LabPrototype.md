---
title: LabPrototype
tags: [factorio-api, prototype]
---
# LabPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `lab`

A [lab](https://wiki.factorio.com/Lab). It consumes science packs (items) to research [[TechnologyPrototype|technologies]].

## Properties

### energy_usage
- **Type:** [[Energy]]
The amount of energy this lab uses.

### energy_source
- **Type:** [[EnergySource]]
Defines how this lab gets energy.

### on_animation
- **Type:** [[Animation]]
- **Optional**
The animation that plays when the lab is active.

### off_animation
- **Type:** [[Animation]]
- **Optional**
The animation that plays when the lab is idle.

### frozen_patch
- **Type:** [[Sprite]]
- **Optional**

### inputs
- **Type:** array<[[ItemID (type)]]>
A list of the names of science packs that can be used in this lab.

If a technology requires other types of science packs, it cannot be researched in this lab.
**Examples:**

```
inputs = {"automation-science-pack", "logistic-science-pack", "chemical-science-pack", "military-science-pack", "production-science-pack", "utility-science-pack", "space-science-pack"}
```

### researching_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### effect_receiver
- **Type:** [[EffectReceiver (type)]]
- **Optional**

### module_slots
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
The number of module slots in this lab.

### quality_affects_module_slots
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set, [[QualityPrototype#lab_module_slots_bonus|QualityPrototype::lab_module_slots_bonus]] will be added to module slots count.

### uses_quality_drain_modifier
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the [[QualityPrototype#science_pack_drain_multiplier|QualityPrototype::science_pack_drain_multiplier]] of the quality of this lab should affect how much science is consumed to research one unit of technology.

### science_pack_drain_rate_percent
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `100`
May not be `0` or larger than `100`.

### allowed_effects
- **Type:** [[EffectTypeLimitation]]
- **Optional**
- **Default:** All effects except quality are allowed
Sets the [[ModulePrototype|modules]] and [[BeaconPrototype|beacon]] effects that are allowed to be used on this lab.

### allowed_module_categories
- **Type:** array<[[ModuleCategoryID]]>
- **Optional**
- **Default:** All module categories are allowed
Sets the [[ModuleCategory|module categories]] that are allowed to be inserted into this machine.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### default_technology_level_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### trash_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**

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
