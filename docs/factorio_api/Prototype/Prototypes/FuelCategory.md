---
title: FuelCategory
tags: [factorio-api, prototype]
---
# FuelCategory

> **Parent:** [[Prototype]] · **Type name:** `fuel-category` · **Instance limit:** 255

Each item which has a fuel_value must have a fuel category. The fuel categories are used to allow only certain fuels to be used in [[EnergySource]].

## Properties

### fuel_value_type
- **Type:** [[LocalisedString (type)]]
- **Optional**
- **Default:** `{"description.fuel-value"}`

## Example

```
{
  type = "fuel-category",
  name = "best-fuel"
}
```
