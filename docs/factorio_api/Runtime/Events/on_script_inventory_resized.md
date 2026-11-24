---
title: on_script_inventory_resized
tags: [factorio-api, runtime, event]
---
# on_script_inventory_resized

Called just after a script inventory is resized.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
If done by console command; the player who ran the command.

### mod
- **Type:** [[string]]
The mod that did the resizing. This will be `"core"` if done by console command or scenario script.

### inventory
- **Type:** [[LuaInventory]]

### old_size
- **Type:** [[uint32]]
The old inventory size.

### new_size
- **Type:** [[uint32]]
The new inventory size.

### overflow_inventory
- **Type:** [[LuaInventory]]
Any items which didn't fit into the new inventory size.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
