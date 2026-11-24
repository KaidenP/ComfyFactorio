---
title: FurnacePrototype
tags: [factorio-api, prototype]
---
# FurnacePrototype

> **Parent:** [[CraftingMachinePrototype]] · **Type name:** `furnace`

A furnace. Normal furnaces only process "smelting" category recipes, but you can make furnaces that process other [[RecipeCategory|recipe categories]].

The difference to assembling machines is that furnaces automatically choose their recipe based on input. See [[furnace-recipe-selection|Furnace Recipe Selection]] for how the recipe is chosen.

## Properties

### result_inventory_size
- **Type:** [[ItemStackIndex (type)]]
The number of output slots.

### source_inventory_size
- **Type:** [[ItemStackIndex (type)]]
The number of input slots, but not more than 1.

### cant_insert_at_source_message_key
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"inventory-restriction.cant-be-smelted"`
The locale key of the message shown when the player attempts to insert an item into the furnace that cannot be processed by that furnace. In-game, the locale is provided the `__1__` parameter, which is the localised name of the item.

The locale key is also used with an `_until` suffix for items that cannot be processed until they recipe is unlocked by a technology.

### custom_input_slot_tooltip_key
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
The locale key of the tooltip to be shown in the input slot instead of the automatically generated list of items that fit there

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### circuit_connector_flipped
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

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
