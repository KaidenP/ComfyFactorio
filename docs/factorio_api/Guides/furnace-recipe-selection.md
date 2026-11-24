---
title: furnace-recipe-selection
tags: [factorio-api, guide]
---
## Furnace Recipe Selection

This page describes how the [[FurnacePrototype|'furnace']] selects a recipe from the available ingredients.

Only recipes with a single [[ItemIngredientPrototype|item ingredient]], a single [[FluidIngredientPrototype|fluid ingredient]], or one fluid and one item ingredient can be used by furnaces. Only recipes that are [[LuaRecipe#enabled|enabled]] and pass the [[LuaRecipePrototype#surface_conditions|surface condition]] checks can be selected.

When selecting a recipe based on the fluid ingredient, the first recipe in inventory order (by [[PrototypeBase#subgroup|subgroup]] and then [[PrototypeBase#order|order]]) that matches the fluid ingredient is picked. The quality of the recipe is always normal.

When selecting a recipe based on the item ingredient, the first recipe in inventory order (by [[PrototypeBase#subgroup|subgroup]] and then [[PrototypeBase#order|order]]) that matches the item ingredient is picked.

After that, the recipe quality is chosen based on the item ingredient's quality. There are three possible paths for choosing the recipe quality:

- If the recipe has [[RecipePrototype#can_set_quality|can_set_quality]] set to `false`, the normal recipe quality is chosen.
- If the recipe has [[RecipePrototype#can_set_quality|can_set_quality]] set to `true` and the item ingredient does not have quality control, meaning [[ItemIngredientPrototype#quality_change|quality_change]], [[ItemIngredientPrototype#quality_min|quality_min]], and [[ItemIngredientPrototype#quality_max|quality_max]] are not set, the recipe quality is set to the item ingredient's quality.
- If the recipe has [[RecipePrototype#can_set_quality|can_set_quality]] set to `true` and the item ingredient has quality control, meaning any of [[ItemIngredientPrototype#quality_change|quality_change]], [[ItemIngredientPrototype#quality_min|quality_min]], or [[ItemIngredientPrototype#quality_max|quality_max]] are set, the recipe quality is set to the reverse of the [[ItemIngredientPrototype#quality_change|quality_change]] applied to the item ingredient's quality.

If the chosen recipe quality requires a different item ingredient quality than the available item ingredient's quality, the recipe is not selected.

If the furnace has recipes with one fluid and one item ingredient, the recipe is selected based on the fluid and item, and that recipe's quality is selected based on the item. If this does not find a recipe, then the recipe and recipe quality is selected based only on the item. If this also fails, the recipe is selected based only on the fluid and the recipe quality is always normal. The selection of the recipe and recipe quality based on item/fluid follow the same algorithm as described above.

