---
title: ItemGroup
tags: [factorio-api, prototype]
---
# ItemGroup

> **Parent:** [[Prototype]] · **Type name:** `item-group` · **Instance limit:** 255

An item group. Item groups are the tabs shown above the list of craftable items in the player's inventory GUI. The built-in groups are "logistics", "production", "intermediate-products" and "combat" but mods can define their own.

Items are sorted into item groups by sorting them into a [[ItemPrototype#subgroup|subgroup]] which then belongs to an [[ItemSubGroup#group|item group]].

## Properties

### icons
- **Type:** array<[[IconData]]>
- **Optional**
The icon that is shown to represent this item group. Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon that is shown to represent this item group.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

The base game uses 128px icons for item groups.

Only loaded if `icons` is not defined.

### order_in_recipe
- **Type:** [[Order]]
- **Optional**
- **Default:** The `order` of this item group.
Item ingredients in recipes are ordered by item group if [[RecipePrototype#sort_item_ingredients|RecipePrototype::sort_item_ingredients]] is set to `true`. The `order_in_recipe` property can be used to specify the ordering in recipes with sorted ingredients without affecting the item group's inventory order.

## Example

```
{
  type = "item-group",
  name = "logistics",
  order = "a",
  icon = "__base__/graphics/item-group/logistics.png",
  icon_size = 128,
}
```
