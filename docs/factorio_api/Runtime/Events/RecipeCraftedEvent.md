---
title: RecipeCraftedEvent
tags: [factorio-api, runtime, event]
---
# RecipeCraftedEvent

Called when a recipe with [[RecipePrototype#raise_on_crafted|RecipePrototype::raise_on_crafted]] is crafted.

## Data

### entity
- **Type:** [[LuaEntity]]
Entity that crafted recipe.

### recipe
- **Type:** [[string]]
Name of recipe that was crafted.

### recipe_quality
- **Type:** [[string]]
Quality of the recipe crafted.

### quality_effect
- **Type:** [[EffectValue]]
- **Optional**
Quality effect used when giving products. Not provided if value is 0. May be different than value obtained from [[LuaEntity#effects|LuaEntity::effects]] when quality modules were changed between craft starting and products being given.

### quality_seed
- **Type:** [[double]]
- **Optional**
Random value in range [0, 1) that was used when selecting product quality. Only provided when quality_effect is provided.

### product_quality
- **Type:** [[string]]
Quality of products given. May be different than recipe quality if quality modules are present. Always provided even if quality_effect is zero because [[LuaEntity#result_quality|LuaEntity::result_quality]] may have been used. Only used by products without quality control.

### bonus
- **Type:** [[boolean]]
If crafted as part of bonus products.

### shared_roll
- **Type:** [[double]]
Random value in range [[ProductPrototypeBase#shared_probability]].

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
