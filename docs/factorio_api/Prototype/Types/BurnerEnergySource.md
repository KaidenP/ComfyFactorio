---
title: BurnerEnergySource
tags: [factorio-api, prototype, type]
---
# BurnerEnergySource

> **Parent:** [[BaseEnergySource]]

## Properties

### type
- **Type:** `"burner"`

### fuel_inventory_size
- **Type:** [[ItemStackIndex (type)]]

### burnt_inventory_size
- **Type:** [[ItemStackIndex (type)]]
- **Optional**
- **Default:** `0`

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**

### light_flicker
- **Type:** [[LightFlickeringDefinition]]
- **Optional**

### effectivity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
`1` means 100% effectivity. Must be greater than `0`. Multiplier of the energy output.

### burner_usage
- **Type:** [[BurnerUsageID]]
- **Optional**
- **Default:** `"fuel"`

### fuel_categories
- **Type:** array<[[FuelCategoryID]]>
- **Optional**
- **Default:** `{"chemical"}`
The energy source can be used with fuel from these [[FuelCategory|fuel categories]].

### initial_fuel
- **Type:** [[ItemID (type)]]
- **Optional**
- **Default:** `""`

### initial_fuel_percent
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.25`

### auto_refuel
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If this burner attempts to auto-refill fuel from the owner character, car, spider vehicle, cargo wagon, or artillery wagon.

### hide_from_stats
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set, items consumed and produced by this burner will not appear in item production statistics.
