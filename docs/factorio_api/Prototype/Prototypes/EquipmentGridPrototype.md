---
title: EquipmentGridPrototype
tags: [factorio-api, prototype]
---
# EquipmentGridPrototype

> **Parent:** [[Prototype]] · **Type name:** `equipment-grid` · **Instance limit:** 255

The prototype of an equipment grid, for example the one used in a [power armor](https://wiki.factorio.com/Power_armor).

## Properties

### equipment_categories
- **Type:** array<[[EquipmentCategoryID]]>
Only [[EquipmentPrototype|equipment]] with at least one of these [[EquipmentCategory|categories]] can be inserted into the grid.

### width
- **Type:** [[uint32 (type)]]

### height
- **Type:** [[uint32 (type)]]

### locked
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this locked from user interaction which means that the user cannot put equipment into or take equipment from this equipment grid.
