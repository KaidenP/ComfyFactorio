---
title: LuaRecipePrototype
tags: [factorio-api, runtime, class]
---
# LuaRecipePrototype

> **Extends:** [[LuaPrototypeBase]]

A crafting recipe prototype.

## Attributes

### enabled
- **Type:** [[boolean]]
If this recipe prototype is enabled by default (enabled at the beginning of a game).

### categories
- **Type:** array<[[string]]>
Categories of the recipe.

### ingredients
- **Type:** array<[[Ingredient]]>
The ingredients to this recipe.
**Examples:**

```
-- The ingredients of "advanced-oil-processing" would look like this
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

### main_product
- **Type:** [[Product]]
- **Optional**
The main product of this recipe, if any.

### hidden_from_flow_stats
- **Type:** [[boolean]]
Is the recipe hidden from flow statistics (item/fluid production statistics)?

### hidden_from_player_crafting
- **Type:** [[boolean]]
Is the recipe hidden from player crafting? The recipe will still show up for selection in machines.

### always_show_made_in
- **Type:** [[boolean]]
Should this recipe always show "Made in" in the tooltip?

### energy
- **Type:** [[double]]
Energy required to execute this recipe. This directly affects the crafting time: Recipe's energy is exactly its crafting time in seconds, when crafted in an assembling machine with crafting speed exactly equal to one.

### request_paste_multiplier
- **Type:** [[uint32]]
The multiplier used when this recipe is copied from an assembling machine to a requester chest or infinity chest. For each item ingredient in the recipe the `ingredient_amount * requester_paste_multiplier * machine_crafting_speed / energy_required` is set in the chest.

### overload_multiplier
- **Type:** [[uint32]]
Used to determine how many extra items are put into an assembling machine before it's considered "full enough".

### maximum_productivity
- **Type:** [[double]]
The maximal productivity bonus that can be achieved with this recipe.

### allow_inserter_overload
- **Type:** [[boolean]]
If the recipe is allowed to have the extra inserter overload bonus applied (4 * stack inserter stack size).

### allow_as_intermediate
- **Type:** [[boolean]]
If this recipe is enabled for the purpose of intermediate hand-crafting.

### allow_intermediates
- **Type:** [[boolean]]
If this recipe is allowed to use intermediate recipes when hand-crafting.

### emissions_multiplier
- **Type:** [[double]]
The emissions multiplier for this recipe.

### allow_decomposition
- **Type:** [[boolean]]
Whether this recipe is allowed to be broken down for the recipe tooltip "Total raw" calculations.

### unlock_results
- **Type:** [[boolean]]
Whether this recipe unlocks the result item(s) so they're shown in filter-select GUIs.

### hide_from_signal_gui
- **Type:** [[boolean]]
Whether this recipe is marked to be hidden from the signal GUI.

### hide_from_flow_stats
- **Type:** [[boolean]]

### hide_from_player_crafting
- **Type:** [[boolean]]

### hide_from_bonus_gui
- **Type:** [[boolean]]

### trash
- **Type:** array<[[LuaItemPrototype]]>
- **Optional**
The 'trash' items that this recipe might produce as a result of spoiling.

### preserve_products_in_machine_output
- **Type:** [[boolean]]

### allowed_effects
- **Type:** dictionary<[[string]] → [[boolean]]>
- **Optional**
The allowed module effects for this recipe, if any.

### allowed_module_categories
- **Type:** dictionary<[[string]] → `true`>
- **Optional**
The allowed module categories for this recipe, if any.

### effect_limitation_messages
- **Type:** array<[[LocalisedString]]>
- **Optional**

### surface_conditions
- **Type:** array<[[SurfaceCondition]]>
- **Optional**
The surface conditions required to craft this recipe.

### alternative_unlock_methods
- **Type:** array<[[LuaTechnologyPrototype]]>
- **Optional**
Additional technologies listed under "Unlocked by" on a recipe's Factoriopedia page.

### crafting_machine_tints
- **Type:** array<[[Color]]>

### factoriopedia_alternative
- **Type:** [[LuaRecipePrototype]]
- **Optional**
An alternative prototype that will be used to display info about this prototype in Factoriopedia.

### can_set_quality
- **Type:** [[boolean]]
True if a player can set quality of the recipe to craft. False when only normal quality recipes can be crafted.

### on_crafted_event
- **Type:** [[LuaEventType]]
- **Optional**
Event raised when this recipe is crafted. Only available if [[RecipePrototype#raise_on_crafted|RecipePrototype::raise_on_crafted]] was set to true.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### has_category
Checks if recipe has given category

**Parameters:**
- **`category`** — [[RecipeCategoryID]]

**Returns:**
- [[boolean]]: `true` if recipe has this category.

### get_ingredient_quality
Ingredient materials required to craft recipe when configured to a specific quality.

**Parameters:**
- **`ingredient_index`** — [[uint32]]
- **`recipe_quality`** — [[QualityID]] *(optional)*: Defaults to `normal`.

**Returns:**
- [[LuaQualityPrototype]]

### get_product_quality
Quality of the product given when recipe is configured to a specific quality.

**Parameters:**
- **`product_index`** — [[uint32]]
- **`recipe_quality`** — [[QualityID]] *(optional)*: Defaults to `normal`.

**Returns:**
- [[LuaQualityPrototype]]

### get_product_amount
Average amount of the product given.

**Parameters:**
- **`product_index`** — [[uint32]]
- **`productivity`** — [[double]] *(optional)*

**Returns:**
- [[double]]
