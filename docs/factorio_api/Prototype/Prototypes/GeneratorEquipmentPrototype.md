---
title: GeneratorEquipmentPrototype
tags: [factorio-api, prototype]
---
# GeneratorEquipmentPrototype

> **Parent:** [[EquipmentPrototype]] · **Type name:** `generator-equipment`

Used by [portable fusion reactor](https://wiki.factorio.com/Portable_fusion_reactor). Provides power in equipment grids. Can produce power for free or use a burner energy source.

## Properties

### power
- **Type:** [[Energy]]
The power output of this equipment.
**Examples:**

```
power = "750kW"
```

### burner
- **Type:** [[BurnerEnergySource]]
- **Optional**
If not defined, this equipment produces power for free.
