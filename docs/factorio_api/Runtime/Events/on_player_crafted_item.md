---
title: on_player_crafted_item
tags: [factorio-api, runtime, event]
---
# on_player_crafted_item

Called when the player finishes crafting an item. This event fires just before the results are inserted into the player's inventory, not when the crafting is queued (see [[on_pre_player_crafted_item]]).

## Data

### item_stack
- **Type:** [[LuaItemStack]]
The item that has been crafted.

### player_index
- **Type:** [[uint32]]
The player doing the crafting.

### recipe
- **Type:** [[LuaRecipe]]
The recipe used to craft this item.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
