---
title: ItemSubGroup
tags: [factorio-api, prototype]
---
# ItemSubGroup

> **Parent:** [[Prototype]] · **Type name:** `item-subgroup`

An item subgroup. Item subgroups are the rows in the recipe list in the player's inventory GUI. The subgroup of a prototype also determines its item [[ItemGroup#group|group]] (tab in the recipe list).

The built-in subgroups can be found [here](https://wiki.factorio.com/Data.raw#item-subgroup). See [[ItemPrototype#subgroup|ItemPrototype::subgroup]] for setting the subgroup of an item.

## Properties

### group
- **Type:** [[ItemGroupID (type)]]
The item group this subgroup is located in.

## Example

```
{
  type = "item-subgroup",
  name = "train-transport",
  group = "logistics",
  order = "e"
}
```
