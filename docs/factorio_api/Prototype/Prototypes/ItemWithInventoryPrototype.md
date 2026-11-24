---
title: ItemWithInventoryPrototype
tags: [factorio-api, prototype]
---
# ItemWithInventoryPrototype

> **Parent:** [[ItemWithLabelPrototype]] · **Type name:** `item-with-inventory`

The inventory allows setting player defined filters similar to cargo wagon inventories.

## Properties

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
The inventory size of the item.

### quality_affects_inventory_size
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### item_filters
- **Type:** array<[[ItemID (type)]]>
- **Optional**
A list of explicit item names to be used as filters.
**Examples:**

```
item_filters = {"iron-ore", "copper-ore", "coal", "stone"}
```

### item_group_filters
- **Type:** array<[[ItemGroupID (type)]]>
- **Optional**
A list of explicit item group names to be used as filters.
**Examples:**

```
item_group_filters = {"logistics", "fluids"}
```

### item_subgroup_filters
- **Type:** array<[[ItemSubGroupID]]>
- **Optional**
A list of explicit [[ItemSubGroup|item subgroup]] names to be used as filters.
**Examples:**

```
item_subgroup_filters = {"military-equipment", "tool"}
```

### filter_mode
- **Type:** `"blacklist"` | `"whitelist"`
- **Optional**
- **Default:** `"whitelist"`
This determines how filters are applied. If no filters are defined this is automatically set to "none".
**Examples:**

```
filter_mode = "blacklist"
```

### filter_message_key
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"item-limitation.item-not-allowed-in-this-container-item"`
The locale key used when the player attempts to put an item that doesn't match the filter rules into the item-with-inventory.

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```
