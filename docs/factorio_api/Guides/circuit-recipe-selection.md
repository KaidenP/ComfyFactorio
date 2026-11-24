---
title: circuit-recipe-selection
tags: [factorio-api, guide]
---
## Circuit Recipe Selection

This page describes how the [[LuaAssemblingMachineControlBehavior#circuit_set_recipe|'Set recipe']] option on crafting machines selects a recipe from the signals it receives.

The machine goes through all incoming signals in their usual order. Any signal whose value is negative or zero is ignored. Any `"virtual"`, `"space-location"`, `"asteroid-chunk"`, and `"quality"` signal is ignored as well.

If a `"recipe"` signal is present which is researched and can be crafted in the machine, it will be selected straight away. Otherwise, the machine considers the remaining signal types.

It first searches through all `"item"` signals, going over all recipes that can produce each item (excluding recipes where the item is a catalyst only). These recipes are iterated in their usual ordering, which means by [[RecipePrototype#category|category]], [[PrototypeBase#subgroup|subgroup]], [[PrototypeBase#order|order]], then [[PrototypeBase#name|name]]. If any is researched and can be crafted in the machine, it is selected.

If no item signal leads to a selection, the machine searches through all `"entity"` signals. It picks the items that can be used to build the entity and applies the same method to them as it does for item signals.

If no entity signal leads to a selection, the machine searches through all `"fluid"` signals. It uses the same method as it does for item signals.

If no relevant recipe is found this way, none is selected and the machine will be idle.

