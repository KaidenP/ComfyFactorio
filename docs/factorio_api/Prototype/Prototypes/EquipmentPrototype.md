---
title: EquipmentPrototype
tags: [factorio-api, prototype]
---
# EquipmentPrototype

> **Parent:** [[Prototype]] · **Abstract**

Abstract base of all equipment modules. Equipment modules can be inserted into [[EquipmentGridPrototype|equipment grids]].

## Properties

### sprite
- **Type:** [[Sprite]]
The graphics to use when this equipment is shown inside an equipment grid.

### shape
- **Type:** [[EquipmentShape]]
How big this equipment should be in the grid and whether it should be one solid rectangle or of a custom shape.

### categories
- **Type:** array<[[EquipmentCategoryID]]>
Sets the categories of the equipment. It can only be inserted into [[EquipmentGridPrototype#equipment_categories|grids]] with at least one matching category.

### energy_source
- **Type:** [[ElectricEnergySource]]

### take_result
- **Type:** [[ItemID (type)]]
- **Optional**
- **Default:** `name` of this prototype
Name of the item prototype that should be returned to the player when they remove this equipment from an equipment grid.

### background_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** equipment_default_background_color in utility constants
The color that the background of this equipment should have when shown inside an equipment grid.

### background_border_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** equipment_default_background_border_color in utility constants
The color that the border of the background of this equipment should have when shown inside an equipment grid.

### grabbed_background_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** equipment_default_grabbed_background_color in utility constants
The color that the background of this equipment should have when held in the players hand and hovering over an equipment grid.
