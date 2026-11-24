---
title: ItemInventoryPositions
tags: [factorio-api, runtime, concept]
---
# ItemInventoryPositions

## Fields

### in_inventory
- **Type:** array<[[InventoryPosition]]>
- **Optional**
A list of stacks into which items should be inserted.

### grid_count
- **Type:** [[ItemCountType]]
- **Optional**
Defaults to `0`. Number of items to request for the equipment grid. When the items arrive they will be used to revive the first matching ghost equipment.
