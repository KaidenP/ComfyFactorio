---
title: GodControllerPrototype
tags: [factorio-api, prototype]
---
# GodControllerPrototype

> **Type name:** `god-controller` · **Instance limit:** 1

Properties of the god controller.

## Properties

### type
- **Type:** `"god-controller"`

### name
- **Type:** [[string (type)]]
Name of the god-controller. Base game uses "default".

### inventory_size
- **Type:** [[ItemStackIndex (type)]]

### movement_speed
- **Type:** [[double (type)]]
Must be >= 0.34375.

### item_pickup_distance
- **Type:** [[double (type)]]

### loot_pickup_distance
- **Type:** [[double (type)]]

### mining_speed
- **Type:** [[double (type)]]

### crafting_categories
- **Type:** array<[[RecipeCategoryID (type)]]>
- **Optional**
Names of the crafting categories the player can craft recipes from.

### mining_categories
- **Type:** array<[[ResourceCategoryID]]>
- **Optional**
Names of the resource categories the player can mine resources from.
