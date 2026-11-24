---
title: on_mod_item_opened
tags: [factorio-api, runtime, event]
---
# on_mod_item_opened

Called when the player uses the 'Open item GUI' control on an item defined with the 'mod-openable' flag

## Data

### player_index
- **Type:** [[uint32]]
The player.

### item
- **Type:** [[LuaItemPrototype]]
The item clicked on.

### quality
- **Type:** [[LuaQualityPrototype]]
The item quality clicked on.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
