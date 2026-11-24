---
title: LuaRecipe
tags: [factorio-api, runtime, class]
---
# LuaRecipe

A crafting recipe. Recipes belong to forces (see [[LuaForce]]) because some recipes are unlocked by research, and researches are per-force.

## Attributes

### name
- **Type:** [[string]]
Name of the recipe. This can be different than the name of the result items as there could be more recipes to make the same item.

### localised_name
- **Type:** [[LocalisedString]]
Localised name of the recipe.

### localised_description
- **Type:** [[LocalisedString]]

### prototype
- **Type:** [[LuaRecipePrototype]]
The prototype for this recipe.

### enabled
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Can the recipe be used?

### categories
- **Type:** array<[[string]]>
Categories of the recipe.

### ingredients
- **Type:** array<[[Ingredient]]>
The ingredients to this recipe.
**Examples:**

```
-- The ingredients of "advanced-oil-processing" would look like this:
{{type="fluid", name="crude-oil", amount=100}, {type="fluid", name="water", amount=50}}
```

### products
- **Type:** array<[[Product]]>
The results/products of this recipe.
**Examples:**

```
-- The products of "advanced-oil-processing" would look like this:
{{type="fluid", name="heavy-oil", amount=25}, {type="fluid", name="light-oil", amount=45}, {type="fluid", name="petroleum-gas", amount=55}}
```

### hidden
- **Type:** [[boolean]]
Is the recipe hidden? Hidden recipes don't show up in the crafting menu.

### hidden_from_flow_stats
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
Is the recipe hidden from flow statistics?

### energy
- **Type:** [[double]]
Energy required to execute this recipe. This directly affects the crafting time: Recipe's energy is exactly its crafting time in seconds, when crafted in an assembling machine with crafting speed exactly equal to one.

### order
- **Type:** [[string]]
The string used to alphabetically sort these prototypes. It is a simple string that has no additional semantic meaning.

### group
- **Type:** [[LuaItemGroup]]
Group of this recipe.

### subgroup
- **Type:** [[LuaItemSubGroup]]
Subgroup of this recipe.

### force
- **Type:** [[LuaForce]]
The force that owns this recipe.

### productivity_bonus
- **Type:** [[EffectValue]]
- **Writable:** [[EffectValue]]
The productivity bonus for this recipe.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### reload
Reload the recipe from the prototype.

### has_category
Checks if recipe has given category

**Parameters:**
- **`category`** — [[RecipeCategoryID]]

**Returns:**
- [[boolean]]: `true` if recipe has this category.
