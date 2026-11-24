---
title: on_market_item_purchased
tags: [factorio-api, runtime, event]
---
# on_market_item_purchased

Called after a player purchases some offer from a `market` entity.

## Data

### player_index
- **Type:** [[uint32]]
The player who did the purchasing.

### market
- **Type:** [[LuaEntity]]
The market entity.

### offer_index
- **Type:** [[uint32]]
The index of the offer purchased.

### count
- **Type:** [[uint32]]
The amount of offers purchased.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
