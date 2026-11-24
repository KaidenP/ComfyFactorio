---
title: on_lua_shortcut
tags: [factorio-api, runtime, event]
---
# on_lua_shortcut

Called when a custom [[ShortcutPrototype|Lua shortcut]] is pressed.

## Data

### player_index
- **Type:** [[uint32]]

### prototype_name
- **Type:** [[string]]
Shortcut prototype name of the shortcut that was clicked.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
