---
title: BlueprintEquipment
tags: [factorio-api, runtime, concept]
---
# BlueprintEquipment

## Fields

### equipment
- **Type:** [[EquipmentWithQualityID]]

### position
- **Type:** [[EquipmentPosition]]

### power_production
- **Type:** [[double]]
- **Optional**
Only used for equipment of type `"electric-energy-interface-equipment"`.

### power_usage
- **Type:** [[double]]
- **Optional**
Only used for equipment of type `"electric-energy-interface-equipment"`.

### buffer_size
- **Type:** [[double]]
- **Optional**
Only used for equipment of type `"electric-energy-interface-equipment"`.

### burner_fuel_inventory
- **Type:** [[BlueprintInventoryWithFilters]]
- **Optional**
Only used for equipment of type `"generator-equipment"` that has a burner energy source.
