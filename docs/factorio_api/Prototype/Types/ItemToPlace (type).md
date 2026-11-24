---
title: ItemToPlace
tags: [factorio-api, prototype, type]
---
# ItemToPlace

*Note: `ItemToPlace (type)`.*

Item that when placed creates this entity/tile.

## Properties

### item
- **Type:** [[ItemID (type)]]
The item used to place this entity/tile.

### count
- **Type:** [[ItemCountType (type)]]
How many items are used to place one of this entity/tile. Can't be larger than the stack size of the item.

## Examples

```
{item = "iron-chest", count = 1}
```
