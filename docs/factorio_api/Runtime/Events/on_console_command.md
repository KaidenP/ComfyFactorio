---
title: on_console_command
tags: [factorio-api, runtime, event]
---
# on_console_command

Called when someone enters a command-like message regardless of it being a valid command.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player if any.

### command
- **Type:** [[string]]
The command as typed without the preceding forward slash ('/').

### parameters
- **Type:** [[string]]
The parameters provided if any.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
