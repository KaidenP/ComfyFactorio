---
title: RecipeCategory
tags: [factorio-api, prototype]
---
# RecipeCategory

> **Parent:** [[Prototype]] · **Type name:** `recipe-category`

A recipe category. The built-in categories can be found [here](https://wiki.factorio.com/Data.raw#recipe-category). See [[RecipePrototype#categories|RecipePrototype::categories]]. Recipe categories can be used to specify which [[CraftingMachinePrototype#crafting_categories|machine]] can craft which [[RecipePrototype|recipes]].

The recipe category with the name "crafting" cannot contain recipes with fluid ingredients or products.

## Example

```
{
  type = "recipe-category",
  name = "my-category"
}
```
