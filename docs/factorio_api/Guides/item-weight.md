---
title: item-weight
tags: [factorio-api, guide]
---
## Item Weight

An item's [[ItemPrototype#weight|weight]] is used to determine how many of it will fit on a rocket to supply a space platform. It can either be set manually or be calculated automatically based on its recipe(s). This page describes the algorithm for this automatic calculation.

### Algorithm

If an item has the `"only-in-cursor"` and `"spawnable"` [[ItemPrototypeFlags|flags]], its weight will be `0`.

If an item has no recipe to produce it, it'll fall back to the [[UtilityConstants#default_item_weight|default item weight]].

The game starts by calculating the *'recipe weight'* of the item's recipe. If an item has multiple recipes, it picks the first recipe, according to the sorting described at the [bottom](#recipe-ordering) of this page. The recipe weight is then calculated by iterating over all ingredients:

- For each item ingredient, the weight is increased by `item_weight * item_ingredient_count`. Note that to do this, it needs to determine the weight of all ingredients first. If this results in a recipe loop, it will fall back to the [[UtilityConstants#default_item_weight|default item weight]] for that item.
- For each fluid ingredient, the weight is increased by `fluid_ingredient_amount * 100`.

If the resulting recipe weight is `0`, the item's weight will fall back to the [[UtilityConstants#default_item_weight|default item weight]].

The game then determines the *product count* of the recipe by iterating all products and adding up the expected (ie. after probabilities) count for all item products. Fluid products are skipped.

If the recipe's product count is `0`, the item's weight will fall back to the [[UtilityConstants#default_item_weight|default item weight]].

Next, an *intermediate result* will be determined as `(recipe_weight / product_count) * ingredient_to_weight_coefficient` (see [[ItemPrototype#ingredient_to_weight_coefficient|ingredient_to_weight_coefficient]], which defaults to `0.5`).

Following this, if a recipe doesn't support productivity, its *simple result* is determined as `rocket_lift_weight / stack_size` (see [[UtilityConstants#rocket_lift_weight|rocket_lift_weight]] and [[ItemPrototype#stack_size|stack_size]]). If this simple result is larger than or equal to the intermediate result, it becomes the item's weight.

Otherwise, the game determines the amount of stacks that would result from the intermediate result as `rocket_lift_weight / intermediate_result / stack_size`. If this amount is less than or equal to `1`, the intermediate result becomes the item's weight. Else, the item's weight is set to `rocket_lift_weight / floor(stack_amount) / stack_size`.

### Example

This is an example of how the `electronic-circuit` item gets its weight. Note that because this algorithm has many branching paths, this one example doesn't cover all of them.

<div class="codehilite" style="background: #263238">

```
-- the global default_item_weight is 100
-- the global rocket_lift_weight is 1000000
-- the item has an ingredient_to_weight_coefficient of 0.28
```

</div>

The electronic circuit item has a recipe of the same name, which is thus used for calculating the item weight.

<div class="codehilite" style="background: #263238">

```
-- electronic circuit recipe ingredients and weights
ingredients = {
    {type = "item", name = "iron-plate", amount = 1},  -- weight of 1000
    {type = "item", name = "copper-cable", amount = 3}  -- weight of 250
}
-- the recipe's weight is thus: 1 * 1000 + 3 * 250 = 1750

-- electronic circuit recipe products
results = { {type="item", name="electronic-circuit", amount=1} }
-- the recipe's product count is thus 1
```

</div>

The recipe weight and product count is more than `0`, so we continue on.

The intermediate result is then determined to be `1750 / 1 * 0.28 = 490`.

The recipe supports productivity, so the simple result branch is skipped.

The stack count is determined to be `1000000 / 490 / 200 = 10.2`. This is bigger than `1`, so we continue on.

The final weight is thus determined to be `1000000 / floor(10.2) / 200 = 500`.

### Recipe Ordering

Items can have multiple recipes to produce them. These recipes are ordered in a particular way to determine which one is used for determining item weight.

Note that recipes that are [[PrototypeBase#hidden|hidden]] or don't [[RecipePrototype#allow_decomposition|allow_decomposition]] are not considered for this use case.

The sorting works by considering the following attributes in order, preferring recipes that fulfill them:

- The name of the recipe is identical to the item name.
- The recipe is *not* using the item as a catalyst.
- The recipe can be used as an [[RecipePrototype#allow_as_intermediate|intermediate]] while hand-crafting.
- The recipe's [[RecipePrototype#category|category]], [[PrototypeBase#subgroup|subgroup]], then [[PrototypeBase#order|order]].

