---
title: AssemblingMachinePrototype
tags: [factorio-api, prototype]
---
# AssemblingMachinePrototype

> **Parent:** [[CraftingMachinePrototype]] · **Type name:** `assembling-machine`

An assembling machine - like the assembling machines 1/2/3 in the game, but you can use your own recipe categories.

## Properties

### fixed_recipe
- **Type:** [[RecipeID (type)]]
- **Optional**
- **Default:** `""`
The preset recipe of this machine. This machine does not show a recipe selection if this is set. The base game uses this for the [rocket silo](https://wiki.factorio.com/Rocket_silo).

### fixed_quality
- **Type:** [[QualityID (type)]]
- **Optional**
Only loaded if `fixed_recipe` is defined.

### gui_title_key
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
The locale key of the title of the recipe selection GUI that is shown when the player opens the assembling machine. May not be longer than 200 characters.

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### default_recipe_finished_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_working_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### ingredient_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `65535`
Sets the maximum number of item ingredients this machine can craft with. Any recipe with more item ingredients than this will be unavailable in this machine.

This only counts item ingredients, not fluid ingredients! This means if ingredient count is 2, and the recipe has 2 item ingredients and 1 fluid ingredient, it can still be crafted in the machine.

### max_item_product_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `65535`

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### circuit_connector_flipped
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### fluid_boxes_off_when_no_fluid_recipe
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the [[CraftingMachinePrototype#fluid_boxes|fluid boxes]] are disabled when this assembling machine has no recipe set.

If a recipe is set, this property does not affect fluidbox behavior. Instead, whether fluidboxes are enabled depends on whether the recipe needs them, e.g. if a recipe without fluid ingredients is set, the input fluidboxes will be disabled.

### disabled_when_recipe_not_researched
- **Type:** [[boolean (type)]]
- **Optional**
Defaults to true if `fixed_recipe` is not given.
