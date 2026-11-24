---
title: on_pre_player_crafted_item
tags: [factorio-api, runtime, event]
---
# on_pre_player_crafted_item

Called when a player queues something to be crafted.

## Data

### player_index
- **Type:** [[uint32]]
The player doing the crafting.

### recipe
- **Type:** [[LuaRecipe]]
The recipe being queued.

### items
- **Type:** [[LuaInventory]]
The items removed from the players inventory to do the crafting.

### queued_count
- **Type:** [[uint32]]
The number of times the recipe is being queued.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
