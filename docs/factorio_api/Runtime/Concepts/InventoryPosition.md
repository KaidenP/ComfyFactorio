---
title: InventoryPosition
tags: [factorio-api, runtime, concept]
---
# InventoryPosition

## Fields

### inventory
- **Type:** [[defines.inventory]]
The ID of the inventory to insert into.

### stack
- **Type:** [[ItemStackIndex]]
The stack index of the inventory to insert into. Uses 0-based indexing, in contrast to the 1-based indexing of most other inventory-related functions.

### count
- **Type:** [[ItemCountType]]
- **Optional**
How many items to insert. Defaults to `1`.
