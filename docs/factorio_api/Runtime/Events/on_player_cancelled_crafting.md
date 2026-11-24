---
title: on_player_cancelled_crafting
tags: [factorio-api, runtime, event]
---
# on_player_cancelled_crafting

Called when a player cancels crafting.

## Data

### player_index
- **Type:** [[uint32]]
The player that did the crafting.

### items
- **Type:** [[LuaInventory]]
The crafting items returned to the player's inventory.

### recipe
- **Type:** [[LuaRecipe]]
The recipe that has been cancelled.

### cancel_count
- **Type:** [[uint32]]
The number of crafts that have been cancelled.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
