---
title: ItemStackDefinition
tags: [factorio-api, runtime, concept]
---
# ItemStackDefinition

## Fields

### name
- **Type:** [[string]]
Prototype name of the item the stack holds.

### count
- **Type:** [[ItemCountType]]
- **Optional**
Number of items the stack holds. Defaults to `1`.

### quality
- **Type:** [[string]]
- **Optional**
Quality of the item the stack holds. Defaults to `"normal"`.

### health
- **Type:** [[float]]
- **Optional**
Health of the items in the stack. Defaults to `1.0`.

### durability
- **Type:** [[double]]
- **Optional**
Durability of the tool items in the stack.

### ammo
- **Type:** [[float]]
- **Optional**
Amount of ammo in the ammo items in the stack.

### tags
- **Type:** [[Tags]]
- **Optional**
Tags of the items with tags in the stack.

### custom_description
- **Type:** [[LocalisedString]]
- **Optional**
Description of the items with tags in the stack.

### spoil_percent
- **Type:** [[double]]
- **Optional**
The spoil percent for this item if the item can spoil. Defaults to `0`.
