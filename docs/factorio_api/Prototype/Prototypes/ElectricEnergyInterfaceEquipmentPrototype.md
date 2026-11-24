---
title: ElectricEnergyInterfaceEquipmentPrototype
tags: [factorio-api, prototype]
---
# ElectricEnergyInterfaceEquipmentPrototype

> **Parent:** [[EquipmentPrototype]] · **Type name:** `electric-energy-interface-equipment`

Provides or consumes power in equipment grids.

## Properties

### energy_production
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
**Examples:**

```
energy_production = "500GW"
```

### energy_usage
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
**Examples:**

```
energy_usage = "10kW"
```

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**
- **Default:** `"none"`

### show_power_production_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### show_power_usage_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### show_stored_energy_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
