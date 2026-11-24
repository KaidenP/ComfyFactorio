---
title: CustomCommandData
tags: [factorio-api, runtime, concept]
---
# CustomCommandData

## Fields

### name
- **Type:** [[string]]
The name of the command.

### tick
- **Type:** [[MapTick]]
The tick the command was used in.

### player_index
- **Type:** [[uint32]]
- **Optional**
The player who issued the command, or `nil` if it was issued from the server console.

### parameter
- **Type:** [[string]]
- **Optional**
The parameter passed after the command, if there is one.
