---
title: on_pre_player_removed
tags: [factorio-api, runtime, event]
---
# on_pre_player_removed

Called before a player is removed (deleted) from the game. This is markedly different from a player temporarily [[on_player_left_game|leaving]] the game, and instead behaves like the player never existed in the save file.

## Data

### player_index
- **Type:** [[uint32]]
The index of the removed player.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
