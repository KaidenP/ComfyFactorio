---
title: ModulePrototype
tags: [factorio-api, prototype]
---
# ModulePrototype

> **Parent:** [[ItemPrototype]] · **Type name:** `module`

A [module](https://wiki.factorio.com/Module). They are used to affect the capabilities of existing machines, for example by increasing the crafting speed of a [[CraftingMachinePrototype|crafting machine]].

## Properties

### category
- **Type:** [[ModuleCategoryID]]
Used when upgrading modules: Ctrl + click modules into an entity and it will replace lower tier modules of the same category with higher tier modules.

### tier
- **Type:** [[uint32 (type)]]
Tier of the module inside its category. Used when upgrading modules: Ctrl + click modules into an entity and it will replace lower tier modules with higher tier modules if they have the same category.

### effect
- **Type:** [[Effect (type)]]
The effect of the module on the machine it's inserted in, such as increased pollution.

### requires_beacon_alt_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### art_style
- **Type:** [[string (type)]]
- **Optional**
Chooses with what art style the module is shown inside [[BeaconPrototype|beacons]]. See [[BeaconModuleVisualizations#art_style|BeaconModuleVisualizations::art_style]]. Vanilla uses `"vanilla"` here.

### beacon_tint
- **Type:** [[BeaconVisualizationTints]]
- **Optional**

### consumption_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
0.0 means that no quality scaling is applied (common for penalties). 1.0 means that the full scaling of the quality prototype applies.

Defaults to 1.0 if the module consumption effect is < 0, otherwise 0.0.

### speed_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
0.0 means that no quality scaling is applied (common for penalties). 1.0 means that the full scaling of the quality prototype applies.

Defaults to 1.0 if the module speed effect is > 0, otherwise 0.0.

### productivity_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
0.0 means that no quality scaling is applied (common for penalties). 1.0 means that the full scaling of the quality prototype applies.

Defaults to 1.0 if the module productivity effect is > 0, otherwise 0.0.

### pollution_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
0.0 means that no quality scaling is applied (common for penalties). 1.0 means that the full scaling of the quality prototype applies.

Defaults to 1.0 if the module pollution effect is < 0, otherwise 0.0.

### quality_quality_multiplier
- **Type:** [[float (type)]]
- **Optional**
0.0 means that no quality scaling is applied (common for penalties). 1.0 means that the full scaling of the quality prototype applies.

Defaults to 1.0 if the module quality effect is > 0, otherwise 0.0.
